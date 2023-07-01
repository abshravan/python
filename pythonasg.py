import tkinter as tk
import math

def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def append_to_expression(value):
    entry.insert(tk.END, value)
window = tk.Tk()
window.title("Scientific Calculator BY 204")
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("^", 5, 3),
    ("(", 6, 0), (")", 6, 1), ("sqrt", 6, 2), ("log", 6, 3)
]
for button in buttons:
    text, row, col = button
    tk.Button(window, text=text, command=lambda text=text: append_to_expression(text)).grid(row=row, column=col)
tk.Button(window, text="=", command=evaluate_expression).grid(row=7, column=0, columnspan=4)
window.mainloop()
