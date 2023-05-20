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
        print (str(self.name) + " - " + "channel:" + str(self.channel) + " volume:" + str(self.volume))
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
        print("New channel has been set: " + str(new_channel))
    
    # get volume
    # set volume
    # channel up
    # channel down
    # volume up
    # volume down