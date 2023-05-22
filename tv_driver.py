# create separate file for TV functions
from functions import TV
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Test Driver (TV)")
root.config(bd=15)
text = tk.Text(root, width=40, height=10)
text.pack()



# create pseudocode for ui file
# create pseudocode for Tv functions
# create objects
tv1 = TV("tv1", 30, 3)
tv2 = TV("tv2", 3, 2)

my_tv = TV()


# call the methods using the objects
tv1.show(text)  
tv2.show(text)
my_tv.show(text)
my_tv.turn_off()
my_tv.status()
my_tv.get_channel()
my_tv.set_channel(122)
my_tv.show(text)
tv2.channel_up()
tv2.show(text)
tv1.volume_down()   
tv1.show(text)


root.mainloop()