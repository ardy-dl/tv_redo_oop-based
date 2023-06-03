# create separate file for TV functions
from functions import TV
import tkinter as tk
from tkinter import messagebox
from inheritance import TvUpgraded

root = tk.Tk()
root.title("Test Driver (TV)")
root.config(bd=15)
text = tk.Text(root, width=40, height=10)
text.pack()

# create objects
tv1 = TvUpgraded("tv1", 30, 3)
tv2 = TvUpgraded("tv2", 3, 2)
my_tv = TvUpgraded()

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
my_tv.save_favorite_channel(tv1)
favorite_channels = my_tv.get_favorite_channels()

text.insert(tk.END, "Favorite Channels:\n")
for channel in favorite_channels:
    text.insert(tk.END, f"{channel.name} - channel: {channel.channel}\n")

root.mainloop()