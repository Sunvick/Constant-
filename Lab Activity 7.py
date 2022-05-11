from tkinter import *

window = Tk()

def Window(source, side):
    calc = Frame(source, borderwidth=4, bd=4, bg="light blue")
    calc.pack(side=side, expand=YES, fill=BOTH)
    return calc

def button(source, side, text, command=None):
    calc = Button(source, text=text, command=command)
    calc.pack(side=side, expand=YES, fill=BOTH)
    return calc

class calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Standard Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="light blue").pack(side=TOP, expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = Window(self, TOP)
            for clear in clearButton:
                button(erase, LEFT, clear, lambda calc=display, q=clear: calc.set(''))

        for NumberButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = Window(self, TOP)
            for integer in NumberButton:
                button(FunctionNum, LEFT, integer, lambda calc=display, q=integer: calc.set(calc.get() + q))

        EqualButton = Window(self, TOP)
        for equals in "=":
            if equals == '=':
                equalbutton = button(EqualButton, LEFT, equals)
                equalbutton.bind('<ButtonRelease-1>', lambda e, s=self, calc=display: s.calc(calc), '+')

            else:
                equalbutton = button(EqualButton, LEFT, equals, lambda calc=display, s=' %s ' % equals: calc.set(calc.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    calculator().mainloop()