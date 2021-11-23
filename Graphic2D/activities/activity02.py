import tkinter as tk;
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PNC UI GAME")
canvas = tk.Canvas(frame)


canvas.create_oval(100, 100, 500, 500, fill="red")
canvas.create_oval(150, 150, 450, 450, fill="blue")
canvas.create_oval(190, 190, 410, 410, fill="green")
canvas.create_oval(230, 230, 370, 370, fill="orange")
canvas.create_oval(270, 270, 330, 330, fill="green")

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()