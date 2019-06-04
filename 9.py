from tkinter import *

a = Tk()
a.title("wellcome")

b = IntVar()

radl1 = Radiobutton(a, text = "pirst", value = 1, variable = b)
radl2 = Radiobutton(a, text = "second", value = 2, variable = b)
radl3 = Radiobutton(a, text = "Third", value = 3, variable = b)

def onClick():
    print(b.get())

bnt = Button(a, text = "Click Me!", command = onClick)

radl1.grid(column = 0, row = 0)
radl2.grid(column = 1, row = 0)
radl3.grid(column = 2, row = 0)
bnt.grid(column = 3, row = 0)

a.mainloop()