from weapon import Weapon
from random import choice

#Weapon  passed in for attack_power 
class Robot:
    def __init__(self,name:str,health:int) :
        self.name = name
        self.weapon = ''  
        self.health = 100
        self.weapon_picker()
    
    def weapon_picker (self):
      axe =  Weapon('axe', 20)
      laser = Weapon(laser, 50)
      bat = Weapon(bat, 10)
      weed_eater = Weapon(weed_eater, 100)
      weapon_list = [axe,laser,bat,weed_eater]
      self.weapon = choice(weapon_list)

   
    
    def attack(self,dinosaur):
       dinosaur.health -= self.weapon.attack_power
        
        
