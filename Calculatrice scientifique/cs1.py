import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np

# Backend: Scientific calculator functions
class SciCalculator:
    def exponential(self, x):
        return math.exp(x)

    def ln(self, x):
        return math.log(x)

    def log10(self, x):
        return math.log10(x)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def tan(self, x):
        return math.tan(x)

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def hyperbolic_sin(self, x):
        return math.sinh(x)

    def hyperbolic_cos(self, x):
        return math.cosh(x)

    def hyperbolic_tan(self, x):
        return math.tanh(x)

    def arctan(self, x):
        return math.atan(x)

    def arcsin(self, x):
        return math.asin(x)

    def arccos(self, x):
        return math.acos(x)

    def factorial(self, x):
        return math.factorial(int(x))

    def nth_root(self, a, n):
        return a ** (1 / n)

    def div(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Error: Division by zero"

    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def parity(self, x):
        return "Even" if int(x) % 2 == 0 else "Odd"

    def average(self, numbers):
        return sum(numbers) / len(numbers)

    def table_of_function(self, func, start, end, step):
        table = []
        x = start
        while x <= end:
            table.append((x, func(x)))
            x += step
        return table

    def deg_to_rad(self, deg):
        return math.radians(deg)

    def rad_to_deg(self, rad):
        return math.degrees(rad)

# Instantiate the calculator backend
calc = SciCalculator()

# GUI using tkinter
class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x700")
        self.configure(bg="lightgray")
        
        # Display for expression/results (calculator screen)
        self.display = tk.Entry(self, font=("Helvetica", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
        
        # Basic calculator buttons (numbers and arithmetic)
        basic_buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        for (text, row, col) in basic_buttons:
            btn = tk.Button(self, text=text, font=("Helvetica", 20),
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Scientific function buttons (first group)
        sci_buttons = [
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('ln', 5, 3),
            ('log', 6, 0), ('exp', 6, 1), ('^', 6, 2), ('√', 6, 3),
            ('n!', 7, 0), ('^y', 7, 1), ('nth√', 7, 2), ('±', 7, 3),
        ]
        for (text, row, col) in sci_buttons:
            btn = tk.Button(self, text=text, font=("Helvetica", 18),
                            command=lambda t=text: self.on_sci_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Plotting row (non-dynamic version)
        self.plot_entry = tk.Entry(self, font=("Helvetica", 16))
        self.plot_entry.grid(row=8, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")
        plot_btn = tk.Button(self, text="Plot", font=("Helvetica", 16),
                             command=self.plot_function)
        plot_btn.grid(row=8, column=3, pady=10, padx=5, sticky="nsew")
        
        # Additional scientific functions (second group)
        extra_buttons = [
            ('sinh', 9, 0), ('cosh', 9, 1), ('tanh', 9, 2), ('asin', 9, 3),
            ('acos', 10, 0), ('atan', 10, 1), ('deg->rad', 10, 2), ('rad->deg', 10, 3),
            ('Table', 11, 0), ('Parity', 11, 1), ('Avg', 11, 2), ('Clr', 11, 3)
        ]
        for (text, row, col) in extra_buttons:
            btn = tk.Button(self, text=text, font=("Helvetica", 16),
                            command=lambda t=text: self.on_sci_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for responsiveness (rows 0 to 11)
        for i in range(12):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        # Build expression for basic arithmetic
        if char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current + char)

    def on_sci_button_click(self, func):
        try:
            current = self.display.get()
            # For functions that need a number input
            if func not in ['Table', 'Clr', 'Avg']:
                if current == "":
                    messagebox.showerror("Error", "Please enter a value")
                    return
                x = float(current)
            
            if func == 'sin':
                result = calc.sin(x)
            elif func == 'cos':
                result = calc.cos(x)
            elif func == 'tan':
                result = calc.tan(x)
            elif func == 'ln':
                result = calc.ln(x)
            elif func == 'log':
                result = calc.log10(x)
            elif func == 'exp':
                result = calc.exponential(x)
            elif func == '√':
                result = math.sqrt(x)
            elif func == 'n!':
                result = calc.factorial(x)
            elif func == '^':
                # Power: prompt for exponent
                exponent = self.simple_input("Enter exponent:")
                result = calc.power(x, float(exponent))
            elif func == 'nth√':
                # nth root: prompt for degree
                n = self.simple_input("Enter degree for nth root:")
                result = calc.nth_root(x, float(n))
            elif func == '±':
                result = -x
            elif func == 'sinh':
                result = calc.hyperbolic_sin(x)
            elif func == 'cosh':
                result = calc.hyperbolic_cos(x)
            elif func == 'tanh':
                result = calc.hyperbolic_tan(x)
            elif func == 'asin':
                result = calc.arcsin(x)
            elif func == 'acos':
                result = calc.arccos(x)
            elif func == 'atan':
                result = calc.arctan(x)
            elif func == 'deg->rad':
                result = calc.deg_to_rad(x)
            elif func == 'rad->deg':
                result = calc.rad_to_deg(x)
            elif func == 'Parity':
                result = calc.parity(x)
            elif func == 'Avg':
                numbers_str = self.simple_input("Enter numbers separated by commas:")
                numbers = [float(num.strip()) for num in numbers_str.split(",")]
                result = calc.average(numbers)
            elif func == 'Table':
                func_expr = self.simple_input("Enter function in terms of x (e.g., sin(x)):")
                start = float(self.simple_input("Enter start value for x:"))
                end = float(self.simple_input("Enter end value for x:"))
                step = float(self.simple_input("Enter step value:"))
                # Create a safe function using math functions
                def f(x_val):
                    safe_dict = {"x": x_val, "sin": math.sin, "cos": math.cos,
                                 "tan": math.tan, "log": math.log, "exp": math.exp,
                                 "sqrt": math.sqrt, "pi": math.pi, "e": math.e}
                    return eval(func_expr, safe_dict)
                table = calc.table_of_function(f, start, end, step)
                self.show_table(table)
                return  # Do not update the main display
            elif func == 'Clr':
                self.display.delete(0, tk.END)
                return
            else:
                result = "Function not implemented"
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def simple_input(self, prompt):
        from tkinter.simpledialog import askstring
        return askstring("Input", prompt)

    def show_table(self, table):
        # Display the table of values in a new window
        table_window = tk.Toplevel(self)
        table_window.title("Table of Function")
        text_area = tk.Text(table_window, font=("Helvetica", 12))
        text_area.pack(expand=True, fill='both')
        for x_val, y_val in table:
            text_area.insert(tk.END, f"x = {x_val:.4f}  ->  f(x) = {y_val:.4f}\n")

    def plot_function(self):
        # Plot a function from an expression (in terms of x)
        expr = self.plot_entry.get()
        if expr == "":
            messagebox.showerror("Error", "Enter a function in terms of x (e.g., sin(x))")
            return
        try:
            x = np.linspace(-10, 10, 400)
            safe_dict = {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                         "log": np.log, "exp": np.exp, "sqrt": np.sqrt,
                         "pi": np.pi, "e": np.e}
            y = eval(expr, safe_dict)
            plt.figure()
            plt.plot(x, y)
            plt.title("Plot of " + expr)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
