from tkinter import *
from PIL import ImageTk,Image

def affichageSite(fenetre):
    fenetre.title('Sephora')
    fenetre.geometry('{}x{}'.format(1000,900)
    fenetre.configure(background='pink')
    labelCommune = Label(fenetre, text='*SEPHORA*', bg='black', fg='white', width=65, anchor=W,font="Andalus  35")
    labelCommune.grid(row=0, column=0, columnspan=3,sticky=(W,E))


def next():
    global fenetreNext
    global root
    fenetreNext= Toplevel(root)
    root.withdraw()
    affichageSite(fenetreNext)

#Affichage de la fenetre d'accueil
root=Tk()
root.title('Sephora')
root.configure(background='black')
root.geometry('{}x{}'.format(1500,1000))
image1=ImageTk.PhotoImage(Image.open('sephoraSEA.jpg'))
labelWelcome= Label(root,image=image1)
#labelWelcome.config(fontsize='50')
#frame=Frame(root,bg='black')
labelSephora= Label(root,text='~SEPHORA~',bg='black',fg='white',font='Times 60 bold italic')
labelSignIn=Label(root,text='Sign in to benefit from many discounts and\nget our latest news',bg='black',fg='white',font='Times 15 bold italic')
labelNext=Label(root,text='or you can simply continue as a guest',fg='white',bg='black',font='Times 15 bold italic')
nextButton=Button(root,text='Next',bg='white',fg='black',font='Times 25 bold italic',command=next)
signInButton=Button(root,text='Sign in',bg='white',fg='black',font='Times 25 bold italic')#command=signIn

#frame.grid(row=1,column=2,columnspan=2,sticky=(W,E,N,S))
labelWelcome.grid(row=0,column=0,columnspan=5,sticky=(W,E))
labelSephora.grid(row=2,column=0,columnspan=2,rowspan=2)
labelSignIn.grid(row=1,column=2,sticky=(W,N,E,S))
signInButton.grid(row=2,column=2,pady=10,sticky=(E,W,N,S))
labelNext.grid(row=3,column=2,sticky=(W,N,E,S))
nextButton.grid(row=4,column=2,pady=10,sticky=(E,W,N,S))

fenetreNext= None
root.mainloop()