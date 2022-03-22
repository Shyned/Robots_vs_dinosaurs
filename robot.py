from weapon import Weapon
import random

"""

"""



class Robot:
    def __init__(self,name,attack_power,health) :
        self.name = name
        self.attack_power =Weapon("",0)
        self.health = 100
    
    
    #dinosaur will be a index position and will be deleted once health <=0
    
    def attack(self,dinosaur:list):
        dinosaur.health= self.attack_power.attack_power- dinosaur.health




# wood_axe = Weapon("axe",70)
# Peter_bot=Robot("Peter",wood_axe,100)
# Peter_bot.attack(100)




        
            

        
        



