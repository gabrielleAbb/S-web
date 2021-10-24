from tkinter import *
from PIL import ImageTk,Image
fenetre=Tk()
fenetre.geometry('1000x500')
fenetre.configure(background='white')
fenetre.title('sign up')
firstname=Label(text='\n    First name: ',bg='white',anchor=W,font='calibry 14')
first_name=Entry(width=25,font='calibry 15')

lastname=Label(text='    Last name:',bg='white',font='calibry 14')
last_name=Entry(width=25,font='calibry 15')

email=Label(text='    Email adress:',bg='white',font='calibry 14')
email_adress=Entry(width=25,font='calibry 15')

password=Label(text='    Password:',bg='white',font='calibry 14')

password_entry=Entry(width=25,font='calibry 15')

passconfirmation=Label(text='    Confirm your password:',bg='white',font='calibry 14')
pass_confirmation=Entry(width=25,font='calibry 15')
back=Button(text='Back',background='black',fg='white',width=15,font='calibry 14')
next=Button(text='Next',background='black',fg='white',width=15,font='calibry 14')
my_img=ImageTk.PhotoImage(Image.open('C:/Users/Admin/Desktop/Projet Info/signUpPageS.png'))
pub=Label(image=my_img,anchor=E)
firstname.grid(row=1,column=2,sticky=W)
first_name.grid(row=2,column=2,sticky=(W),columnspan=2)
lastname.grid(row=3,column=2,sticky=W)
last_name.grid(row=4,column=2,sticky=W,columnspan=2)
email.grid(row=5,column=2,sticky=W)
email_adress.grid(row=6,column=2,sticky=W,columnspan=2)
password.grid(row=7,column=2,sticky=W)
password_entry.grid(row=8,column=2,sticky =W,columnspan=2)
passconfirmation.grid(row=9,column=2,sticky=W)
pass_confirmation.grid(row=10,column=2,sticky=W,columnspan=2)
back.grid(row=11,column=2,sticky=W,pady=5,padx=30)
next.grid(row=11,column=3,sticky=W)
pub.grid(row=1,column=4,rowspan=11,columnspan=2,sticky=E,padx=100)
fenetre.mainloop()

