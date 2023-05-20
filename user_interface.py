# create the class
class TV:
    # initialize the class
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        self.name = name
        self.channel = channel
        self.channel = volume
        self.is_on = False
    # show the name of the object, channel and volume level
    def show(self):
        print(self.name)
    # show the status of the object
