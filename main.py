from tkinter import *
window = Tk()

window.geometry("500x200+10+20")
window.title("Button")

bt=Button(window,text = "Click" , fg ="red", bg= "blue",activebackground='yellow')
bt.place(x=100,y=70)

bt=Button(window,text = "<--click to change the color of the button", fg ="Black",font=("Verdana",10))
bt.place(x=140,y=70)



window.mainloop()