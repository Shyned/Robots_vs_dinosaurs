from unicodedata import name
from robot import Robot






class Fleet:
    def __init__(self) :
        self.robo_fleet = []


    def create_fleet(self):
        self.robo_fleet.append(Robot(name,attack_power,health))
        self.robo_fleet.append(Robot(name,attack_power,health))
        self.robo_fleet.append(Robot(name,attack_power,health))
        


    




army=Fleet()
army.create_fleet()



