import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = display.get().replace("^", "**")
            result = str(eval(expression))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Division by zero")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid expression")
    elif text == "C":
        display.delete(0, tk.END)
    elif text in {"sin", "cos", "tan"}:
        try:
            current_value = float(display.get())
            if text == "sin":
                result = math.sin(math.radians(current_value))
            elif text == "cos":
                result = math.cos(math.radians(current_value))
            elif text == "tan":
                result = math.tan(math.radians(current_value))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
    else:
        display.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="black")  # Change background color

# Create a text entry widget for the display
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

# Define the button labels
button_labels = [
    "7", "8", "9", "/", "C", "^0.5",
    "4", "5", "6", "*", "^",  "%",
    "1", "2", "3", "-", "^3", "^2",
    "0", ".", "=", "+", "sin", "cos", 
    "tan", "log", "deg", "2nd", "  "  # Add two spaces for width 
]
# Create and place the calculator buttons
row = 1
col = 0
for label in button_labels:
    if label == "  ":  # Empty label for spanning two columns
        col_span = 2 
        button = tk.Label(root, text=label, font=("Arial", 16), width=9, height=2, bd=2)  # Adjust width and height as needed
    else:
        col_span = 1
        button = tk.Button(root, text=label, font=("Arial", 16), width=4, height=2, bd=2)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="ew")
    button.bind("<Button-1>", on_click)
    col += col_span
    if col > 5:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
