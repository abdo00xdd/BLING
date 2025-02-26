import time
import os
import pygame
import tkinter as tk
from tkinter import messagebox

# Global variables
remaining_time = 0  # To hold remaining time when paused
pquse = False

# Check if pygame is available
try:
    pygame.mixer.init()
    SOUND_ENABLED = True
except Exception as e:
    SOUND_ENABLED = False
    print(f"pygame not found or failed to initialize. Sound disabled. Error: {e}")

def play_sound():
    """Play the alarm sound using pygame."""
    if SOUND_ENABLED and os.path.exists("alarm.mp3"):
        try:
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")
    else:
        print("Alarm sound file not found or sound is disabled.")

def update_timer(label):
    """Update the countdown every second."""
    global remaining_time, pquse

    if remaining_time > 0 and not pquse:
        mins, secs = divmod(remaining_time, 60)
        label.config(text=f'{mins:02}:{secs:02}')
        remaining_time -= 1
        label.after(1000, update_timer, label)
    elif remaining_time == 0:
        label.config(text="Time's up!")
        play_sound()

def start_timer():
    """Start the timer with user input."""
    global remaining_time, pquse
    try:
        t = int(entry.get())
        if t <= 0:
            raise ValueError("Time must be a positive integer.")
        remaining_time = t
        pquse = False
        update_timer(timer_label)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

def pause_timer():
    """Pause the timer."""
    global pquse
    pquse = True

def resume_timer():
    """Resume the timer."""
    global pquse
    pquse = False
    update_timer(timer_label)

# Create main window
root = tk.Tk()
root.title("Countdown Timer")

# Entry for user input
entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack(pady=10)

# Timer display
timer_label = tk.Label(root, font=('Helvetica', 48), text="00:00")
timer_label.pack(pady=10)

# Buttons
start_button = tk.Button(root, text="Start Timer", font=('Helvetica', 20), command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", font=('Helvetica', 20), command=pause_timer)
pause_button.pack(pady=5)

resume_button = tk.Button(root, text="Resume", font=('Helvetica', 20), command=resume_timer)
resume_button.pack(pady=5)

# Run the app
root.mainloop()
