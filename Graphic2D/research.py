# import tkinter as tk 
# root = tk.Tk()

# message = tk.Label(root, text="Hello, Sarath")
# message.pack()

# root.mainloop()

# # Button 
# import tkinter as tk
# from tkinter import ttk

# # root window
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Button Demo')

# # exit button
# exit_button = ttk.Button(
#     root,
#     text='Exit',
#     command=lambda: root.quit()
# )

# exit_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )

# root.mainloop()

# button img 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Image Button Demo')


# download button
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = tk.PhotoImage(file='./img/download.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


root.mainloop()