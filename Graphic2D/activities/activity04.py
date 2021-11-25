import tkinter as tk;
import random
from tkinter.constants import RADIOBUTTON
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)

numbers = random.randint(1,10)
for i in range(1, 11):
    canvas.create_oval(50 * i, 50, 50 + (i*50), 100, fill="blue")
    if numbers == i:
        canvas.create_oval(50 * i, 50, 50 + (i*50), 100, fill="red")


canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()