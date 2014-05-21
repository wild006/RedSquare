from tkinter import *
import tkinter.messagebox as messagebox

class Vue():
    def __init__(self,parent):
        self.parent = parent
        self.root = Tk()
        self.saveWindows(15)
        self.canevas = Canvas(self.root,width=self.parent.getGrandeurJeuX(),height=self.parent.getGrandeurJeuY(), bg = "white")
        self.canevas.pack()
        self.cliquer = False
        self.permierClick = False
        self.bindMouse()

    def afficherEtatJeu(self,carre,pions,bordures):
        self.canevas.delete("carre")
        self.canevas.delete("pions")
        self.canevas.delete("bordures")
        self.carre = self.canevas.create_rectangle(carre.x,carre.y,carre.x+ carre.dim,carre.y + carre.dim,
                                      fill=carre.couleur,tags ="carre")
        for i in bordures:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2 ,
                                          fill=i.couleur,tags ="bordures")
        for i in pions:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2 ,
                                      fill=i.couleur,tags ="pions")


    def bindMouse(self):
        self.canevas.bind("<Button-1>", self.click)
        self.canevas.bind("<B1-Motion>", self.dragged)
        self.canevas.bind("<ButtonRelease-1>", self.clickRelease)

    def clickRelease(self,event):
        self.cliquer = False

    def click(self,event):
        clicke = self.canevas.find_withtag("current")
        for i in clicke :
            if i == self.carre:  
                self.curseurPosX = event.x
                self.curseurPosY = event.y
                self.cliquer = True
                if not self.premierClick :
                    self.premierClick = True
                    self.controleur.jouer()

        
    def dragged(self,event):
        if self.cliquer :
            self.parent.changementPosCarre(event,self.curseurPosX,self.curseurPosY)
            self.curseurPosX = event.x
            self.curseurPosY = event.y


    def afficherTemps(self,temps):
        messagebox.showinfo("Score", "Votre temps est : " + temps.__str__() )
        
    def saveWindows(self,temps):
        saveWindow = Toplevel(self.root)
        label  = Label(saveWindow,text="Veillez entrer vos informations pour sauvegarder votre score")
        boutonSauvegarder = Button(saveWindow, text="Sauvegarder")

        

