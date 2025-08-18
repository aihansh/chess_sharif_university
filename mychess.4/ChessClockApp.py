#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ساعت شطرنج با پایتون (tkinter)

ویژگی‌ها:
- دو تایمر مستقل با فرمت mm:ss.t
- افزونه‌ی فیشری (Fischer Increment) پس از هر حرکت
- کلیدهای میانبر: 
  * Space: شروع/توقف
  * A یا Left Shift: پایان نوبت بازیکن چپ (شروع نوبت راست)
  * L یا Right Shift: پایان نوبت بازیکن راست (شروع نوبت چپ)
  * R: ریست
  * S: جابه‌جایی طرفین
  * T: تنظیم زمان پایه و افزونه
- شمارش حرکت‌ها
- تشخیص اتمام زمان (پرچم)

بدون وابستگی خارجی؛ با Python 3 و tkinter اجرا می‌شود.
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

MS_STEP = 100  # فاصله‌ی به‌روزرسانی به میلی‌ثانیه (0.1 ثانیه)

class PlayerClock:
    def __init__(self, name: str, base_ms: int):
        self.name = name
        self.base_ms = base_ms
        self.time_ms = base_ms
        self.moves = 0

    def reset(self):
        self.time_ms = self.base_ms
        self.moves = 0

class ChessClockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Clock ⏱️")
        self.geometry("560x360")
        self.minsize(480, 320)
        self.configure(bg="#0f172a")  # slate-900

        # تنظیمات پیش‌فرض: 5 دقیقه به‌علاوه 3 ثانیه افزونه
        self.base_minutes = 10
        self.increment_seconds = 3

        base_ms = self.base_minutes * 60 * 1000
        self.left = PlayerClock("Left", base_ms)
        self.right = PlayerClock("Right", base_ms)

        self.running = False
        self.active_side = None  # 'left' یا 'right'
        self.after_id = None
        self.flag_fallen = False

        self._build_ui()
        self._bind_keys()
        self._update_labels()

    # ---------------- UI -----------------
    def _build_ui(self):
        # استایل‌ها
        style = ttk.Style(self)
        try:
            style.theme_use('clam')
        except:
            pass
        style.configure("TButton", padding=6)

        # قاب بالا: دکمه‌ها
        top = ttk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.X, padx=12, pady=10)

        self.btn_start = ttk.Button(top, text="شروع", command=self.toggle_start)
        self.btn_start.pack(side=tk.LEFT, padx=6)

        self.btn_reset = ttk.Button(top, text="ریست (R)", command=self.reset_all)
        self.btn_reset.pack(side=tk.LEFT, padx=6)

        self.btn_swap = ttk.Button(top, text="جابه‌جایی (S)", command=self.swap_sides)
        self.btn_swap.pack(side=tk.LEFT, padx=6)

        self.btn_settings = ttk.Button(top, text="تنظیمات (T)", command=self.open_settings)
        self.btn_settings.pack(side=tk.LEFT, padx=6)

        # قاب تایمرها
        body = ttk.Frame(self)
        body.pack(expand=True, fill=tk.BOTH, padx=12, pady=10)
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        # سمت چپ
        self.left_frame = tk.Frame(body, bg="#111827", bd=0, highlightthickness=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0,6))
        self.left_label = tk.Label(self.left_frame, text="05:00.0", font=("SF Pro Display", 44, "bold"),
                                   bg="#111827", fg="#e5e7eb")
        self.left_label.pack(expand=True)
        self.left_info = tk.Label(self.left_frame, text="حرکت‌ها: 0", font=("SF Pro Text", 12),
                                  bg="#111827", fg="#9ca3af")
        self.left_info.pack(pady=(0,10))
        self.left_frame.bind("<Button-1>", lambda e: self.press('left'))
        self.left_label.bind("<Button-1>", lambda e: self.press('left'))

        # سمت راست
        self.right_frame = tk.Frame(body, bg="#111827", bd=0, highlightthickness=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(6,0))
        self.right_label = tk.Label(self.right_frame, text="05:00.0", font=("SF Pro Display", 44, "bold"),
                                    bg="#111827", fg="#e5e7eb")
        self.right_label.pack(expand=True)
        self.right_info = tk.Label(self.right_frame, text="حرکت‌ها: 0", font=("SF Pro Text", 12),
                                   bg="#111827", fg="#9ca3af")
        self.right_info.pack(pady=(0,10))
        self.right_frame.bind("<Button-1>", lambda e: self.press('right'))
        self.right_label.bind("<Button-1>", lambda e: self.press('right'))

        # نوار وضعیت پایین
        self.status = tk.Label(self, text=self._status_text(), anchor='w',
                               bg="#0f172a", fg="#a1a1aa", padx=12)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def _bind_keys(self):
        self.bind('<space>', lambda e: self.toggle_start())
        self.bind('r', lambda e: self.reset_all())
        self.bind('R', lambda e: self.reset_all())
        self.bind('s', lambda e: self.swap_sides())
        self.bind('S', lambda e: self.swap_sides())
        self.bind('t', lambda e: self.open_settings())
        self.bind('T', lambda e: self.open_settings())
        # پایان نوبت هر طرف
        self.bind('a', lambda e: self.press('left'))
        self.bind('A', lambda e: self.press('left'))
        self.bind('<Shift-L>', lambda e: self.press('left'))
        self.bind('l', lambda e: self.press('right'))
        self.bind('L', lambda e: self.press('right'))
        self.bind('<Shift-R>', lambda e: self.press('right'))

    # -------------- منطق ---------------
    def toggle_start(self):
        if self.flag_fallen:
            # اگر پرچم افتاده، ریست لازم است
            self.reset_all()
            return
        if not self.running:
            # اگر هنوز طرف فعال مشخص نشده، با راست شروع می‌کنیم (مثل شطرنج: سفید اول حرکت می‌کند)
            if self.active_side is None:
                self.active_side = 'right'
            self.running = True
            self.btn_start.config(text="توقف")
            self._tick()
        else:
            self.running = False
            self.btn_start.config(text="ادامه")
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
        self._update_status()

    def press(self, side: str):
        """بازیکنی که حرکتش تمام شده را می‌گیریم تا نوبت عوض شود.
        side همان طرفی است که روی ناحیه‌اش کلیک یا کلیدش را زده‌اند."""
        if not self.running or self.flag_fallen:
            return
        if self.active_side is None:
            return
        # اگر روی طرفی کلیک شد که نوبت او نیست، نادیده بگیر
        if side != self.active_side:
            return
        # افزودن افزونه به بازیکنی که حرکتش را تمام کرد
        self._add_increment(side)
        # تغییر نوبت
        self.active_side = 'left' if side == 'right' else 'right'
        # شمارش حرکت برای بازیکنی که حرکتش را تمام کرد
        p = self.left if side == 'left' else self.right
        p.moves += 1
        self._update_labels()
        self._update_status()

    def _add_increment(self, side: str):
        inc_ms = self.increment_seconds * 1000
        p = self.left if side == 'left' else self.right
        p.time_ms += inc_ms

    def _tick(self):
        if not self.running or self.active_side is None:
            return
        # کم کردن زمان طرف فعال
        p = self.left if self.active_side == 'left' else self.right
        p.time_ms -= MS_STEP
        if p.time_ms <= 0:
            p.time_ms = 0
            self.running = False
            self.flag_fallen = True
            self.btn_start.config(text="شروع")
            self._update_labels()
            self._update_status(flag_side=self.active_side)
            try:
                self.bell()
            except:
                pass
            return
        self._update_labels()
        self.after_id = self.after(MS_STEP, self._tick)

    def reset_all(self):
        self.running = False
        self.flag_fallen = False
        self.active_side = None
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        self.left.base_ms = self.base_minutes * 60 * 1000
        self.right.base_ms = self.base_minutes * 60 * 1000
        self.left.reset()
        self.right.reset()
        self.btn_start.config(text="شروع")
        self._update_labels()
        self._update_status()

    def swap_sides(self):
        # جابه‌جایی داده‌ها و UI دو طرف
        self.left, self.right = self.right, self.left
        if self.active_side is not None:
            self.active_side = 'left' if self.active_side == 'right' else 'right'
        self._update_labels()
        self._update_status()

    def open_settings(self):
        if self.running:
            messagebox.showinfo("تنظیمات", "برای تغییر تنظیمات ابتدا تایمر را متوقف کنید (Space).")
            return
        m = simpledialog.askinteger("زمان پایه", "دقایق هر بازیکن؟", minvalue=1, maxvalue=180, initialvalue=self.base_minutes)
        if m is None:
            return
        inc = simpledialog.askinteger("افزونه فیشری", "ثانیه افزوده پس از هر حرکت؟", minvalue=0, maxvalue=60, initialvalue=self.increment_seconds)
        if inc is None:
            return
        self.base_minutes = int(m)
        self.increment_seconds = int(inc)
        self.reset_all()

    # -------------- کمک‌ها --------------
    def _format_time(self, ms: int) -> str:
        if ms < 0:
            ms = 0
        total_sec = ms // 1000
        minutes = total_sec // 60
        seconds = total_sec % 60
        tenths = (ms % 1000) // 100
        if minutes < 100:
            return f"{minutes:02d}:{seconds:02d}.{tenths}"
        else:
            # در زمان‌های خیلی طولانی فقط mm:ss نشان بده
            return f"{minutes:02d}:{seconds:02d}"

    def _status_text(self, flag_side: str | None = None) -> str:
        if self.flag_fallen:
            loser = "چپ" if flag_side == 'left' else "راست"
            return f"اتمام زمان! طرف {loser} باخت. (R برای ریست)"
        if not self.running:
            return "Space: شروع/توقف • A/LeftShift: نوبت چپ • L/RightShift: نوبت راست • T: تنظیمات • R: ریست"
        turn = "چپ" if self.active_side == 'left' else "راست"
        return f"نوبت فعال: {turn}. برای پایان نوبت کلید مربوطه را بزنید."

    def _update_status(self, flag_side: str | None = None):
        self.status.config(text=self._status_text(flag_side))

    def _update_labels(self):
        # رنگ‌ها بسته به نوبت فعال
        def fg_for(side):
            if self.flag_fallen:
                return "#fca5a5"  # قرمز ملایم در باخت
            if self.active_side == side and self.running:
                return "#86efac"  # سبز ملایم
            return "#e5e7eb"  # خاکستری روشن

        self.left_label.config(text=self._format_time(self.left.time_ms), fg=fg_for('left'))
        self.right_label.config(text=self._format_time(self.right.time_ms), fg=fg_for('right'))
        self.left_info.config(text=f"حرکت‌ها: {self.left.moves}")
        self.right_info.config(text=f"حرکت‌ها: {self.right.moves}")


if __name__ == "__main__" :
    app = ChessClockApp()
    app.mainloop()
