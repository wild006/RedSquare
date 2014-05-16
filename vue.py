class Vue():
    def __init__(self,parent):
        self.parent = parent
        self.root = Tk()
        self.canevas = Canvas(self.root,225,225)

    def afficherEtatJeu(self,carre,pions,bordures):
        self.canevas.delete("carre")
        self.canevas.delete("pions")
        self.canevas.delete("bordures")
        self.canevas.create_rectangle(carre.x,carre.y,carre.x+ carre.dim,carre.y + carre.dim,
                                      fill=carre.couleur,tags ="carre")
        for i in pions:
            self.canevas.create_rectangle(i.x1,i.y1,i.x+ i.x2,i.y2 ,
                                      fill=i.couleur,tags ="pions")
        for i in bordures:
            self.canevas.create_rectangle(i.x1,i.y1,i.x+ i.x2,i.y2 ,
                                          fill=i.couleur,tags ="bordures")

    def bindMouse(self):
        self.canevas.bind("<button-1>", self.parent.click)

    def afficherTemps(self,temps):
        tkMessageBox.showinfo("Score", temps)
    
