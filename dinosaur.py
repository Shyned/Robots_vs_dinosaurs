import random




from re import A




class Dinosaur:
    def __init__(self,attack_power,name,health) :
        self.name = name
        self.attack_power = attack_power
        self.health = 100




    def attack(self,robot:list):
        damages_list =[20,30,40,10,50,60]
        self.attack_power = random.choice(damages_list)
        robot.health = robot.health - self.attack_power






        

