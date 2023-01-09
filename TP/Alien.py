
"""
    TP4
    Crée Le 08/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe alien 
               - implémentation de la classe alien

"""

from tkinter import PhotoImage

#Alien
class alien : 
    def __init__(self, vitesse, x, y, taille, apparence) :
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.taille = taille 
        self.apparence = apparence

    def afficher(self, Canevas) :
        if self.apparence == 'alien' :
            photo = PhotoImage(file = "Images\\alien.png")
            return Canevas.create_image(20, 20, image = photo)
        if self.apparence == 'oval' :
           return Canevas.create_oval(self.x - 15, self.y - 15 , self.x + 15, self.y + 15, width = self.taille, outline = 'black', fill = 'red') 
    
    def shift(self, RAYON, DX, DY, LARGEUR, Canevas, Mafenetre, forme) :
        """Déplacement des aliens""" 
        #Gestion des collisions 
        #aller-retour à droite
        if self.x + RAYON + DX > LARGEUR : 
            self.x = 2*(LARGEUR - RAYON) - self.x
            DX = - DX

        #Aller-retour à gauche
        if self.x - RAYON + DX < 0 : 
            self.x = 2*RAYON - self.x 
            DX = - DX

        self.x = self.x + DX
        self.y = self.y + DY
        #Actualisation des coordonnées de l'alien
        Canevas.coords(forme, self.x - RAYON, self.y - RAYON, self.x + RAYON, self.y + RAYON)
        Mafenetre.after(25, lambda : self.shift(RAYON, DX, DY, LARGEUR, Canevas, Mafenetre, forme))
    