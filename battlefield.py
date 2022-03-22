from herd import Herd
from fleet import Fleet




class Battlefeild:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()



    def run_game(self):
        pass


    def display_welcome(self):
        answer = ["n","y"]
        play_game = input("Would you like to play (y or n): ")
        
        while play_game not in answer:
            play_game

        else:




    def battle(self):
        pass



    def dino_turn(self,dinosaur):
        pass



    def robo_turn (self,robot):
        pass


    def show_dino_opponent_options (self):
        self.robo_fleet


    def show_robo_oppent_options(self):
        pass

    def display_winners(self):
        pass