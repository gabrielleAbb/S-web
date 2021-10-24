from tkinter import *
from PIL import ImageTk,Image
import pickle
from tkinter import messagebox

def affichageSite():
    global fenetreSite
    fenetreSite.title('Sephora')
    fenetreSite.geometry('1000x500')
    fenetreSite.configure(background='white')
    #labelHi = Label(fenetre, text='hi')
    #imageHead=ImageTk.PhotoImage(Image.open('sephoraSS.jpg'))
    #labelHead=Label(fenetre,image=imageHead,anchor=CENTER,height=100)
    #labelCommune = Label(fenetre, text='*SEPHORA*', bg='black', fg='white', width=65, anchor=W,font="Andalus  35")
    #labelHead.grid(row=0, column=0, columnspan=3,sticky=(W,E))
    #labelHi.grid(row=1, column=1)
    fenetreSite.mainloop()

def Next(fenetreOuvrir,fenetreFerme):
    fenetreFerme.withdraw()
    fenetreOuvrir.deiconify()
    fenetreOuvrir.mainloop()


def Back(fenetreOuvrir,fenetreFerme):
    fenetreFerme.withdraw()
    fenetreOuvrir.deiconify()
    fenetreOuvrir.geometry('1000x500+0+0')

def backSU():
    fenetreSU.withdraw()
    fenetreSI.deiconify()

def backSI():
    fenetreSI.withdraw()
    root.deiconify()


def nextWelcome():
    global fenetreSite
    global root
    root.withdraw()
    affichageSite()

def ajout():
    if (firstname.get()=="" or lastname.get()=='' or password.get()=='' or username.get==''):
        messagebox.showerror("ERROR","You have to fill all the informations above!!")
    elif(password.get()!=passconfirmation.get()):
        messagebox.showerror("ERROR","Password and Password Confirmation should match!!")
    elif(len(password.get())<8):
        messagebox.showerror("ERROR","Your password should be formed of at least from 8 characters.")
    elif('/' in username.get() or '/' in firstname.get() or '/' in lastname.get() or  '/' in password.get()):
    #pour avoir une condition sur laquelle on fait split pour ne pas avoir out of input pour load
        messagebox.showerror("ERROR","Your username, first name, last name or password should not include the character '/'")

    else:
        user=[username.get(),firstname.get(),lastname.get(),password.get(),'/']
        used=False
        with open('usernames.txt', 'r')as f:
            a = f.read()
            liste = a.split('/')
        with open('usernames.txt', 'rb')as g:
            i = 0
            while(i < len(liste) - 1 and used==False):
                l = pickle.load(g)
                if l[0]==user[0]:
                    used=True
                i = i + 1
        if used==False:
             with open("Usernames.txt", "ab") as f:
                pickle.dump(user, f)
             Next(fenetreSI,fenetreSU)
        elif used==True:
            messagebox.showerror("ERROR","username already in use choose a different one.")


def signUp():
    global fenetreSU
    fenetreSI.withdraw()
    fenetreSU = Toplevel(fenetreSI)
    fenetreSU.geometry('1000x500+0+0')
    fenetreSU.configure(background='white')
    fenetreSU.title('sign up')
    fenetreSU.resizable(width=False,height=False)
    firstnameLabel = Label(fenetreSU,text='\n    First name: ', bg='white', anchor=W, font='calibry 14')
    firstnameEntry = Entry(fenetreSU,textvariable=firstname,width=25, font='calibry 15')
    lastnameLabel = Label(fenetreSU,text='    Last name:', bg='white', font='calibry 14')
    lastnameEntry = Entry(fenetreSU,textvariable=lastname,width=25, font='calibry 15')
    usernameLabel = Label(fenetreSU,text='    Username:', bg='white', font='calibry 14')
    usernameEntry = Entry(fenetreSU,textvariable=username,width=25, font='calibry 15')
    passwordLabel = Label(fenetreSU,text='    Password:', bg='white', font='calibry 14')
    passwordEntry = Entry(fenetreSU,textvariable=password,width=25, font='calibry 15',show='*')
    passconfirmationLabel = Label(fenetreSU,text='    Confirm your password:', bg='white', font='calibry 14')
    passconfirmationEntry = Entry(fenetreSU,textvariable=passconfirmation,width=25, font='calibry 15',show='*')
    backButton = Button(fenetreSU,text='Back', background='black', fg='white', width=15, font='calibry 14',command=backSU)
    nextButton = Button(fenetreSU,text='Next', background='black', fg='white', width=15, font='calibry 14',command=ajout)
    myImg = ImageTk.PhotoImage(Image.open('signUpPageS.png'))
    pub = Label(fenetreSU,image=myImg, anchor=E)
    firstnameLabel.grid(row=1, column=2, sticky=W)
    firstnameEntry.grid(row=2, column=2, sticky=(W), columnspan=2)
    lastnameLabel.grid(row=3, column=2, sticky=W)
    lastnameEntry.grid(row=4, column=2, sticky=W, columnspan=2)
    usernameLabel.grid(row=5, column=2, sticky=W)
    usernameEntry.grid(row=6, column=2, sticky=W, columnspan=2)
    passwordLabel.grid(row=7, column=2, sticky=W)
    passwordEntry.grid(row=8, column=2, sticky=W, columnspan=2)
    passconfirmationLabel.grid(row=9, column=2, sticky=W)
    passconfirmationEntry.grid(row=10, column=2, sticky=W, columnspan=2)
    backButton.grid(row=11, column=2, sticky=W, pady=5, padx=30)
    nextButton.grid(row=11, column=3, sticky=W)
    pub.grid(row=1, column=4, rowspan=11, columnspan=2, sticky=E, padx=100)
    fenetreSU.mainloop()

