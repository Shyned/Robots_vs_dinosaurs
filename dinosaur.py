
from random import choice


from re import A




class Dinosaur:
    def __init__(self,attack_power:int,name:str,health:int) :
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.move = ''




    def attack(self,robot:list):
        damages_list =[20,30,40,10,50,60]

        move_list = ["Bite",'Roar',"Tailwhip","Stomp"]
        self.move=choice(move_list)

        self.attack_power = choice(damages_list)

        print(f"{self.name} used {self.move}  doing {self.attack_power} points of damage ")
        robot.health = robot.health - self.attack_power
        print(robot.health)




