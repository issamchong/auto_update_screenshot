
import tkinter as tk
from PIL import ImageTk,Image
import pyscreenshot as ImageGrab #pyscreen only for linux  for win

path='/home/issam/detectionProduct/test.gif'

class Timer:
    def __init__(self, parent):
        # variable storing time
        im1 = ImageGrab.grab(bbox = (10,10,510,510))
        im1.save("test.gif")
        img = ImageTk.PhotoImage(Image.open(path))
        self.label = tk.Label(parent, image=img)
        self.label.pack(side="bottom", fill="both", expand="y")
        #self.seconds = 0
        # label displaying time
        #self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
        #self.label.pack()
        # start the timer
        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        #self.seconds += 1
        # display the new time
        #self.label.configure(text="%i s" % self.seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        im2 = ImageGrab.grab(bbox = (10,10,510,510))
        im2.save("test.gif")
        img2 = ImageTk.PhotoImage(Image.open(path))
        self.label.configure(image=img2)
        self.label.image_names = img2
        #self.label.after(1000, self.refresh_label)
        self.label.after(1000,self.refresh_label)

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()