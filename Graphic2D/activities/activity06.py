import tkinter as tk;
import random
root = tk.Tk()
root.geometry("660x660")
frame = tk.Frame()
frame.master.title("PNC UI GAME")
canvas = tk.Canvas(frame)


y1 = 26
y2 = 77
y_1 = 89
y_2 = 203
colors = ['red','blue','green','orange','yellow','black','purple']
for row in range(10):
    x1 = 26    
    x2 = 77
    x_1 = 89 
    x_2 = 203
    for col in range(10):
        if  col == 0 or row == 0 or col == 9 or row == 9:
            canvas.create_rectangle(x1, y1, x2, y2, fill=random.choice(colors), outline="")
        elif (row %2 == 1 and row !=9) and (col %2 == 1 and col !=9): 
            canvas.create_rectangle(x_1, y_1, x_2, y_2, fill=random.choice(colors), outline="") 
            x_1 = x_2 + 12
            x_2 += 123
            y_1 = x_2 + 12   
            y_2 += 203
        x1 = x2 + 12
        x2 += 62
    y1 = y2 + 12
    y2 += 62

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()   

# import tkinter as tk;
# import random
# root = tk.Tk()
# root.geometry("660x660")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)


# x1 = 0
# y1 = 0
# colors = ['red','blue','green','orange','yellow','black','purple']
# for row in range(10):
#     for col in range(10):
#         if  col == 0 or row == 0 or col == -1 or row == -1:
#             canvas.create_rectangle(25+x1, 25+y1, 55+x1, 55+y1, fill=random.choice(colors), outline="")
#             x1 += 50
#         # elif (row %2 == 1 and row !=9) and (col %2 == 1 and col !=9): 
#         #     canvas.create_rectangle(25+x1, 25+y1, 55+x1, 55+y1, fill=random.choice(colors), outline="") 
  
#     y1 += 50
#     x1 = 0
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# root.mainloop()   