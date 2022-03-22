from unicodedata import name
from dinosaur import Dinosaur





class Herd:
    def __init__(self) :
        self.dino_herd = []

    def create_herd(self):
        self.dino_herd.append(Dinosaur(attack_power,name,health))
        self.dino_herd.append(Dinosaur(attack_power,name,health))
        self.dino_herd.append(Dinosaur(attack_power,name,health))
        

        
            


gary=Dinosaur(50,"gary",100)
dinos=Herd
dinos.create_herd(gary)
print(Herd.dino_herd)
