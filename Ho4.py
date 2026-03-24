import tkinter as tk
from tkinter import messagebox

accounts = {}

window = tk.Tk()
window.title("Navaja HO Exam")
window.geometry("350x250")
window.configure(bg="white")

# ---------- REGISTER WINDOW ----------
def open_register():
    reg_win = tk.Toplevel()
    reg_win.title("Register")
    reg_win.geometry("300x200")
    reg_win.configure(bg="white")

    tk.Label(reg_win, text="Registration From", bg="white",
             fg="black", font=("Arial", 14, )).pack(pady=10)

    tk.Label(reg_win, text="Username", bg="white").pack()
    user = tk.Entry(reg_win)
    user.pack()

    tk.Label(reg_win, text="Password", bg="white").pack()
    pw = tk.Entry(reg_win, show="*")
    pw.pack()

    show = tk.IntVar()
    def toggle():
        pw.config(show="" if show.get() else "*")

    tk.Checkbutton(reg_win, text="See Password",
                   variable=show, command=toggle,
                   bg="white").pack()

    def register():
        if user.get() in accounts:
            messagebox.showerror("Error", "User already exists!")
        else:
            accounts[user.get()] = pw.get()
            messagebox.showinfo("Success", "Registered Successfully!")
            reg_win.destroy()

    tk.Button(reg_win, text="Register", command=register).pack(pady=10)


# ---------- LOGIN WINDOW ----------
def open_login():
    log_win = tk.Toplevel()
    log_win.title("Log In")
    log_win.geometry("300x200")
    log_win.configure(bg="green")

    tk.Label(log_win, text="Log In", bg="white",
             fg="black", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(log_win, text="Username", bg="white").pack()
    user = tk.Entry(log_win)
    user.pack()

    tk.Label(log_win, text="Password", bg="white").pack()
    pw = tk.Entry(log_win, show="*")
    pw.pack()

    show = tk.IntVar()
    def toggle():
        pw.config(show="" if show.get() else "*")

    tk.Checkbutton(log_win, text="See Password",
                   variable=show, command=toggle,
                   bg="white").pack()

    def login():
        if user.get() in accounts and accounts[user.get()] == pw.get():
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid username/password!")

    tk.Button(log_win, text="Log In", command=login).pack(pady=10)


# ---------- MAIN WINDOW ----------
tk.Label(window, text="Welcome!", font=("Arial", 16, "bold"),
         bg="white").pack(pady=20)

tk.Button(window, text="Register",
          bg="blue", fg="white",
          width=50, height=3,
          command=open_register).pack(pady=10)

tk.Button(window, text="Log In",
          bg="green", fg="black",
          width=50, height=3,
          command=open_login).pack(pady=10)
window.mainloop()