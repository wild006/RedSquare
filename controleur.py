from modele import *
from vue import *
from time import time

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v =Vue(self)

        
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
        self.m.p.tempsDepart = time()
        self.m.p.jouer()
    
    def click(self,event):
        self.m.click(event)

    def mort(self, temps):
        self.v.afficherTemps(temps)
        self.v.saveWindows()
        
    def getGrandeurJeuX(self):
        return self.m.grandeurJeuX
    
    def getGrandeurJeuY(self):
        return self.m.grandeurJeuY
    
    def sauvegarderHighscore(self, score):
        self.m.p.sauvegarderHighscore(score)
        
           
if __name__ == '__main__':
    c = Controleur()
