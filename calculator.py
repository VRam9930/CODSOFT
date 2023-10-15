import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()
        
        if operator == "+":
            result.set(num1 + num2)
        elif operator == "-":
            result.set(num1 - num2)
        elif operator == "*":
            result.set(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Unique Calculator")

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

entry_num1.pack()
entry_num2.pack()

operator_var = tk.StringVar()
operator_var.set("+")   

operators = ["+", "-", "*", "/"]
operator_menu = tk.OptionMenu(root, operator_var, *operators)
operator_menu.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

root.mainloop()
