class Device:
    def turn_on(self):
        pass 
class TV(Device):
    def turn_on(self):
        print("TV on") 
class Radio(Device):
    def turn_on(self):
        print("Radio on") 
class BasicRemote:
    def __init__(self, device):
        self.device = device 
    def power(self):
        self.device.turn_on() 
class AdvancedRemote(BasicRemote):
    def mute(self):
        print("Device muted")
 
tv = TV()
basic_remote = BasicRemote(tv)
basic_remote.power() 
radio = Radio()
advanced_remote = AdvancedRemote(radio)
advanced_remote.power()
advanced_remote.mute()
