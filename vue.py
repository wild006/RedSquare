# Fait par Alexandre Laplante-Turpin et Francois Genest

from tkinter import *
import tkinter.messagebox as messagebox
from modele import Niveau
import re

class Vue():
    def __init__(self,parent):

        self.parent = parent
        self.root = Tk()
        self.canevas = Canvas(self.root,width=self.parent.getGrandeurJeuX(),height=self.parent.getGrandeurJeuY(), bg = "white")
        self.canevas.pack()
        self.cliquer = False
        self.premierClick = False
        self.cbVar = BooleanVar()
        self.cbModif = Checkbutton(self.root,text="Modificateur",variable=self.cbVar)
        if self.parent.getPowerUp() == True:
            self.cbModif.select()
            print(self.parent.getPowerUp())
        
        self.bgImage= PhotoImage(file="Menu.gif")
        self.labelNbPointage = Label(self.root, text="Nombre de pointage sauvegarder" )        

        self.labelOptionInvalide = Label(self.root,text="",fg="red")
        self.boutonJouer = Button(text= "Jouer",width =9,command = self.jouerOptions)
        self.boutonOptions = Button(text= "Options",width =9,command = self.afficherOptions)
        self.boutonScores = Button(text= "Pointages",width =9, command = self.afficherHighscores)
        self.boutonCredits = Button(text= "Crédits",width =9, command = self.afficherCredits)
        self.boutonQuitter = Button(text= "Quitter",width =9, command = self.quitter)
        self.boutonRetour = Button(text= "Retour au Menu",width =14, command = self.menu)
        self.boutonConfirmer = Button(text= "Confirmer",width =14, command = self.changerOptions)
        self.labelScore = Label(self.root,text="Pointage de la session", relief= "groove", width=20)
        self.labelHScore = Label(self.root,text="Meilleur pointage", relief= "groove",width=20)
        self.entreeNbPointage = Entry(width=5)
        self.lbScore = Listbox(self.root,width=25,height=5)
        self.lbHscore =Listbox(self.root,width=25,height=5)
        self.entreeNbPointage.delete(0,END)
        self.entreeNbPointage.insert(0,3)

        self.menu()

        self.entreeNbPointage.delete(0,END)
        self.entreeNbPointage.insert(0,self.parent.getNbSauvegarde())
        

        



    def afficherEtatJeu(self,carre,pions,bordures,powerUps):
        self.canevas.delete("carre")
        self.canevas.delete("pions")
        self.canevas.delete("power")
        self.canevas.delete("bordures")
        self.carre = self.canevas.create_rectangle(carre.x,carre.y,carre.x+ carre.dim,carre.y + carre.dim,
                                      fill=carre.couleur,tags ="carre")
        for i in bordures:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2 ,
                                          fill=i.couleur,tags ="bordures")
        for i in pions:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2 ,
                                      fill=i.couleur,tags ="pions")
        for i in powerUps:
            self.canevas.create_oval(i.x1,i.y1,i.x2,i.y2 ,
                                      fill=i.couleur,tags ="power")


    def bindMouse(self):
        self.canevas.bind("<Button-1>", self.click)
        self.canevas.bind("<B1-Motion>", self.dragged)
        self.canevas.bind("<ButtonRelease-1>", self.clickRelease)
        
    def unbindMouse(self):
        self.canevas.unbind("<Button-1>")
        self.canevas.unbind("<B1-Motion>")
        self.canevas.unbind("<ButtonRelease-1>")

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
                    self.parent.jouer()

        
    def dragged(self,event):
        if self.cliquer :
            self.parent.changementPosCarre(event,self.curseurPosX,self.curseurPosY)
            self.curseurPosX = event.x
            self.curseurPosY = event.y


    def afficherTemps(self,temps):
        self.premierClick = False
        messagebox.showinfo("Partie Terminée", "Votre temps est  " + "%.3f" % (temps) + " secondes !" )
        
    def saveWindows(self):
        self.saveWindow = Toplevel(self.root)
        self.saveWindow.transient(self.root)
        self.labelSauvegarde  = Label(self.saveWindow,text= "Veillez entrer vos informations pour sauvegarder votre score" )
        boutonSauvegarder = Button(self.saveWindow, text = "Sauvegarder et rejouer", command = self.sauvegarder, width =30)
        boutonSauveQuitter = Button(self.saveWindow, text = "Sauvegarder et revenir au menu", command = self.sauvegarderQuitter,width =30 )
        self.labelSauvegarde.pack()
        self.texte = Entry(self.saveWindow, width =25)
        self.texte.pack()
        boutonSauvegarder.pack()
        boutonSauveQuitter.pack()
        self.saveWindow.grab_set()
        self.root.wait_window(self.saveWindow)
        self.parent.commencerPartie(self.parent.getDernierNiveau())


    def sauvegarderQuitter(self):
        self.sauvegarder()
        self.unbindMouse()
        self.menu()
        
        
    def sauvegarder(self):
        self.parent.sauvegarderHighscore(self.texte.get())
        self.saveWindow.destroy()

    
    def commencerPartie(self,difficulte):
        self.canevas.delete("jouerOptions")
        self.canevas.delete("bg")
        self.bindMouse()
        self.parent.commencerPartie(difficulte)

    def afficherOptions(self):
        self.canevas.delete("menu")
        self.canevas.create_window(230,75,window=self.labelOptionInvalide ,tags="options")
        self.canevas.create_window(150,100,window= self.cbModif, tags="options")
        self.canevas.create_window(140,150,window= self.entreeNbPointage, anchor=E, tags="options")
        self.canevas.create_window(140,150,window= self.labelNbPointage, anchor=W, tags="options")
        self.canevas.create_window(100,400,window= self.boutonRetour,tags="options")
        self.canevas.create_window(360,400,window= self.boutonConfirmer,tags="options")

    def changerOptions(self):
        try:
            self.parent.changerOptions(self.cbVar.get(),int(self.entreeNbPointage.get()))
            self.labelOptionInvalide.config(text="Les options ont été sauvegardées",fg="green")
        except:
            self.labelOptionInvalide.config(text="Une donné est invalide", fg = "red")
            
    def afficherHighscores(self):
        self.canevas.delete("menu")

        self.lbScore.delete(0,END)
        self.lbHscore.delete(0,END)
        hscore = self.parent.getScore()
        score = self.parent.getScoreSession()
        
        difficulte = "facile"
        Modif = "Modif"
        for i in range(hscore.__len__()):
            if hscore[i][2]== 0:
                difficulte = "Facile"
            elif hscore[i][2]== 1:
                difficulte = "Classique"
            elif hscore[i][2]== 2:
                difficulte = "Expert"

            if hscore[i][3]:
                Modif = "Modif"
            else:
                Modif = "Sans Modif"
                
            self.lbHscore.insert(i, hscore[i][0] + "   " + "%.3f" % round(hscore[i][1],3)+ " | " +difficulte +" " + Modif)

        for i in range(score.__len__()):
            if score[i][2]== 0:
                difficulte = "Facile"
            elif score[i][2]== 1:
                difficulte = "Classique"
            elif score[i][2]== 2:
                difficulte = "Expert"

            if score[i][3]:
                Modif = "Modif"
            else:
                Modif = "Sans Modif"
            self.lbScore.insert(i,score[i][0] + "   " +  "%.3f" % round(score[i][1],3)+ " | " +difficulte +" " + Modif)
            

        self.canevas.create_window(120,150,window =self.labelScore,anchor=S)
        self.canevas.create_window(340,150,window =self.labelHScore,anchor=S)
        self.canevas.create_window(120,150,window =self.lbScore,anchor=N)
        self.canevas.create_window(340,150,window =self.lbHscore, anchor=N)
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="scores")

    def afficherCredits(self):
        self.canevas.delete("menu")
        labelNomAlex = Label(text = "Alexandre Lplante-Turpin")
        labelNomFrancois = Label(text  = "François Genest")
        self.canevas.create_window(230,100,window=labelNomFrancois,tags="credits")
        self.canevas.create_window(230,125,window=labelNomAlex,tags="credits")
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="credits")

    def jouerOptions(self):
        self.canevas.delete("menu")
        self.boutonFacile = Button(text="Facile", command = lambda : self.commencerPartie(Niveau.facile),  width=10)
        self.boutonClassique = Button(text="Classique", command = lambda : self.commencerPartie(Niveau.classique),  width=10)
        self.boutonExpert = Button(text="Expert", command = lambda : self.commencerPartie(Niveau.expert), width=10)
        self.canevas.create_window(230,150,window= self.boutonFacile, tags="jouerOptions")
        self.canevas.create_window(230,200,window= self.boutonClassique, tags="jouerOptions")
        self.canevas.create_window(230,250,window= self.boutonExpert, tags="jouerOptions")
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="jouerOptions")
        
    def quitter(self):
        exit(0)
        
    def menu(self):
        self.canevas.delete("all")
        self.labelOptionInvalide.config(text="")
        self.canevas.create_image(0,0,image=self.bgImage,anchor=NW ,tags="bg" )
        self.canevas.create_window(230,125,window = self.boutonJouer,tags="menu")
        self.canevas.create_window(230,175,window = self.boutonScores,tags="menu")
        self.canevas.create_window(230,225,window = self.boutonOptions,tags="menu")
        self.canevas.create_window(230,275,window = self.boutonCredits,tags="menu")
        self.canevas.create_window(230,325,window = self.boutonQuitter,tags="menu")
        

