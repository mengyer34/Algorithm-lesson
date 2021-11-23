import tkinter as tk;
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)
# Eye 
canvas.create_oval(100, 50, 200, 100, fill="#FFFFFF")
canvas.create_oval(125,50,175,100, fill="#0000FF")
canvas.create_oval(400, 50, 500, 100, fill="#FFFFFF")
canvas.create_oval(425,50,475,100, fill="#0000FF")
# Nose 
canvas.create_oval(275,250,325,300, fill="#FF0000")
# Mouse 
canvas.create_rectangle(100, 450, 500, 480, fill="#FF0000", outline="")
canvas.create_rectangle(100, 390, 130, 450, fill="#FF0000", outline="")
canvas.create_rectangle(470, 420, 500, 450, fill="#FF0000", outline="")

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()