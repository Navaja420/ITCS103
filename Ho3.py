import tkinter as tk



window = tk.Tk()
window.title("Simple Calculator")

# window.geometry("500x500")
window.resizable(True, True)
window.configure(bg="lightblue")
window.title("Simple Calculator")

frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
frame.grid(row=1, column=2, padx=5, pady=5)

def add():
    a = float(Entry1.get())
    b = float(Entry2.get())
    result.config(text=f"The sum of {a} + {b} = {a + b}")

def substract():
    a = float(Entry1.get())
    b = float(Entry2.get())
    result.config(text=f"The difference of {a} - {b} = {a - b}")

def multiply():
    a = float(Entry1.get())
    b = float(Entry2.get())
    result.config(text=f"The product of {a} * {b} = {a * b}")

def divide():
    a = float(Entry1.get())
    b = float(Entry2.get())
    result.config(text=f"The quotient of {a} / {b} = {a / b}")

result = tk.Label(window, text="Result will be shown here", bg="white", font=("Arial", 12))
result.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label1 = tk.Label(window, text="Enter First Number:")
label1.grid(row=1, column=0, padx=10, pady=5)

Entry1 = tk.Entry(window)
Entry1.grid(row=1, column=1, padx=10, pady=5) 

Label2 = tk.Label(window, text="Enter Second Number:")
Label2.grid(row=2, column=0, padx=10, pady=5)

Entry2 = tk.Entry(window)
Entry2.grid(row=2, column=1, padx=10, pady=5)

btn1 = tk.Button(window, text="Add", command=add)
btn1.grid(row=3, column=0, padx=10, pady=5)

btn2 = tk.Button(window, text="Substract", command=substract)
btn2.grid(row=3, column=1, padx=10, pady=5)

btn3 = tk.Button(window, text="Multiply", command=multiply)
btn3.grid(row=4, column=0, padx=10, pady=5)

btn4 = tk.Button(window, text="Divide", command=divide)
btn4.grid(row=4 , column=1, padx=10, pady=5)

window.mainloop()



    