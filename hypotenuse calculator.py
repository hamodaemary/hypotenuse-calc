from tkinter import *
from math import sqrt
x=Tk() 
def tri():
	y=int(ent.get())
	z=int(enu.get())
	c=sqrt((y*y)+(z*z))
	lbl.config(text=c)

x.title('right angle triangle')
ent = Entry(bd=2)
ent.pack()
enu = Entry(bd=2)
enu.pack()
but = Button(text='calculate',command=tri)
but.pack()
lbl = Label(text='')
lbl.pack()
x.mainloop()