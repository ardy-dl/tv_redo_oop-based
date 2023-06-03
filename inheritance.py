from functions import TV
import tkinter as tk
from tkinter import messagebox

class TvUpgraded(TV):
# save favorite channel
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        super().__init__(name, channel, volume)
        self.favorite_channels = []

    def save_favorite_channel(self, channel):
        if channel not in self.favorite_channels:
            self.favorite_channels.append(channel)
            messagebox.showinfo("Save Favorite", f"{channel.name} saved as a favorite channel.")

    def remove_favorite_channel(self, channel):
        if channel in self.favorite_channels:
            self.favorite_channels.remove(channel)
            messagebox.showinfo("Remove Favorite", f"{channel.name} removed from favorite channels.")

    def get_favorite_channels(self):
        return self.favorite_channels
