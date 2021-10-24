from tkinter import *
# PIL import ImageTk,Image
from tkinter import ttk

#Product=StringVar()

fenetre=Tk()
butt_search=ttk.Button(fenetre, text='search')
entry_search=ttk.Entry(fenetre, textvariable='Product ', width=40, font='calibry 15')
#my_img=ImageTk.PhotoImage(Image.open('C:/Users/Admin/Desktop/Projet Info/search1.jpg'))
#pub=Label(image=my_img,anchor=E)


entry_search.grid(row=1,column=4,columnspan=3)
butt_search.grid(row=1,column=10,sticky=E, rowspan=3)
#pub.grid(row=1,column=4,rowspan=3,columnspan=10)
