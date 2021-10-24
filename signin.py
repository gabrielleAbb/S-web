from tkinter import *
from PIL import ImageTk,Image


fenetre=Tk()
fenetre.title("Sephora")
fenetre.configure(background='white')
fenetre.geometry('1000x500')


username=StringVar()
password=StringVar()

def signup():
    pass

def login():
    pass

username=Label( text="\n    Username", background='white', anchor=W, font='calibry 14',)
password=Label( text="\n     Password",bg='white', anchor=W, font='calibry 14')
b1 = Button (fenetre, text='Login ', command= login ,background ='black' ,fg='white' ,width=15 , font='calibry 14' )
b2 = Button (fenetre, text='Sign Up ', command=signup ,background ='black' ,fg='white' ,width=15 , font='calibry 14' )

username_Entry=Entry (fenetre, textvariable="username", width=25,font='calibry 15'  )
password_Entry= Entry ( fenetre,textvariable="password", width=25,font='calibry 15', show='*')


username.grid(row=1 ,column=2, sticky=(W) )
password.grid(row=3 ,column=2,  sticky=(W) )

b1.grid(row=5, column=2 ,columnspan=2  )

b2.grid(row= 6, column=2, columnspan=2)
username_Entry.grid(row=2,column=2, sticky=(W), columnspan=2 ,pady=20)
password_Entry.grid(row=4,column=2, sticky=(W), columnspan=2, pady=20)

my_img=ImageTk.PhotoImage(Image.open('C:/Users/Admin/Desktop/Projet Info/signInPageS.png'))
pub=Label(image=my_img,anchor=E)
pub.grid(row=1,column=4,rowspan=16,columnspan=5,sticky=(E) ,padx=200)


fenetre.mainloop()
