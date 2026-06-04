import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from playsound import playsound
import threading
import time

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Alarm Clock")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        # Custom font
        self.custom_font = ("Helvetica", 14)
        self.title_font = ("Helvetica", 18, "bold")
        
        # Current time display
        self.time_label = tk.Label(
            root, 
            text="Current Time:", 
            font=self.custom_font
        )
        self.time_label.pack(pady=(20, 5))
        
        self.current_time = tk.StringVar()
        self.time_display = tk.Label(
            root, 
            textvariable=self.current_time, 
            font=("Helvetica", 24, "bold"),
            fg="blue"
        )
        self.time_display.pack()
        
        # Alarm time input
        self.alarm_frame = tk.Frame(root)
        self.alarm_frame.pack(pady=20)
        
        tk.Label(
            self.alarm_frame, 
            text="Set Alarm Time (HH:MM):", 
            font=self.custom_font
        ).grid(row=0, column=0, columnspan=3)
        
        self.hour_var = tk.StringVar(value="12")
        self.minute_var = tk.StringVar(value="00")
        self.ampm_var = tk.StringVar(value="AM")
        
        # Hour dropdown
        tk.OptionMenu(
            self.alarm_frame, 
            self.hour_var, 
            *["{:02d}".format(i) for i in range(1, 13)]
        ).grid(row=1, column=0, padx=5)
        
        # Minute dropdown
        tk.OptionMenu(
            self.alarm_frame, 
            self.minute_var, 
            *["{:02d}".format(i) for i in range(0, 60)]
        ).grid(row=1, column=1, padx=5)
        
        # AM/PM dropdown
        tk.OptionMenu(
            self.alarm_frame, 
            self.ampm_var, 
            *["AM", "PM"]
        ).grid(row=1, column=2, padx=5)
        
        # Set Alarm button
        self.set_button = tk.Button(
            root, 
            text="Set Alarm", 
            font=self.custom_font,
            command=self.set_alarm,
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED,
            bd=3
        )
        self.set_button.pack(pady=10)
        
        # Alarm status
        self.alarm_status = tk.StringVar(value="No alarm set")
        self.status_label = tk.Label(
            root, 
            textvariable=self.alarm_status, 
            font=self.custom_font,
            fg="gray"
        )
        self.status_label.pack()
        
        # Initialize variables
        self.alarm_time = None
        self.alarm_active = False
        
        # Start clock update
        self.update_clock()
    
    def update_clock(self):
        """Update the current time display every second"""
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        self.current_time.set(current_time)
        
        # Check alarm if one is set
        if self.alarm_active and self.alarm_time:
            if now.hour == self.alarm_time.hour and now.minute == self.alarm_time.minute and now.second == 0:
                self.trigger_alarm()
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
    
    def set_alarm(self):
        """Set the alarm time based on user input"""
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            ampm = self.ampm_var.get()
            
            # Convert to 24-hour format
            if ampm == "PM" and hour != 12:
                hour += 12
            elif ampm == "AM" and hour == 12:
                hour = 0
                
            # Get current time
            now = datetime.now()
            
            # Create alarm time (today's date with the specified time)
            self.alarm_time = datetime(
                now.year, 
                now.month, 
                now.day, 
                hour, 
                minute
            )
            
            # If alarm time is in the past, set for tomorrow
            if self.alarm_time < now:
                self.alarm_time = datetime(
                    now.year, 
                    now.month, 
                    now.day + 1, 
                    hour, 
                    minute
                )
            
            self.alarm_active = True
            self.alarm_status.set(f"Alarm set for {self.alarm_time.strftime('%I:%M %p')}")
            self.alarm_status.set(f"Alarm set for {self.alarm_time.strftime('%I:%M %p')}")
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time.strftime('%I:%M %p')}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid time")
    
    def trigger_alarm(self):
        """Play the alarm sound and show alert"""
        self.alarm_active = False
        self.alarm_status.set("Alarm ringing!")
        
        # Play sound in a separate thread to avoid blocking
        threading.Thread(target=self.play_alarm_sound, daemon=True).start()
        
        # Show alert message
        messagebox.showwarning("Alarm", "Time's up! Wake up!")
        
        # Reset status after alarm
        self.alarm_status.set("No alarm set")
    
    def play_alarm_sound(self):
        """Play the alarm sound (using a simple beep if playsound fails)"""
        try:
            # Try to play a sound file (replace with your own file path)
            playsound("alarm.wav")  # You need to have an alarm.wav file in the same directory
        except:
            # Fallback to system beep if sound file not found
            import winsound
            for _ in range(5):  # Beep 5 times
                winsound.Beep(1000, 500)  # 1000Hz for 500ms
                time.sleep(0.2)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()