import tkinter as tk
window = tk.Tk()

window.title("Navaja_HO2")
window.geometry("600x600")
window.resizable(True, True)
window.configure(bg="pink")

label = tk.Label(window, text="STUDENT PROFILE", font=("Arial", 24, "bold"), bg="pink",fg="black")
label.pack(pady=20)

label = tk.Label(window, text="Full Name: John Lloyd Navaja", font=("Arial", 18), bg="white",fg="black")
label.pack(pady=20, padx=20,anchor="w")
label = tk.Label(window, text="Age: 19Years old", font=("Arial", 18), bg="white",fg="black", justify= "left")
label.pack(pady=20, padx=20,anchor="w")
label = tk.Label(window, text="Course: BSIT_1B", font=("Arial", 18), bg="white",fg="black", justify= "left")
label.pack(pady=20, padx=20, anchor="w")
label = tk.Label(window, text="Birthday: March 14, 2006", font=("Arial", 18), bg="white",fg="black", justify= "left")
label.pack(pady=20,padx=20, anchor="w")
label = tk.Label(window, text="Motto:", font=("Arial", 18), bg="white",fg="black", justify= "left")
label.pack(pady=10, padx=20, anchor="w")
label = tk.Label(window, text=f"         No rush, but never stop.", font=("Arial", 18), bg="white",fg="red", justify= "left")
label.pack(pady=20, padx=20, anchor="w")


# label = tk.Label(window, text=f"""
#                  Twinkle, twinkle, little star, 
#                  how I wonder what you are. 
#                  Up above the world so high,
#                  like a diamond in the sky. 
#                  Twinkle, twinkle, little star,
#                  how I wonder what you are.
#                  When the blazing sun is set, 
#                  and the grass with dew is wet.
#                  Then you show your little
#                  light, twinkle, twinkle all the night. 
#                  Twinkle, twinkle little star, 
#                  how I wonder what you are.
# """, font=("Arial", 24), bg="gray",fg="red", justify= "left")
# label.pack(anchor="center")
window.mainloop()