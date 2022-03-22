from weapon import Weapon
import random

"""

"""



class Robot:
    def __init__(self,name,attack_power,health) :
        self.name = name
        self.attack_power =Weapon("sword",0)
        self.health = 100
    
    def attack(self,dinosaur):
        if self.attack_power.attack_power>=dinosaur:
            dinosaur = 0
            print(dinosaur)
            

        else:
            dinosaur= self.attack_power.attack_power- dinosaur




wood_axe = Weapon("axe",70)
Peter_bot=Robot("Peter",wood_axe,100)
Peter_bot.attack(100)




        
            

        
        



