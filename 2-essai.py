from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('sephora')
my_img=ImageTk.PhotoImage(Image.open('C:/Users/Admin/Desktop/Projet Info/Sephora.png'))
image1=ImageTk.PhotoImage(Image.open('C:/Users/Admin/Desktop/Projet Info/sephora2.png'))
my_label=Label(image=my_img)
label1=Label(image=image1)
my_label.grid(row=0,column=0,sticky=(W))
label1.grid(row=1,column=0)


root.mainloop()