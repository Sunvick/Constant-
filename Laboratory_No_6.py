from tkinter import *
window = Tk()
window.title('Semestral Grade')
window.geometry("400x350+20+10")

class Mywindow:
    def __init__(self, window):
        self.lbl1 = Label(window, font="Calibri", text="Semestral Grade")
        self.lbl1.place(relx=0.50, y=50, anchor="center")

        self.lbl2 = Label(window, font="Calibri", text="Prelim Grade:")
        self.lbl2.place(x=50, y=80)

        self.txtfield2 = Entry(window, font="Calibri", bd=3)
        self.txtfield2.place(x=180, y=80)

        self.lbl3 = Label(window, font="Calibri", text="Midterm Grade:")
        self.lbl3.place(x=50, y=120, )

        self.txtfield3 = Entry(window, font="Calibri", bd=3)
        self.txtfield3.place(x=180, y=120)

        self.lbl4 = Label(window, font="Calibri", text="Final Grade:")
        self.lbl4.place(x=50, y=160, )

        self.txtfield4 = Entry(window, font="Calibri", bd=3)
        self.txtfield4.place(x=180, y=160)

        self.btn1 = Button(window, font="Calibri", text="Semestral Grade", command=self.Grade)
        self.btn1.place(relx=0.50, y=220, anchor="center")

        self.txtfield5 = Entry(window, font="Calibri", bd=3)
        self.txtfield5.place(relx=.50, y=255, anchor="center")

    def Grade(self):
        self.txtfield5.delete(0, 'end')
        Prelim = int(self.txtfield2.get())
        Midterm = int(self.txtfield3.get())
        Final = int(self.txtfield4.get())
        Grade = Prelim*.30+Midterm*.30+Final*.40
        self.txtfield5.insert(END, str(Grade))


mywin = Mywindow(window)
window.mainloop()
