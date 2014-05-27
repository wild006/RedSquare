# Fait par Alexandre Laplante-Turpin et Francois Genest
 

from modele import *
from vue import *
from time import time
from modele import Niveau

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v =Vue(self)        
        self.v.root.mainloop()
        
    def afficherEtatJeu(self,carre,pions,bordures,powerUp):
        self.v.afficherEtatJeu(carre,pions,bordures,powerUp)
    
    def changementPosCarre(self, event, ancienX, ancienY):
        deltaX = event.x - ancienX
        deltaY = event.y - ancienY
        self.m.p.c.changementPos(deltaX,deltaY)
    
    def commencerPartie(self, niveau):
        self.m.commencerPartie(niveau)
    
    def recommencerPartie(self):
        self.m.commencerPartie(self.m.dernierNiveau)
    
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
    
    def sauvegarderHighscore(self, nom):
        print("Mon score est ", nom)
        self.m.p.sauvegarderHighscore(nom)

    def changerOptions(self,powerUps,nbSauvegarde):
        self.m.changerOptions(powerUps, nbSauvegarde)

    def getPowerUp(self):
        return self.m.isPowerUp
    
    def getDernierNiveau(self):
        return self.m.dernierNiveau

    def getNbSauvegarde(self):
        return self.m.limiteHighscore

    def getScore(self):
        return self.m.highscore

    def getScoreSession(self):
        return self.m.scoreSession

if __name__ == '__main__':
    c = Controleur()
