from tkinter import *

class Vue():
    def __init__(self,parent):
        self.parent = parent
        self.root = Tk()
        self.canevas = Canvas(self.root,width=450,height=450, bg = "white")
        self.canevas.pack()
        self.cliquer = False
        self.bindMouse()

    def afficherEtatJeu(self,carre,pions,bordures):
        self.canevas.delete("carre")
        self.canevas.delete("pions")
        self.canevas.delete("bordures")
        self.canevas.create_rectangle(carre.x,carre.y,carre.x+ carre.dim,carre.y + carre.dim,
                                      fill=carre.couleur,tags ="carre")
        for i in pions:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2 ,
                                      fill=i.couleur,tags ="pions")
        for i in bordures:
            self.canevas.create_rectangle(i.x1,i.y1,i.x1+ i.x2,i.y2 ,
                                          fill=i.couleur,tags ="bordures")
        

    def bindMouse(self):
        self.canevas.bind("<Button-1>", self.click)
        self.canevas.bind("<B1-Motion>", self.dragged)
        print("lol")

    def click(self,event):
        self.curseurPosX = event.x
        self.curseurPosY = event.y
        print(event.x, " ", event.y)
        #A CHANGER DE PLACE.... POUR TEST !
        self.parent.commencerPartie()
        self.parent.jouer()
        
    def dragged(self,event):
        self.parent.changementPosCarre(event,self.curseurPosX,self.curseurPosY)
        self.curseurPosX = event.x
        self.curseurPosY = event.y


    def afficherTemps(self,temps):
        tkMessageBox.showinfo("Score", temps ,)
    
