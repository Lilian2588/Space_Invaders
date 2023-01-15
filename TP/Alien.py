
"""
    TP SpaceInvaders
    Crée Le 08/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe alien 

"""

#Librairie importée
from tkinter import PhotoImage

#Alien
class alien : 
    #Constructeur
    def __init__(self, vitesse, x, y, taille, apparence) :
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.taille = taille 
        self.apparence = apparence

    #Méthode qui prend en compte la hitbox de l'alien 
    def affiche_hitbox (self, Canevas) : 
        #return Canevas.create_line(self.hitbox[0], self.hitbox[2], self.hitbox[1], self.hitbox[2], fill='white') 
        #liste qui comprends les coordonnées des 4 points du carré entourant l'alien 
        hitbox = [self.x-15, self.y -15, self.x +15, self.x +15, self.x +15, self.y -15, self.x-15, self.y +15]
        return hitbox 
           
    #Méthode qui affiche l'alien selon l'apparence choisis
    def afficher(self, Canevas) :
        '''
            Renvoie l'apparence de l'alien en lui même et sa hitbox qui est le segment inférieur 
        '''
        if self.apparence == 'alien' :
            photo = PhotoImage(file = "Images\\alien.png")
            return Canevas.create_image(20, 20, image = photo)
        if self.apparence == 'oval' :
           alien =  Canevas.create_oval(self.x - 15, self.y - 15 , self.x + 15, self.y + 15, width = self.taille, outline = 'black', fill = 'red')
           return alien 
        '''
            NTE A MOI MEME : ATTRIBUT DANS ALIEN QUI REPRESENTE UNE LISTE DES 3 POINTS DU SEGMENTS AINSI DECRIT 
        '''
    
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
    
    def actualiser_pos(self, RAYON, DX, DY, LARGEUR, Canevas, Mafenetre, forme) :
        if self.shift(RAYON, DX, DY, LARGEUR, Canevas, Mafenetre, forme) : 
            return 4