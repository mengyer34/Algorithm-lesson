import tkinter as tk;
import random
root = tk.Tk()
root.geometry("660x660")
frame = tk.Frame()
frame.master.title("PNC UI GAME")
canvas = tk.Canvas(frame)


y1 = 26
y2 = 77
colors = ['green', 'purple', 'orange', 'red', 'blue', 'pink', 'yellow']
for row in range(10):
    x1 = 26    
    x2 = 77
    x_1 = 89 
    x_2 = 203
    for col in range(10):
        if  col == 0 or row == 0 or col == 9 or row == 9:
            canvas.create_rectangle(x1, y1, x2, y2, fill=random.choice(colors), outline="")
        elif (row %2 == 1 and row !=9) and (col %2 == 1 and col !=9): 
            canvas.create_rectangle(x_1, y1, x_2, y2+61, fill=random.choice(colors), outline="") 
            x_1 = x_2 + 12
            x_2 += 123
        x1 = x2 + 12
        x2 += 62
    y1 = y2 + 12
    y2 += 62

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()   

