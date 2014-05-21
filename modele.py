class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.grandeurJeuX = 460 #Selon la doc...
        self.grandeurJeuY = 460
        self.largeurBordure = 60
        #A FAIRE: Mettre les options
    
    def commencerPartie(self):
        self.p = Partie(self)
        #Initialiser le carre
        
    
class Partie():
    def __init__(self, parent):
        print("Partie")
        self.parent = parent
        self.c = Carre()
        self.pions = []
        self.bordures = []
        
        vitesseDeBase = 4 #Pour avoir toute la meme vitesse au depart
        
        self.pions.append(Pion(self,100,100,60,60, vitesseDeBase, vitesseDeBase))
        self.pions.append(Pion(self,300,85,60,50, -vitesseDeBase, vitesseDeBase))
        self.pions.append(Pion(self,85,350,30,60, vitesseDeBase, -vitesseDeBase))
        self.pions.append(Pion(self,355,340,100,20, -vitesseDeBase, -vitesseDeBase))
        self.bordures.append(Bordure(0,0,self.parent.grandeurJeuX,self.parent.largeurBordure))#haut
        self.bordures.append(Bordure(0,self.parent.largeurBordure,self.parent.largeurBordure,self.parent.grandeurJeuY - (2*self.parent.largeurBordure)))#gauche
        self.bordures.append(Bordure(0,self.parent.grandeurJeuY-self.parent.largeurBordure,self.parent.grandeurJeuX, self.parent.largeurBordure))#bas
        self.bordures.append(Bordure(self.parent.grandeurJeuX-self.parent.largeurBordure,self.parent.largeurBordure,self.parent.largeurBordure,self.parent.grandeurJeuY - (2*self.parent.largeurBordure)))#droite
        
    def jouer(self):
        for pion in self.pions:
            pion.changementPos()
        self.c.collisions(self.pions)
        self.c.collisions(self.bordures)
        self.parent.parent.afficherEtatJeu(self.c,self.pions,self.bordures)
        self.parent.parent.v.root.after(50,self.jouer)
        
class Carre():
    def __init__(self):
        self.x = 225 #Selon la doc... Depend de notre grandeur de jeu...
        self.y = 225

        self.couleur = "red"
        self.dim = 40
    
    def changementPos(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

    def collisions(self,obstacle):
        
        for i in obstacle:
            if self.x > i.x1 and self.x <i.x2 and self.y > i.y1 and self.y < i.y2:
                    print("mort")
                    
            elif self.x +self.dim > i.x1 and self.x + self.dim <i.x2 and self.y > i.y1 and self.y < i.y2:
                    print("mort")
                    
            elif self.x > i.x1 and self.x <i.x2 and self.y + self.dim > i.y1 and self.y + self.dim < i.y2:
                    print("mort")
                    
            elif self.x  + self.dim> i.x1 and self.x  + self.dim<i.x2 and self.y + self.dim > i.y1 and self.y + self.dim < i.y2:
                    print("mort")
        
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
            
class Bordure():
    def __init__(self,x,y,largeur,hauteur):
        self.x1 =x 
        self.y1 = y
        self.x2 = x + largeur 
        self.y2= y +hauteur
        self.couleur ="black"
    