def signIn():
    global fenetreSI
    root.withdraw()
    fenetreSI = Toplevel(root)
    fenetreSI.title("Sephora")
    fenetreSI.configure(background='white')
    fenetreSI.geometry('1000x500+0+0')
    fenetreSI.resizable(width=False,height=False)
    usernameLabelSI = Label(fenetreSI, text="    Username:", bg='white', fg='black', anchor=W, font='calibry 14 bold', )
    passwordLabelSI = Label(fenetreSI, text="     Password:", bg='white', fg='black', anchor=W, font='calibry 14 bold')
    logInButton = Button(fenetreSI, text='Sign In ', command=login, bg='black', fg='white', width=15, font='calibry 14')
    signUpButton = Button(fenetreSI, text='Sign Up ', command=signUp, bg='black', fg='white', width=15, font='calibry 14')
    backButtonSI = Button(fenetreSI, text='Back',command=backSI, bg='black', fg='white', font='calibry14', width=15)
    username_Entry = Entry(fenetreSI, textvariable=usernameSI, width=25, font='calibry 15')
    password_Entry = Entry(fenetreSI, textvariable=passwordSI, width=25, font='calibry 15', show='*')
    imagePub = ImageTk.PhotoImage(Image.open('signInPageS.png'))
    labelPub = Label(fenetreSI,image=imagePub, anchor=E)

    usernameLabelSI.grid(row=1, column=2, sticky=(W, N, S))
    passwordLabelSI.grid(row=3, column=2, sticky=(W, N, S))
    logInButton.grid(row=5, column=2, columnspan=2, sticky=(S, W, E))
    backButtonSI.grid(row=7, column=2, columnspan=2, sticky=(N, W, E))
    signUpButton.grid(row=6, column=2, sticky=(W, E), columnspan=2)
    username_Entry.grid(row=2, column=2, sticky=(W, N), columnspan=2)
    password_Entry.grid(row=4, column=2, sticky=(W, N), columnspan=2)
    labelPub.grid(row=1, column=4, rowspan=7, columnspan=5, sticky=(E), padx=210)
    fenetreSI.mainloop()

def login():
    trouve=False
    passwordEntered=True
    with open('usernames.txt', 'r')as f:
        a = f.read()
        liste = a.split('/')
    with open('usernames.txt', 'rb')as g:
        i = 0
        while (i < len(liste) - 1 and trouve==False):
            l = pickle.load(g)
            #l est de la forme [username,firstname,lastname,password,'/']
            if l[0] == usernameSI.get():
                trouve=True
                if l[3]!= passwordSI.get():
                    passwordEntered=False
                    messagebox.showerror("ERROR","Wrong password!")
                else:
                    break
            i=i+1
        if trouve==False:
            messagebox.showerror("ERROR","Wrong username!")
        elif(trouve==True and passwordEntered==True):
            Next(fenetreSite,fenetreSI)


