import tkinter as tk
from tkinter import font
import time

class BeautifulCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Custom fonts
        self.display_font = font.Font(family="Helvetica", size=28, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=18, weight="bold")
        
        # Color scheme
        self.bg_color = "#1e1e1e"
        self.display_bg = "#2d2d2d"
        self.display_fg = "#ffffff"
        self.number_btn_bg = "#3a3a3a"
        self.operator_btn_bg = "#ff9500"
        self.special_btn_bg = "#a5a5a5"
        self.hover_color = "#4a4a4a"
        self.active_color = "#2a2a2a"
        
        # Initialize variables
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set(self.current_input)
        
        self.display = tk.Label(
            root, 
            textvariable=self.display_var, 
            anchor="e", 
            padx=20,
            pady=15,
            font=self.display_font,
            bg=self.display_bg,
            fg=self.display_fg,
            relief="flat",
            bd=0
        )
        self.display.pack(fill=tk.X, padx=10, pady=(20, 10))
        
        # Create buttons frame
        self.buttons_frame = tk.Frame(root, bg=self.bg_color)
        self.buttons_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('C', 0, 0, 'special'), ('±', 0, 1, 'special'), ('%', 0, 2, 'special'), ('/', 0, 3, 'operator'),
            ('7', 1, 0, 'number'), ('8', 1, 1, 'number'), ('9', 1, 2, 'number'), ('*', 1, 3, 'operator'),
            ('4', 2, 0, 'number'), ('5', 2, 1, 'number'), ('6', 2, 2, 'number'), ('-', 2, 3, 'operator'),
            ('1', 3, 0, 'number'), ('2', 3, 1, 'number'), ('3', 3, 2, 'number'), ('+', 3, 3, 'operator'),
            ('0', 4, 0, 'number', 2), ('.', 4, 2, 'number'), ('=', 4, 3, 'operator')
        ]
        
        # Create buttons with effects
        self.button_widgets = {}
        for button_info in buttons:
            if len(button_info) == 4:
                text, row, col, btn_type = button_info
                colspan = 1
            else:
                text, row, col, btn_type, colspan = button_info
                
            btn = tk.Button(
                self.buttons_frame, 
                text=text, 
                font=self.button_font,
                borderwidth=0,
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            )
            
            # Configure button colors based on type
            if btn_type == 'number':
                btn.config(
                    bg=self.number_btn_bg,
                    fg="white",
                    activebackground=self.active_color,
                    activeforeground="white"
                )
            elif btn_type == 'operator':
                btn.config(
                    bg=self.operator_btn_bg,
                    fg="white",
                    activebackground="#e68a00",
                    activeforeground="white"
                )
            elif btn_type == 'special':
                btn.config(
                    bg=self.special_btn_bg,
                    fg="black",
                    activebackground="#959595",
                    activeforeground="black"
                )
            
            # Add hover effects
            btn.bind("<Enter>", lambda e, b=btn: self.on_enter(e, b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(e, b))
            
            # Add press animation
            btn.bind("<Button-1>", lambda e, b=btn: self.on_press(b))
            
            btn.grid(
                row=row, 
                column=col, 
                columnspan=colspan,
                sticky="nsew", 
                padx=3, 
                pady=3,
                ipadx=10,
                ipady=10
            )
            
            self.button_widgets[text] = btn
        
        # Configure grid weights
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
        
        # Make 0 button wider
        self.buttons_frame.columnconfigure(1, weight=1)
    
    def on_enter(self, event, button):
        """Button hover effect"""
        current_bg = button.cget("bg")
        if current_bg == self.number_btn_bg:
            button.config(bg=self.hover_color)
        elif current_bg == self.operator_btn_bg:
            button.config(bg="#ffaa00")
        elif current_bg == self.special_btn_bg:
            button.config(bg="#b5b5b5")
    
    def on_leave(self, event, button):
        """Reset button color after hover"""
        current_text = button.cget("text")
        if current_text in '0123456789.':
            button.config(bg=self.number_btn_bg)
        elif current_text in '+-*/=%':
            button.config(bg=self.operator_btn_bg)
        else:
            button.config(bg=self.special_btn_bg)
    
    def on_press(self, button):
        """Button press animation"""
        original_bg = button.cget("bg")
        darker_bg = self.darken_color(original_bg, 20)
        button.config(bg=darker_bg)
        button.after(100, lambda: button.config(bg=original_bg))
    
    def darken_color(self, color, percent):
        """Helper function to darken a color"""
        # Convert hex to RGB
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        # Darken each component
        r = max(0, r - int(r * percent / 100))
        g = max(0, g - int(g * percent / 100))
        b = max(0, b - int(b * percent / 100))
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.handle_digit(button_text)
        elif button_text == 'C':
            self.handle_clear()
        elif button_text in '+-*/':
            self.handle_operation(button_text)
        elif button_text == '=':
            self.handle_equals()
        elif button_text == '±':
            self.handle_negate()
        elif button_text == '%':
            self.handle_percentage()
        
        self.display_var.set(self.current_input)
    
    def handle_digit(self, digit):
        if self.reset_input:
            self.current_input = "0"
            self.reset_input = False
            
        if digit == '.':
            if '.' not in self.current_input:
                self.current_input += digit
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
    
    def handle_clear(self):
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = False
    
    def handle_operation(self, op):
        try:
            if self.operation and not self.reset_input:
                self.calculate_result()
            
            self.stored_value = float(self.current_input)
            self.operation = op
            self.reset_input = True
        except ValueError:
            self.current_input = "Error"
            self.reset_input = True
    
    def handle_equals(self):
        if self.operation and not self.reset_input:
            self.calculate_result()
            self.operation = None
    
    def handle_negate(self):
        if self.current_input != "0":
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
    
    def handle_percentage(self):
        try:
            value = float(self.current_input) / 100
            if value.is_integer():
                self.current_input = str(int(value))
            else:
                self.current_input = str(value)
        except:
            self.current_input = "Error"
            self.reset_input = True
    
    def calculate_result(self):
        try:
            current_value = float(self.current_input)
            
            if self.operation == '+':
                result = self.stored_value + current_value
            elif self.operation == '-':
                result = self.stored_value - current_value
            elif self.operation == '*':
                result = self.stored_value * current_value
            elif self.operation == '/':
                if current_value == 0:
                    raise ZeroDivisionError
                result = self.stored_value / current_value
            
            # Format result to remove unnecessary decimal places
            if result.is_integer():
                self.current_input = str(int(result))
            else:
                self.current_input = "{:.10f}".format(result).rstrip('0').rstrip('.')
            
            self.reset_input = True
        except ZeroDivisionError:
            self.current_input = "Error"
            self.reset_input = True
        except:
            self.current_input = "Error"
            self.reset_input = True

if __name__ == "__main__":
    root = tk.Tk()
    calculator = BeautifulCalculator(root)
    
    # Add some additional styling
    try:
        from ttkthemes import ThemedTk
        root = ThemedTk(theme="equilux")
        calculator = BeautifulCalculator(root)
    except:
        pass  # Use default if ttkthemes is not available
    
    root.mainloop()