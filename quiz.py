import tkinter as tk

def calculate_age():
    try:
       year = int(entry_birth.get())
       age = 2026 - year
       label_age.config(text=f"You are {age} years old.")
    except:
        label_age.config(text="Invalid year")

window = tk.Tk()
window.title("Profile Builder")
window.geometry("500x300")
window.configure(bg="lightblue")

title = tk.Label(window, text="Profile Builder", font=("arial", 16, "bold"), bg="lightblue")
title.pack(pady=10)

frame = tk.Frame(window, bg="lightgreen")
frame.pack(pady=10)

tk.Label(frame, text="First Name", bg="lightgreen").grid(row=1, column=0)
entry_frist = tk.Entry(frame)
entry_frist.grid(row=0, column=0, padx=10)

tk.Label(frame, text="Middle Name", bg="lightgreen").grid(row=1, column=1)
entry_middle = tk.Entry(frame)
entry_middle.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Last Name", bg="lightgreen").grid(row=1, column=2)
entry_last = tk.Entry(frame)
entry_last.grid(row=0, column=2, padx=10)

tk.Label(frame, text="Birth Year", bg="lightgreen").grid(row=3, column=0, pady=10)
entry_birth = tk.Entry(frame)
entry_birth.grid(row=2, column=0)

tk.Label(frame, text="Gender", bg="lightgreen").grid(row=4, column=0)

gender_var = tk.StringVar(value="male")

tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="lightgreen").grid(row=4, column=1)
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="lightgreen").grid(row=4, column=2)

label_age = tk.Label(window, text="You are  years old", bg="lightgreen", font=("arial", 12))
label_age.pack(pady=10)

btn_submit = tk.Button(window, text="Submit", bg="lightgreen", command=calculate_age)
btn_submit.pack()


window.mainloop()