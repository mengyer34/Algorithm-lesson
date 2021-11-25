import tkinter as tk;
import random
from tkinter.constants import RADIOBUTTON
root = tk.Tk()
root.geometry("340x340")
frame = tk.Frame()
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)

y1 = 50
y2 = 100
for i in range(1, 6):
    x1 = 50   
    x2 = 100
    for j in range(1, 6):
        if i == j:
            canvas.create_oval(x1,y1,x2,y2,fill="red")
        else:
            canvas.create_oval(x1,y1,x2,y2,fill="blue")
        x1 = x2  
        x2 += 50
    y1 = y2 
    y2 += 50

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()