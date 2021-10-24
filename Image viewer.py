from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('sephora')

image1 = ImageTk.PhotoImage(Image.open('images/s...png')) #pour acceder a l image
image2 = ImageTk.PhotoImage(Image.open('images/sephora2...png'))
image3 = ImageTk.PhotoImage(Image.open('images/sephora3...png'))

image_list = [image1,image2,image3]

label1= Label(image=image1)
label1.grid(row=0,column=0,columnspan=3)

def forward(imageNum):
    global label1
    global buttonForward
    global buttonBack #to upadte the button every time we click on it

    label1.grid_forget()
    label1 = Label(image=image_list[imageNum - 1])
    buttonForward = Button(root,text=">>",command=lambda: forward(imageNum+1))
    buttonBack = Button(root,text="<<",command=lambda: back(imageNum-1))

    if imageNum== len(image_list):#pour eviter l'erreur out of range
        buttonForward = Button(root,text=">>",state=DISABLED)

    label1.grid(row=0, column=0, columnspan=3,sticky=(W,N,E,S))
    buttonBack.grid(row=1,column=0)
    buttonForward.grid(row=1,column=2)#reafficher les widgets apres modification

def back(imageNum):
    global label1
    global buttonForward
    global buttonBack  # to upadte the button every time we click on it

    label1.grid_forget()
    label1 = Label(image=image_list[imageNum - 1])
    buttonForward = Button(root, text=">>", command=lambda: forward(imageNum + 1))
    buttonBack = Button(root, text="<<", command=lambda: back(imageNum - 1))

    if imageNum == 1:  # pour eviter l'erreur out of range
        buttonBack= Button(root, text="<<", state=DISABLED)

    label1.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

buttonBack = Button(root,text="<<",command=back,state=DISABLED)
buttonExit = Button(root,text="Exit",command=root.quit)#ou root.destroy
buttonForward=Button(root,text=">>",command=lambda:forward(2))#on a appelee la fct forward avec l'argument 2 on peut mettre 1

buttonBack.grid(row=1,column=0)
buttonExit.grid(row=1,column=1)
buttonForward.grid(row=1,column=2)


labelDescription= Label(root,text="Description du produit")
labelDescription.grid(row=2,column=0,columnspan=3,sticky=(E,W,S,N))

root.mainloop()