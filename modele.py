class Modele():
    def __init__(self, parent):
        self.parent = parent
        #Mettre les options
    
    def commencerPartie(self):
        self.p = Partie(self)
        #Initialiser le carre
        
    
class Partie():
    def __init__(self, parent):
        print("Partie")
        self.parent = parent
    
    def Jouer(self):
        pass
        #after
    