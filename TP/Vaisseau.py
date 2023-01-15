
"""
    TP SpaceInvaders
    Crée Le 08/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe vaisseau 

"""

#Librairie importée
from tkinter import PhotoImage

#Vaisseau
class vaisseau: 
    #Constructeur
    def __init__(self, vitesse, PosX, PosY, vie, apparence) :
        self.vitesse = vitesse
        self.PosX = PosX
        self.PosY = PosY
        self.vie = vie 
        self.apparence = apparence 

    #Méthode qui affiche le vaisseau selon l'apparence choisis 
    def affichage(self, Canevas) :
        if self.apparence == 'oval' : 
             return Canevas.create_oval(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width=3, outline='black', fill='blue')
        if self.apparence == 'rectangle' : 
            return Canevas.create_rectangle(self.PosX, self.PosY, self.PosX -10, self.PosY -10, fill = 'blue', width = 3, outline = 'black')
        #apparence de vaisseau choisis : implémentation d'une image sur le vaisseau
        if self.apparence == 'vessel' : 
            photo = PhotoImage(file = "Images\\r_space_vessel.png")
            return Canevas.create_image(20, 20, image = photo)
        
    #Méthode qui fait perdre des vies au joueur au contact des missiles des aliens
    def vie_perdu(self) :
        ''' 
        if 
        '''
        self.vie -= 1
    
        
