from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v =Vue(self)
        
        #A CHANGER DE PLACE.... POUR TEST SEULEMENT !
        self.commencerPartie()
        self.jouer()
        
        self.v.root.mainloop()
        
    def afficherEtatJeu(self,carre,pions,bordures):
        self.v.afficherEtatJeu(carre,pions,bordures)
    
    def changementPosCarre(self, event, ancienX, ancienY):
        deltaX = event.x - ancienX
        deltaY = event.y - ancienY
        self.m.p.c.changementPos(deltaX,deltaY)
    
    def commencerPartie(self):
        self.m.commencerPartie()
    
    def jouer(self):
        self.m.p.jouer()
    
    def click(self,event):
        self.m.click(event)

    def mort(self):
        self.v.afficherTemps(0.5)
        
if __name__ == '__main__':
    c = Controleur()
