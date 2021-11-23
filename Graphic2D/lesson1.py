from random import shuffle
students = ['ab', 'bs', 'cs', 'ds']
shuffle(students)
print(students)

# random.randrange(start, stop, step)

# # Ex : 
# import random
# for i in range(1,4):
#     print("Number", str(i), ":", str(random.randrange(0, 100)))

# Ex 2:
# import random
# studentsList = ["SARETH","SEAVY","RATHTEKA","SREYHON","VANTHORN","SOK","TOUN","SREYTOUCH","CHAINY","SOM","SIMENG","NHORK","SREYNOT","THIN","SEANGHAY","LYHUOY","SOPHANNA","NIMOUT","VOULEAK","CHET","SINY","SOTHEAN","SOPHORN","SREYHIEB","MENGHOUR","NISAI","CHANTHEA","PHEARAK","SOMOUN","SREYNICH","SAOLEE","RIN","ON","SOPHANNA","CHANTHY","MOLIKA","BUNSAL","SOKTHANG","DYNA","SARA","VOUCHLY","SOTHOUN","LYDEN","MONYRA","VUN","LANH","PHALLY","SREYPICH","SENGHIM","DAVY","CHUM","LYHEANG","KOEMSAK","VICHEKA","LAMYAI","CHANTHOU","KUNTHY","SOPHEA","VANTHEAV","SOPHEAK","NARATH","SREYNGIT","MENGHEANG","VUTHY","CHANRY","CHANNARY","LYHOR","THALY","HOUTCHHAY","SOMPHORS","SINET","SREY AEM","THON","PROS"]
# name = input("What is your name? : ")
# print(name, "secret lover is", random.choice(studentsList))

# # Tk library 
# import tkinter as tk;
# # Create an empty window
# root = tk.Tk()
# # Set TK window size to width 600px and height 200px
# root.geometry("600x200")
# # Create a frame in the window (frame is a container, like "div" in HTML)
# frame = tk.Frame()
# # Set the title of the frame
# frame.master.title("Mengyi")

# # Here you can start to draw
# canvas = tk.Canvas(frame)
# # x1, y1, x2, y2  
# canvas.create_rectangle(10,10,50,50, fill="#8EE5EE")
# canvas.create_oval(500, 500, 550, 550, fill="#8EE5EE")
# canvas.create_text(200, 200, text="Just Do It", font=("purisa", 26))

# # pack means "draw what I put inside"
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# # Display all
# root.mainloop()
