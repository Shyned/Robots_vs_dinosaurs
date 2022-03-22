from unicodedata import name
from robot import Robot


class Fleet:
    def __init__(self) :
        self.robo_fleet = []


    def create_fleet(self,Robot):
        self.robo_fleet.append(Robot)
        self.robo_fleet.append(Robot)
        self.robo_fleet.append(Robot)




# army=Fleet()
# army.create_fleet(Peter_bot)
# print(army.robo_fleet[0].name)



