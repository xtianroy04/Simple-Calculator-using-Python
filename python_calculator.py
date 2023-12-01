import tkinter as tk
from tkinter import messagebox

def multiply(num1, num2):
    return num1 * num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

def perform_operation(choice, num1, num2):
    if choice == 1:
        return multiply(num1, num2)
    elif choice == 2:
        return add(num1, num2)
    elif choice == 3:
        return subtract(num1, num2)
    elif choice == 4:
        return divide(num1, num2)

def on_submit():
    try:
        choice = int(choice_var.get())
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers and choice.")
        return

    if choice not in [1, 2, 3, 4]:
        messagebox.showerror("Error", "Invalid choice. Please enter a valid choice (1/2/3/4).")
        return

    result = perform_operation(choice, num1, num2)
    result_label.config(text=f"Result: {result}")
    messagebox.showinfo("Result", f"The result is: {result}")

def stop_program():
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")  # Set the size of the GUI

# Set font size
font_size = ("Arial", 12)

# Widgets
choice_var = tk.StringVar()
tk.Label(root, text="Select operation:", font=font_size).pack()

operations = [("Multiply", 1), ("Add", 2), ("Subtract", 3), ("Divide", 4)]
for text, value in operations:
    tk.Radiobutton(root, text=text, variable=choice_var, value=value, font=font_size).pack()

entry_num1 = tk.Entry(root, width=10, font=font_size)
entry_num1.pack()
entry_num2 = tk.Entry(root, width=10, font=font_size)
entry_num2.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit, font=font_size)
submit_button.pack()

result_label = tk.Label(root, text="Result: ", font=font_size)
result_label.pack()

root.mainloop()