def affichagePage(foldername, fenetre):
    global researchdProduct

    fenetre.configure(background='white')
    path = os.getcwd() + '\\' + foldername + '\\size200'
    images = os.listdir(path)
    imagesCombo = list(images)
    i = 0
    while i <= len(imagesCombo):
        imagesCombo[i] = imagesCombo[i].split('png')[0]
        i = i + 1
    searchBox = ttk.Combobox(fenetre, textvariable=researchdProduct, width=20, values = imagesCombo, state = readonly, font = 'calibry 13 bold')
    searchBox.bind('<<ComboboxSelected>> ', searchProduct)
    labelProduct = Label(fenetre, text='Product', background='white', foreground='black', font='Times 20 bold italic')
    backButton1 = Button(fenetre, text='<<', background='white', foreground='black', font='calibry 13 bold')
    nextButton1 = Button(fenetre, text='>>', background='white', foreground='black', font='calibry 13 bold')

    labelProduct.grid(row=0, column=0,columnspan=2,sticky=(N,S,W))
    backButton1.grid(row=0, column=1,sticky=(N,S))
    searchBox.grid(row=0, column=0,columnspan=2,sticky=(N,S,E,W))
    nextButton1.grid(row=0, column=4,sticky=(N,S,W))

    try:
        Image1=ImageTk.PhotoImage(Image.open(path+'\\'+ images[0]))
        label1=Label(fenetre, image=Image1)
        nom1_1=images[0],split('.png')
        nom1=nom1_1[0]
        labelNom1= Label(fenetre, text=nom1, font= 'calibry 13 bold', background='white')
        ButtonMore1 = Button(fenetre, text='>>', background='black',foreground='white')
        label1.grid(row=1, column=9)
        ButtonMore1.grid(row=1,column=1, sticky=(S))
        labelNom1.grid(row=2, column=0)

        Image2 = ImageTk.PhotoImage(Image.open(path + '\\' + images[1]))
        label2 = Label(fenetre, image=Image2)
        nom1_2 = images[0], split('.png')
        nom2 = nom1_2[0]
        labelNom2 = Label(fenetre, text=nom2, font='calibry 13 bold', background='white')
        ButtonMore2 = Button(fenetre, text='>>', background='black', foreground='white')
        label2.grid(row=1, column=2)
        ButtonMore2.grid(row=1, column=3, sticky=(S))
        labelNom2.grid(row=2, column=2)

        Image3 = ImageTk.PhotoImage(Image.open(path + '\\' + images[2]))
        label3 = Label(fenetre, image=Image3)
        nom1_3 = images[0], split('.png')
        nom3 = nom1_3[0]
        labelNom3 = Label(fenetre, text=nom3, font='calibry 13 bold', background='white')
        ButtonMore3 = Button(fenetre, text='>>', background='black', foreground='white')
        label3.grid(row=1, column=4)
        ButtonMore3.grid(row=1, column=5, sticky=(S))
        labelNom3.grid(row=2, column=4)


        Image4 = ImageTk.PhotoImage(Image.open(path + '\\' + images[3]))
        label4 = Label(fenetre, image=Image4)
        nom1_4 = images[0], split('.png')
        nom4 = nom1_4[0]
        labelNom4 = Label(fenetre, text=nom4, font='calibry 13 bold', background='white')
        ButtonMore4 = Button(fenetre, text='>>', background='black', foreground='white')
        label4.grid(row=3, column=0)
        ButtonMore4.grid(row=3, column=1, sticky=(S))
        labelNom4.grid(row=4, column=0)

        Image5 = ImageTk.PhotoImage(Image.open(path + '\\' + images[4]))
        label5 = Label(fenetre, image=Image5)
        nom1_5 = images[0], split('.png')
        nom5 = nom1_5[0]
        labelNom5 = Label(fenetre, text=nom5, font='calibry 13 bold', background='white')
        ButtonMore5 = Button(fenetre, text='>>', background='black', foreground='white')
        label5.grid(row=3, column=2)
        ButtonMore5.grid(row=3, column=3, sticky=(S))
        labelNom5.grid(row=4, column=2)

        Image6 = ImageTk.PhotoImage(Image.open(path + '\\' + images[5]))
        label6 = Label(fenetre, image=Image6)
        nom1_6 = images[0], split('.png')
        nom6 = nom1_6[0]
        labelNom6 = Label(fenetre, text=nom6, font='calibry 13 bold', background='white')
        ButtonMore6 = Button(fenetre, text='>>', background='black', foreground='white')
        label6.grid(row=3, column=4)
        ButtonMore6.grid(row=3, column=5, sticky=(S))
        labelNom6.grid(row=4, column=4)

    except IndexError:
        pass

    fenetre.mainloop()


#Affichage de la fenetre d'accueil
root=Tk()
root.title('Sephora')
root.configure(background='black')
root.geometry('1000x500+0+0')
root.resizable(width=False,height=False)
image1=ImageTk.PhotoImage(Image.open('sephoraSS.jpg'))
labelWelcome= Label(root,image=image1,anchor=CENTER,height=200)
#labelWelcome.config(fontsize='50')
#frame=Frame(root,bg='black')
labelSephora= Label(root,text='~SEPHORA~',bg='black',fg='white',font='Times 50 bold italic')
labelSignIn=Label(root,text='Sign in to benefit from many discounts',bg='black',fg='white',font='Times 15 bold italic')
labelNext=Label(root,text='or you can simply continue as a guest',fg='white',bg='black',font='Times 15 bold italic')
nextButton=Button(root,text='Next',bg='white',fg='black',font='Times 20 bold italic',command=nextWelcome)
signInButton=Button(root,text='Sign in',bg='white',fg='black',font='Times 20 bold italic',command=signIn)

#frame.grid(row=1,column=2,columnspan=2,sticky=(W,E,N,S))
labelWelcome.grid(row=0,column=0,columnspan=4,sticky=(W,E))
labelSephora.grid(row=3,column=0,columnspan=3,rowspan=3)
labelSignIn.grid(row=2,column=3,sticky=(W,N,E,S))
signInButton.grid(row=3,column=3,sticky=(E,W,N,S))
labelNext.grid(row=4,column=3,sticky=(W,N,E,S))
nextButton.grid(row=5,column=3,sticky=(E,W,N,S))

#fenetre Sign In
usernameSI=StringVar()
passwordSI=StringVar()

#fenetre Sign Up
userInfos=[]
lastname=StringVar()
firstname=StringVar()
username=StringVar()
password=StringVar()
passconfirmation=StringVar()

#fenetre Site
fenetreSite=None

root.mainloop()
