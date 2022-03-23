from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
from robot import Robot




class Battlefeild:
    def __init__(self) :
        self.fleet = Fleet
        self.herd = Herd



    def run_game(self):
        self.display_welcome
        while len(self.fleet)>0 or len(self.herd) >0:
            self.show_robo_oppent_options
            self.dino_turn
            self.battle
            self.show_dino_opponent_options
            self.robo_turn
            self.battle

        else:
            self.display_winners
            



    def display_welcome(self):
        answer = ["n","y"]
        play_game = input("Would you like to play (y or n): ")

        while play_game not in answer:
            play_game = input("Would you like to play (y or n): ")

        else:
            if play_game == 'n':
                quit

            else:
                pass




    def battle(self):
        for robot in self.fleet:
            if robot.health <=0:
                self.fleet.remove(robot)
                print(f"{robot.name} has died in battle!")


        for dino in self.herd:
            if dino.health<=0:
                self.herd.remove(dino)
                print(f"{dino.name} has died in battle!")
                
        


    def dino_turn(self,dinosaur):
        Dinosaur.attack(self.fleet)



    def robo_turn (self,robot):

        Robot.attack(self.herd)


    def show_dino_opponent_options (self):
        for robot in self.fleet:
            print(robot.name())


    def show_robo_oppent_options(self):
        for dino in self.herd:
            print(dino.name())

    def display_winners(self):
        if len(self.fleet) ==0:
            print("Robots won!")
        elif len(self.fleet)==0:
            print("Dinosaurs Have won!")
        



test= Battlefeild
test.show_dino_opponent_options()
test.show_robo_oppent_options()