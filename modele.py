from time import time
import math
import random

class Niveau():
    facile = 0
    classique = 1
    expert = 2

class TypePowerUp():
    petit = 0
    grand = 1

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.grandeurJeuX = 460 #Selon la doc...
        self.grandeurJeuY = 460
        self.largeurBordure = 60
        self.highscore = []
        self.scoreSession = []
        self.limiteHighscore = 3
        self.lireHighscore()
        self.dernierNiveau = Niveau.classique
        #A FAIRE: Mettre les options
    
    def commencerPartie(self, niveau):
        self.p = Partie(self, niveau)
        self.parent.afficherEtatJeu(self.p.c,self.p.pions,self.p.bordures, self.p.powersUP)#Afficher le jeu des le depart
        #Initialiser le carre
        
    def ecrireHighscore(self):
        fichierHighscore = open("score.txt", 'w')
        for i in self.highscore:
            fichierHighscore.write((str(i[0]) + ","+ str(i[1])+ "\n"))
        fichierHighscore.close()
        
    def lireHighscore(self):
        try:
            fichierHighscore = open("score.txt", 'r')
            self.highscore = [] #Pour etre sur d'avoir seulement les socres du fichier
            
            for line in fichierHighscore:
                self.highscore.append(line.split(','))
            for score in self.highscore:
                score[1] = float(score[1])
                
            fichierHighscore.close()
        except:
            pass #Le fichier n'est pas cree
    
class Partie():
    def __init__(self, parent, niveau):
        print("Partie")
        self.parent = parent
        self.c = Carre(self)
        self.pions = []
        self.bordures = []
        self.powersUP = []
        self.niveau = niveau
        self.parent.dernierNiveau = niveau
        self.finPartie = False
        self.tempsDepart = 0
        self.tempsFin = 0
        self.nbChangementVitesse = 0
        self.incrVit = 2
        self.nbSecIncrVit = 8
        self.probPowerUp = 0.08
        self.isPowerUp = True
        
        #Pour avoir toute la meme vitesse au depart
        if niveau == Niveau.facile:
            self.incrVit = 1
            vitesseDeBaseX = 8 
            vitesseDeBaseY = 10
        elif niveau == Niveau.classique:
            self.incrVit = 2
            vitesseDeBaseX = 9 
            vitesseDeBaseY = 12
        elif niveau == Niveau.expert:
            self.incrVit = 2
            vitesseDeBaseX = 14 
            vitesseDeBaseY = 18
        
        
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
            
        #PowerUp
        if self.isPowerUp:
            for powerUp in self.powersUP:
                powerUp.changementPos()
            self.apparitionPowerUp()
            
        self.c.collisions()
        self.parent.parent.afficherEtatJeu(self.c,self.pions,self.bordures, self.powersUP)
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
        score = [nom, self.tempsFin]
       
        self.parent.scoreSession.append(score)
        self.parent.highscore.append(score)
        
        self.parent.highscore.sort(key=lambda highscore: highscore[1], reverse=True)
        
        if len(self.parent.highscore) > self.parent.limiteHighscore:
            self.parent.highscore = self.parent.highscore[0:self.parent.limiteHighscore] #On enleve le score en trop
            
        for i in self.parent.scoreSession:
            print(i)
        for i in self.parent.highscore:
            print(i)
        
        self.parent.ecrireHighscore()
        
    def apparitionPowerUp(self):
        if random.random() < self.probPowerUp:
            print("powerUP")
            self.powersUP.append(PowerUp(self,self.pions[0].vitesseX, self.pions[0].vitesseY, 40))

        
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
    
   # def collisionPowerUp(self, powerUp):
        
   # def collision(self, element):
        
        
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
            
class PowerUp(Pion):
    def __init__(self, parent, vitesseX, vitesseY, dim):
        x = random.randint(0,parent.parent.grandeurJeuX - dim)
        y = random.randint(0,parent.parent.grandeurJeuY - dim)
        Pion.__init__(self, parent, x, y, dim, dim, vitesseX, vitesseY)
        
        if random.random() <= 0.5:
            self.type = TypePowerUp.petit
            self.couleur = "yellow"
        else:
            self.type = TypePowerUp.grand
            self.couleur = "purple"
            
        #self.parent = parent
        
        #self.x2 = self.x1 + dim
        #self.y2 = self.y1 + dim
        #self.vitesseX = vitesseX
        #self.vitesseY = vitesseY
        
        print("POWER UP   : x1", self.x1, "x2", self.x2, "y1", self.y1, "y2", self.y2)
    
            
class Bordure():
    def __init__(self,x,y,largeur,hauteur):
        self.x1 =x 
        self.y1 = y
        self.x2 = x + largeur 
        self.y2= y +hauteur
        self.couleur ="black"
    
