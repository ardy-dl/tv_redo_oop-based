import tkinter as tk
from tkinter import messagebox


# create the class
class TV:
    # initialize the class
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        self.name = name
        self.channel = channel
        self.volume = volume
        self.is_on = False
    # show the name of the object, channel and volume level
    def show(self, text_widget):
        text_widget.insert(tk.END, f"{self.name} - channel: {self.channel} | volume: {self.volume}\n")
    # show the status of the object
    def status(self):
        status = f"{self.name} Status: ON" if self.is_on else f"{self.name} Status: OFF"
        messagebox.showinfo("Status", status)
    def turn_on(self):
        self.is_on = True
        messagebox.showinfo("Turn ON", f"{self.name} is turned ON.")
    def turn_off(self):
        self.is_on = False
        messagebox.showinfo("Turn OFF", f"{self.name} is turned OFF.")
    # channel
    def get_channel(self):
        messagebox.showinfo("Channel", f"{self.name}'s channel is {self.channel}")
    def set_channel(self, new_channel):
        self.channel = new_channel
        messagebox.showinfo("Set Channel", f"New channel has been set: {new_channel}")
    def channel_up(self):
        self.channel += 1
    # decrease channel
    def channel_down(self):
        self.channel -= 1
    # volume
    def get_volume(self):
        messagebox.showinfo("Volume", f"{self.name}'s volume level is {self.volume}")
    def set_volume(self, new_volume):
        self.volume = new_volume
        messagebox.showinfo("Set Volume", f"New volume level has been set: {new_volume}")
    # increase volume
    def volume_up(self):
        self.volume += 1
    # decrease volume  
    def volume_down(self):
        self.volume -= 1

