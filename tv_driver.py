# create separate file for TV functions
from functions import TV
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
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
tv1.status()

root.mainloop()