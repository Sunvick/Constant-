from tkinter import*
from tkinter import ttk
window = Tk()

window.geometry('400x230+10+20')
window.title('Text Field')

txtfld = Entry(window, text = "This is a text field", bd = 5)
txtfld.place(x=130, y=85)

window.mainloop()