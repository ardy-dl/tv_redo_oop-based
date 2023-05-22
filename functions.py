import tkinter as tk

root = tk.Tk()
root.title("Test Driver (TV)")
text = tk.Text(root, width=40, height=10)
text.pack()

# create the class
class TV:
    # initialize the class
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        self.name = name
        self.channel = channel
        self.volume = volume
        self.is_on = False
    # show the name of the object, channel and volume level
    def show(self):
        text.insert(tk.END, f"{self.name} - channel: {self.channel} | volume: {self.volume}\n")
    # show the status of the object
    def status(self):
        print(self.name, "Status: ON" if self.is_on else "Status: OFF")
    def turn_on(self):
        self.is_on = True
        print(self.name, "is turned ON")
    def turn_off(self):
        self.is_on = False
        print(self.name, "is turned OFF")
    # channel
    def get_channel(self):
        print(self.name + " channel: " + str(self.channel))
    def set_channel(self, new_channel):
        self.channel = new_channel
        print("New channel has been set for " + self.name + ":s " + str(new_channel))
    def channel_up(self):
        self.channel += 1
    # decrease channel
    def channel_down(self):
        self.channel -= 1
    # volume
    def get_volume(self):
        print(self.name + " volume: " + str(self.volume))
    def set_volume(self, new_volume):
        self.volume = new_volume
        print("New volume has been set for " + self.name + ": " + str(new_volume))
    # increase volume
    def volume_up(self):
        self.volume += 1
    # decrease volume  
    def volume_down(self):
        self.volume -= 1

