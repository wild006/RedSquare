class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.grandeurJeuX = 450 #Selon la doc...
        self.grandeurJeuY = 450
        #A FAIRE: Mettre les options
    
    def commencerPartie(self):
        self.p = Partie(self)
        #Initialiser le carre
        
    def click(self,event):
        pass
        
    
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
        
    def jouer(self):
        for pion in self.pions:
            pion.changementPos()
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

    def collisions(self,pions,bordures):
        for i in pions:
            if self.x >= i.x2 and self.y >= i.x2:
                if self.x +self.dim <= i.x1 and self.y +self.dim <= i.y1:
                    exit(0)
                    
        for i in bordures:
            if self.x >= i.x2 and self.y >= i.x2:
                if self.x +self.dim <= i.x1 and self.y +self.dim <= i.y1:
                    exit(0)
        
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
            
class Bordures():
    def __init__(self,x,y,largeur,hauteur):
        self.x1 =x 
        self.y1 = y
        self.x2 = x + largeur 
        self.y2= y +hauteur
        self.couleur ="gray"
    
