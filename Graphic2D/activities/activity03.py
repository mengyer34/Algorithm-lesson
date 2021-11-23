import tkinter as tk;
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PNC UI GAME")
canvas = tk.Canvas(frame)


y1 = 26
y2 = 77
colors = ['red','blue','green','orange','yellow','black','purple']
for row in range(9):
    x1 = 26    
    x2 = 77
    for col in range(9):
        canvas.create_rectangle(x1, y1, x2, y2, fill=random.choice(colors), outline="")
        x1 = x2 + 12
        x2 += 62  
    y1 = y2 + 12
    y2 += 62
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()   