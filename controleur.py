from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.commencerPartie()
    
    def changementPosCarre(self, event):
        pass
    
    def commencerPartie(self):
        self.m.commencerPartie()
        
if __name__ == '__main__':
    c = Controleur()