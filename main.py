from tkinter import *
window = Tk()

window.geometry("400x200+10+20")
window.title("Father of Computer")

label=Label(window,text = "Charles Babbage" , fg ="Black", bg= "cyan",font=("Verdana",17))
label.place(x=100,y=70)


window.mainloop()