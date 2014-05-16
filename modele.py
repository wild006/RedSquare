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
        
    def Jouer(self):
        pass
        #after
        
class Carre():
    def __init__(self):
        self.x = 225 #Selon la doc... Depend de notre grandeur de jeu...
        self.y = 225

        self.couleur = "red"
        self.dim = 30
    
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
    def __init__(self,x,y, largeur, hauteur):
        self.x1 = x #haut/gauche
        self.y1 = y
        self.x2 = x + largeur #bas/droite
        self.y2 = y + hauteur
        self.couleur ="blue"

class Bordures():
    def __init__(self,x,y,largeur,hauteur):
        self.x1 =x 
        self.y1 = y
        self.x2 = x + largeur 
        self.y2= y +hauteur
        self.couleur ="gray"
    
