from time import time
import math

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.grandeurJeuX = 460 #Selon la doc...
        self.grandeurJeuY = 460
        self.largeurBordure = 60
        self.highscore = []
        self.scoresSession = []
        self.limiteHighscore = 3
        #A FAIRE: Mettre les options
    
    def commencerPartie(self):
        self.p = Partie(self)
        self.parent.afficherEtatJeu(self.p.c,self.p.pions,self.p.bordures)#Afficher le jeu des le depart
        #Initialiser le carre
    
class Partie():
    def __init__(self, parent):
        print("Partie")
        self.parent = parent
        self.c = Carre(self)
        self.pions = []
        self.bordures = []
        self.finPartie = False
        self.tempsDepart = 0
        self.tempsFin = 0
        self.nbChangementVitesse = 0
        self.incrVit = 2
        self.nbSecIncrVit = 8
        
        vitesseDeBaseX = 9 #Pour avoir toute la meme vitesse au depart
        vitesseDeBaseY = 12
        
        self.pions.append(Pion(self,100,100,60,60, vitesseDeBaseX, vitesseDeBaseY))
        self.pions.append(Pion(self,300,85,60,50, -vitesseDeBaseX, vitesseDeBaseY))
        self.pions.append(Pion(self,85,350,30,60, vitesseDeBaseX, -vitesseDeBaseY))
        self.pions.append(Pion(self,355,340,100,20, -vitesseDeBaseX, -vitesseDeBaseY))
        self.bordures.append(Bordure(0,0,self.parent.grandeurJeuX,self.parent.largeurBordure))#haut
        self.bordures.append(Bordure(0,self.parent.largeurBordure,self.parent.largeurBordure,self.parent.grandeurJeuY - (2*self.parent.largeurBordure)))#gauche
        self.bordures.append(Bordure(0,self.parent.grandeurJeuY-self.parent.largeurBordure,self.parent.grandeurJeuX, self.parent.largeurBordure))#bas
        self.bordures.append(Bordure(self.parent.grandeurJeuX-self.parent.largeurBordure,self.parent.largeurBordure,self.parent.largeurBordure,self.parent.grandeurJeuY - (2*self.parent.largeurBordure)))#droite
        
    def jouer(self):
        for pion in self.pions:
            pion.changementPos()
        
        self.c.collisions()
        self.parent.parent.afficherEtatJeu(self.c,self.pions,self.bordures)
        if self.finPartie == True:
            print("mort")
            self.tempsFin = time()-self.tempsDepart
            print(self.tempsFin)
            print(self.tempsDepart)
            self.parent.parent.mort(self.tempsFin)
            print("TEMPS ", self.tempsFin)
        else:
            if math.floor((time()-self.tempsDepart)/self.nbSecIncrVit) > self.nbChangementVitesse:
                print("CHANGEMENT vitesse", math.floor((time()-self.tempsDepart)/self.nbSecIncrVit))
                for pion in self.pions:
                    print("vitesse avant" , pion.vitesseX, " ", pion.vitesseY)
                    pion.changementVitesse(self.incrVit)
                    print("vitesse apres" , pion.vitesseX, " ", pion.vitesseY)
                self.nbChangementVitesse = self.nbChangementVitesse + 1
                print(self.nbChangementVitesse)
            self.parent.parent.v.root.after(50,self.jouer)
            
    def sauvegarderHighscore(self,nom):
        print(self.tempsFin)
        #BUG ! LE TEMPS EST TOUJOURS 0 DEVRAIT SE REGLER AVEC LE MENU...
        
        score = [nom, self.tempsFin]
       
        self.parent.scoresSession.append(score)
        self.parent.highscore.append(score)
        
        self.parent.highscore.sort(key=lambda highscore: highscore[1], reverse=True)
        
        if len(self.parent.highscore) > self.parent.limiteHighscore:
            self.parent.highscore = self.parent.highscore[0:self.parent.limiteHighscore] #On enleve le score en trop
            
        for i in self.parent.scoresSession:
            print(i)
        for i in self.parent.highscore:
            print(i)
        
class Carre():
    def __init__(self, parent):
        self.parent = parent
        self.x = 225 #Selon la doc... Depend de notre grandeur de jeu...
        self.y = 225
        self.couleur = "red"
        self.dim = 40
    
    def changementPos(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

    def collisionObstacle(self,obstacle):        
        for i in obstacle:
            if self.x > i.x1 and self.x <i.x2 and self.y > i.y1 and self.y < i.y2:
                    self.parent.finPartie = True
            elif self.x +self.dim > i.x1 and self.x + self.dim <i.x2 and self.y > i.y1 and self.y < i.y2:
                    self.parent.finPartie = True
            elif self.x > i.x1 and self.x <i.x2 and self.y + self.dim > i.y1 and self.y + self.dim < i.y2:
                self.parent.finPartie = True
            elif self.x  + self.dim> i.x1 and self.x  + self.dim<i.x2 and self.y + self.dim > i.y1 and self.y + self.dim < i.y2:
                self.parent.finPartie = True
    
    def collisions(self):
        if self.x < 0 or self.x > self.parent.parent.grandeurJeuX:
            self.parent.finPartie = True
        elif self.y < 0 or self.y > self.parent.parent.grandeurJeuY:
            self.parent.finPartie = True
        else:
            self.collisionObstacle(self.parent.pions)
            self.collisionObstacle(self.parent.bordures)
        
class Pion():
    def __init__(self,parent,x,y, largeur, hauteur, vitesseX, vitesseY):
        self.parent = parent
        self.x1 = x #haut/gauche
        self.y1 = y
        self.x2 = x + largeur #bas/droite
        self.y2 = y + hauteur
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.couleur ="blue"
    
    def changementPos(self):
        self.x1 = self.x1 + self.vitesseX
        self.x2 = self.x2 + self.vitesseX
        self.y1 = self.y1 + self.vitesseY
        self.y2 = self.y2 + self.vitesseY
        if self.x1 <= 0 and self.vitesseX < 0:
            self.vitesseX = self.vitesseX * -1
        if self.x2 >= self.parent.parent.grandeurJeuX and self.vitesseX > 0:
            self.vitesseX = self.vitesseX * -1
        if self.y1 <= 0 and self.vitesseY < 0:
            self.vitesseY = self.vitesseY * -1
        if self.y2 >= self.parent.parent.grandeurJeuY and self.vitesseY > 0:
            self.vitesseY = self.vitesseY * -1
            
    def changementVitesse(self, incrVit):
        if self.vitesseX < 0:
            self.vitesseX = self.vitesseX - incrVit
        else:
            self.vitesseX = self.vitesseX + incrVit
        if self.vitesseY < 0:
            self.vitesseY = self.vitesseY - incrVit
        else:
            self.vitesseY = self.vitesseY + incrVit        
            
class Bordure():
    def __init__(self,x,y,largeur,hauteur):
        self.x1 =x 
        self.y1 = y
        self.x2 = x + largeur 
        self.y2= y +hauteur
        self.couleur ="black"
    
