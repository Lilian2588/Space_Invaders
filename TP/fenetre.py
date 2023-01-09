"""
    TP4
    Crée Le 05/12/2022
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - créer le canvas 
               - implémentation des types de données
    modifié le 08/01/23

"""

from tkinter import Tk, Button, Canvas, PhotoImage
import math
from Vaisseau import vaisseau
from Alien import alien

Mafenetre = Tk()
bg = PhotoImage(file = "Images\\universe.png") 
Mafenetre['bg'] = 'grey'
Mafenetre.title('Space Invader')
Canevas = Canvas(Mafenetre, height = 460,  width= 640)
Canevas.pack()
Canevas_Image = Canevas.create_image(0, 0, image = bg, anchor = "nw")
Buttonstart = Button(Mafenetre,text = "quit", command = Mafenetre.destroy)
Buttonstart.pack(side = "right", padx = 10, pady = 10)
Boutonquit = Button(Mafenetre, text =  'New Game', command = Canevas.destroy)
Boutonquit.pack(side = "right", padx = 10, pady = 10)

#Dimensions du canvas
LARGEUR = 640 
HAUTEUR = 460
#Rayon utilisé pour la taille du vaisseau
RAYON = 15

#Position initale des aliens
X = 320
Y = 50

#Vitesse des aliens et du vaisseau
vitesse = 3 
#Angle pour se faire déplacer horizontalement (-pi) (pi/2 : déplacement vertical)
angle = - math.pi 

#Petit déplacement des aliens et du vaisseau liés a la vitesse définie avant 
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)

#Position initiale du vaisseau
PosX = LARGEUR/2
PosY = 370

Canevas.focus_set()
#Création de l'entité du vaisseau et affichage de sa forme 
Vaisseau = vaisseau(vitesse, PosX, PosY, 3, 'vessel')
affich_vaisseau = Vaisseau.affichage(Canevas) 

'''
#Création des aliens et affichages de leur formes
Alien = alien(vitesse, X, Y, 1, 'oval')
affich_alien = Alien.afficher(Canevas)
#Alien.shift(Canevas, Mafenetre)
'''
'''
#Tir des Aliens
class missile_alien :
    def __init__(self, x, y, apparence):
        self.x = x
        self.y = y
        self.apparence = apparence
    
    def afficher(self) :
        Canevas.coords(self.apparence, self.x, self.y+4, self.x, self.y)

    def deplacement(self):
        self.y += 5
        self.afficher()
        Mafenetre.after(20, self.deplacement)
    
    def touche_vaisseau(self) : 
        vaisseau.vie_perdu

#Tir du vaisseau
class missile_vaisseau:
    def __init__(self, x, y, apparence):
        self.x = x
        self.y = y
        self.apparence = apparence
        #Canevas.create_line(self.x , self.y-4 , self.x ,self.y , opacity = "1", fill='white')
      
    def afficher(self):
        Canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)

    def deplacement(self):
        self.y -= 5
        self.afficher()
        Mafenetre.after(20, self.deplacement)
        
    def destruction(self):
        points = 0
        if self.y < 0:
            Canevas.delete(self.apparence)
        else:
            if self.y >= alien.y and self.y <= alien.x + 30 and self.x <= alien.x + 30 and self.x >= alien.x :
                Canevas.delete(self.apparence)
                Canevas.delete(alien)
                points += 1

'''

"""
block1 = Canevas.create_rectangle(random(100,400), random(100,400), random(100,400), random(100,400), width= 1, outline = 'blue', fill= 'green')
block2 = Canevas.create_rectangle(random(100,400), random(100,400), random(100,400), random(100,400), width= 2, outline = 'blue', fill= 'green')
block3 = Canevas.create_rectangle(random(100,400), random(100,400), random(100,400), random(100,400), width= 3, outline = 'blue', fill= 'green')
"""

#Fonction de binding des touches 
def Clavier(event) : 
    #Création des postions du vaiseau    
    global PosX, PosY, LARGEUR, HAUTEUR
    touche = event.keysym
    #On délimite la fenêtre par la Largeur ainsi défini au début - nombre de pixel auquel se déplace le vaisseau pour que le vaisseau ne déborde pas du canvas
    if PosX > 20 and PosX < LARGEUR - 20 : 
        #Le point en haut a gauche du canvas à pour coord (0px, 0px)
        if touche == 'd' or touche == 'Right' :
            # On diminue la position horizontale du vaisseau de 20 px
            PosX += 20
        if touche == 'q' or touche == 'Left' :
            # On augmente la position Horizontale du vaisseau de 20 px
            PosX -= 20 
    #Limite de Bordure, si le vaisseau se trouve au bord, lui imposé qu'un seul déplacement possible ( au bord a gauche, lui imposé d'aller a droite)
    if PosX == LARGEUR - 20  : 
        if touche == 'q' or touche == 'Left' : 
            PosX -= 20 
    #Limite de Bordure, si le vaisseau se trouve au bord, lui imposé qu'un seul déplacement possible ( au bord a droite, lui imposé d'aller a gauche)
    if PosX == 20 :
        if touche == 'd' or touche == 'Right' : 
            PosX += 20
    '''
    if touche == 'Backspace' : 
        #tir_missile_vaisseau()
    '''
    #Mise a jour des coordonnées du vaisseau 
    Canevas.coords(affich_vaisseau, PosX -10, PosY -10, PosX +10, PosY +10)

#On attribut les touches du clavier
Canevas.bind('<Key>', Clavier)  

Mafenetre.mainloop()