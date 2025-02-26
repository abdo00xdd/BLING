import tkinter as tk
from tkinter import messagebox
import threading

# Global variables
remaining_time = 0
is_paused = False
current_phase = ""

# Pomodoro Timer App
def start_timer():
    global remaining_time, is_paused, current_phase
    try:
        work_time = int(work_entry.get()) * 60
        break_time = int(break_entry.get()) * 60
        start_btn.config(state='disabled')
        current_phase = "Work"
        remaining_time = work_time
        update_timer()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for work and break times.")

def update_timer():
    global remaining_time, is_paused, current_phase
    if remaining_time > 0 and not is_paused:
        mins, secs = divmod(remaining_time, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        bling_label.config(text="BLING", font=("Helvetica", 10, "bold"), fg="orange")
        remaining_time -= 1
        root.after(1000, update_timer)
    elif remaining_time == 0:
        if current_phase == "Work":
            current_phase = "Break"
            remaining_time = int(break_entry.get()) * 60
            update_timer()
        else:
            timer_label.config(text="Cycle Complete!")
            bling_label.config(text="BLING", font=("Helvetica", 10, "bold"), fg="red")
            start_btn.config(state='normal')

def pause_timer():
    global is_paused
    is_paused = True

def resume_timer():
    global is_paused
    is_paused = False
    update_timer()

def start_thread():
    threading.Thread(target=start_timer, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("350x600")
root.configure(bg="#002244")

# Timer Display Frame
timer_frame = tk.Frame(root, bg="#002244")
timer_frame.pack(pady=20)

# Timer Circle
timer_label = tk.Label(timer_frame, text="25:00", font=("Helvetica", 48, "bold"), fg="white", bg="#002244")
timer_label.pack()

# BLING Watermark
bling_label = tk.Label(timer_frame, text="BLING", font=("Helvetica", 12, "bold"), fg="orange", bg="#002244")
bling_label.pack()

# Control Buttons
button_frame = tk.Frame(root, bg="#002244")
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="Start", command=start_thread, font=("Helvetica", 16), bg="#FF6600", fg="white", width=12)
start_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(button_frame, text="Pause", command=pause_timer, font=("Helvetica", 16), bg="#FFCC00", fg="black", width=12)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(button_frame, text="Resume", command=resume_timer, font=("Helvetica", 16), bg="#00CC66", fg="white", width=12)
resume_btn.grid(row=0, column=2, padx=5)

# Work and Break Time Entry
entry_frame = tk.Frame(root, bg="#002244")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Work Time (min):", font=("Helvetica", 14), fg="white", bg="#002244").grid(row=0, column=0, padx=5)
work_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=5)
work_entry.grid(row=0, column=1)
work_entry.insert(0, "25")

tk.Label(entry_frame, text="Break Time (min):", font=("Helvetica", 14), fg="white", bg="#002244").grid(row=1, column=0, padx=5)
break_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=5)
break_entry.grid(row=1, column=1)
break_entry.insert(0, "5")

# Run App
root.mainloop()

