import tkinter as tk;
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PNC UI GAME")
canvas = tk.Canvas(frame)


canvas.create_rectangle(100, 100, 500, 500, fill="red")
canvas.create_rectangle(150, 150, 450, 450, fill="blue")
canvas.create_rectangle(190, 190, 410, 410, fill="green")
canvas.create_rectangle(230, 230, 370, 370, fill="orange")
canvas.create_rectangle(270, 270, 330, 330, fill="green")

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()