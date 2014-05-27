from tkinter import *
import tkinter.messagebox as messagebox

class Vue():
    def __init__(self,parent):

        self.parent = parent
        self.root = Tk()
        self.canevas = Canvas(self.root,width=self.parent.getGrandeurJeuX(),height=self.parent.getGrandeurJeuY(), bg = "white")
        self.canevas.pack()
        self.cliquer = False
        self.premierClick = False
        self.bgImage= PhotoImage(file="Menu.gif")
        self.boutonJouer = Button(text= "Jouer",width =9,command = self.commencerPartie)
        self.boutonOptions = Button(text= "Options",width =9,command = self.afficherOptions)
        self.boutonScores = Button(text= "Scores",width =9, command = self.afficherHighscores)
        self.boutonCredits = Button(text= "Crédits",width =9, command = self.afficherCredits)
        self.boutonQuitter = Button(text= "Quitter",width =9, command = self.Quitter)
        self.boutonRetour = Button(text= "Retour au Menu",width =14, command = self.Menu)
        self.Menu()


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
        messagebox.showinfo("Score", "Votre temps est  " + "%.3f" % round(temps,3) + " secondes !" )
        
    def saveWindows(self):
        self.parent.commencerPartie()
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

    def sauvegarderQuitter(self):
        self.sauvegarder()
        self.unbindMouse()
        self.Menu()
        
        
    def sauvegarder(self):
        self.parent.sauvegarderHighscore(self.texte.get())
        self.saveWindow.destroy()

    
    def commencerPartie(self):
        self.canevas.delete("menu")
        self.canevas.delete("bg")
        self.bindMouse()
        self.parent.commencerPartie()

    def afficherOptions(self):
        self.canevas.delete("menu")
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="options")

    def afficherHighscores(self):
        self.canevas.delete("menu")
        self.lbScore = Listbox(self.root,width=15,height=5)
        self.lbHScore =Listbox(self.root,width=15,height=5)
        
        Hscore = self.parent.getScore()
        score = self.parent.getScoreSession()
        
        for i in range(score.__len__()):
            self.lbHScore.insert(i, score[i][0] + "   " + score[i][1])

        for i in range(Hscore.__len__()):
            self.lbScore.insert(i,Hscore[i][0] + "   " + Hscore[i][1])

        self.labelScore = Label(self.root,text="Score de la session", relief= "groove", width=16)
        self.labelHScore = Label(self.root,text="MeilleurScore", relief= "groove",width=16)
        self.canevas.create_window(120,150,window =self.labelScore,anchor=S)
        self.canevas.create_window(340,150,window =self.labelHScore,anchor=S)
        self.canevas.create_window(120,150,window =self.lbScore,anchor=N)
        self.canevas.create_window(340,150,window =self.lbHScore, anchor=N)
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="scores")

    def afficherCredits(self):
        self.canevas.delete("menu")
        labelNomAlex = Label(text = "Alexandre Lplante-Turpin")
        labelNomFrancois = Label(text  = "François Genest")
        self.canevas.create_window(230,100,window=labelNomFrancois,tags="credits")
        self.canevas.create_window(230,125,window=labelNomAlex,tags="credits")
        self.canevas.create_window(230,400,window= self.boutonRetour,tags="credits")
        
    def Quitter(self):
        exit(0)
        
    def Menu(self):
        self.canevas.delete("all")
        self.canevas.create_image(0,0,image=self.bgImage,anchor=NW ,tags="bg" )
        self.canevas.create_window(230,125,window = self.boutonJouer,tags="menu")
        self.canevas.create_window(230,175,window = self.boutonScores,tags="menu")
        self.canevas.create_window(230,225,window = self.boutonOptions,tags="menu")
        self.canevas.create_window(230,275,window = self.boutonCredits,tags="menu")
        self.canevas.create_window(230,325,window = self.boutonQuitter,tags="menu")
        

