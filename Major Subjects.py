from tkinter import *
window = Tk()

window.geometry("400x200+10+20")
window.title("Major Subjects")

lb = Listbox(window, height=5, selectmode="single")
data = "reading","writing","arithmetic","coding"
for num in data:
    lb.insert(END, num)
lb.place(x=140)


window.mainloop()