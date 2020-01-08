import pyscreenshot as ImageGrab #pyscreen only for linux  for windows use 
#from PIL import ImageGrab 
from PIL import Image,ImageTk
from  tkinter import *

root=Tk()
my_label=Label(root,text="testing")
my_label.pack()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
canvas=Canvas(root,width=500,height=500)
canvas.pack()
my_image=PhotoImage(file='/home/issam/detectionProduct/test.gif')
canvas.create_image(0,0,anchor=NW,image=my_image )
button1=Button(topframe,text="get_screen",fg="red")
button1.pack()
im2 = ImageGrab.grab(bbox = (10,10,510,510))
im2.save("test.gif")
canvas.after(10)
im2 = ImageGrab.grab(bbox = (10,10,510,510))
im2.save("test.gif")
canvas.update_idletasks
root.mainloop()

#im2.show() 

