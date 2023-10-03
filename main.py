# Simple Calculator program with tkinter


# Import tkinter
import tkinter as tk

# global variable
equation = ""


# Adds button values to the equation
def append_calc(operation, result):
    global equation
    equation += str(operation)
    result.delete(1.0, "end")
    result.insert(1.0, equation)
    pass


# Evaluates the equation
def evaluate(result):
    global equation
    try:
        equation = str(eval(equation))
        result.delete(1.0, "end")
        result.insert(1.0, equation)
    except:
        result.delete(1.0, "end")
        result.insert(1.0, "ERROR")


# Clears the equation line
def clear(result):
    global equation
    equation = ""
    result.delete(1.0, "end")


def main():
    # Create ui window
    root = tk.Tk()
    root.geometry("325x300")
    root.title("Simple Calculator")

    # Create buttons for numbers
    result = tk.Text(root, height=2, width=16, font=("Ariel", 24))
    result.grid(columnspan=5)
    btn_0 = tk.Button(root, text="0", command=lambda: append_calc(0, result), width=5)
    btn_0.grid(row=5, column=1, columnspan=1)
    btn_1 = tk.Button(root, text="1", command=lambda: append_calc(1, result), width=5)
    btn_1.grid(row=4, column=1)
    btn_2 = tk.Button(root, text="2", command=lambda: append_calc(2, result), width=5)
    btn_2.grid(row=4, column=2)
    btn_3 = tk.Button(root, text="3", command=lambda: append_calc(3, result), width=5)
    btn_3.grid(row=4, column=3)
    btn_4 = tk.Button(root, text="4", command=lambda: append_calc(4, result), width=5)
    btn_4.grid(row=3, column=1)
    btn_5 = tk.Button(root, text="5", command=lambda: append_calc(5, result), width=5)
    btn_5.grid(row=3, column=2)
    btn_6 = tk.Button(root, text="6", command=lambda: append_calc(6, result), width=5)
    btn_6.grid(row=3, column=3)
    btn_7 = tk.Button(root, text="7", command=lambda: append_calc(7, result), width=5)
    btn_7.grid(row=2, column=1)
    btn_8 = tk.Button(root, text="8", command=lambda: append_calc(8, result), width=5)
    btn_8.grid(row=2, column=2)
    btn_9 = tk.Button(root, text="9", command=lambda: append_calc(9, result), width=5)
    btn_9.grid(row=2, column=3)

    # Create buttons for operators
    btn_mult = tk.Button(root, text="x", command=lambda: append_calc("*", result), width=5)
    btn_mult.grid(row=2, column=4)
    btn_div = tk.Button(root, text="/", command=lambda: append_calc("/", result), width=5)
    btn_div.grid(row=3, column=4)
    btn_sub = tk.Button(root, text="-", command=lambda: append_calc("-", result), width=5)
    btn_sub.grid(row=4, column=4)
    btn_add = tk.Button(root, text="+", command=lambda: append_calc("+", result), width=5)
    btn_add.grid(row=5, column=4)

    # Create button to clear line
    btn_clear = tk.Button(root, text="C", command=lambda : clear(result), width=5)
    btn_clear.grid(row=5, column=2)

    # Create "=" button to evaluate equation
    btn_eq = tk.Button(root, text="=", command=lambda: evaluate(result), width=5)
    btn_eq.grid(row=5, column=3)
    root.mainloop()


if __name__ == "__main__":
    main()