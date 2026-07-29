import tkinter as tk
import random

names = ["Birat", "Manish", "Ishan", "Mandip", "Brihaspati"]

window = tk.Tk()
window.title("Name Picker")
window.geometry("300x220")

winner = random.choice(names)

main_box = tk.Frame(window, bd=2, relief="solid", width=220, height=140)
main_box.pack(pady=20)
main_box.pack_propagate(False)

title = tk.Label(main_box, text="Winner", bd=2, relief="solid",
                 font=("Arial", 12), width=10)
title.pack(pady=10)

name = tk.Label(main_box, text=winner, font=("Arial", 18))
name.pack(pady=20)

window.mainloop()