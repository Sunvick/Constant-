from tkinter import *
window = Tk()

window.geometry("400x200+10+20")
window.title("label")

label=Label(window,text = "Laboratory Activity 5" , fg ="Black")
label.place(x=150,y=40)
label=Label(window,text = "Submitted to: Ma'am Sayo" , fg ="Black")
label.place(x=140,y=70)


window.mainloop()