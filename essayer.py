from tkinter import *
from tkinter import ttk 


root=Tk()
root.title("Sephora")

email=[]
passsword=[]

def SignIn():
    pass

label1=ttk.Label(root, text="E-mail")
label2=ttk.Label(root, text="Password")
button=ttk.Button(root, text="sign in ",command=SignIn)
Entry1=ttk.Entry(root, textvariable="email" )
Entry2=ttk.Entry(root, textvariable="password" )


label1.grid(row=1 ,column=1 )
label2.grid(row=2 ,column=1)
button.grid(row=3 , column=1, columnspan =4 )
Entry1.grid(row=1 ,column=2 )
Entry2.grid(row=2 ,column=2 )

root.mainloop()
