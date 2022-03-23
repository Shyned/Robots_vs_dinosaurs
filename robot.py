from dinosaur import Dinosaur
from weapon import Weapon


import random

#Weapon  passed in for attack_power 
class Robot:
    def __init__(self,name:str,Weapon,health:int) :
        self.name = name
        #Weapon.attack_power for attack power and Weapon.name to name
        
        self.health = 100
        self.hit_points = ''
    
    
    #dinosaur will be a index position and will be deleted once health <=0
    
    def attack(self,dinosaur):
        damage_list =[1,.2,.3,2,1]
        
        self.hit_points = random.choice(damage_list)*Weapon.attack_power()
        print(f"{self.name}used the {self.name}on{dinosaur[0].name()}.")

        dinosaur[0].health=self.hit_points - dinosaur.health()
        
        

dino = []



rob =Dinosaur(100,"rob",100)
bab=Dinosaur(100,"bab",20)
dino.append(bab)
dino.append(rob)

wood_axe = Weapon("axe",1)


Peter_bot=Robot("Peter",wood_axe,100)

Peter_bot.attack(dino)