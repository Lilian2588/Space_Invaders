"""
    TP SpaceInvaders
    Crée Le 09/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe tir du vaisseau  

"""
#Librairies et fonctions importées
from delete_item import suppression_items

#Tir du vaisseau
class missile_vaisseau:
    #Constructeur
    def __init__(self, x, y, vitesse):
        self.x = x
        self.y = y
        self.vitesse = vitesse

    #Méthode qui affiche l'apparence du missile
    def afficher(self, Canevas):
        #Affichage du missile au dessus de la tête du vaisseau 
        return Canevas.create_rectangle (self.x , self.y -15, self.x  , self.y -8, width = 4, fill='black')
    

    #Méthode qui fait déplacer le missile verticalement vers le haut
    def deplacement(self, forme_missile, affich_alien, Canevas, Mafenetre, posx_alien, posy_alien, taille_alien):
            
        #forme_missile correspond à l'apparence du missile, si c'est un rectangle, un oval, une image... 
        #On fait monter le missile en jouant sur l'axe vertical y
        self.y -= 5
        #On actualise les coordonnées du missile
        Canevas.coords(forme_missile, self.x, self.y-15 , self.x, self.y-8)
        #Condition si le missile dépasse le cadre de la fenêtre
        if self.y < 15 : 
            Canevas.delete(forme_missile)
        '''
        suppression_items(forme_missile, affich_alien, self.x, self.y, 3, posx_alien, posy_alien, taille_alien, Canevas)
        print(posx_alien)
        print(posy_alien)
        '''
        #On rappelle la fonction après une certaine durée qui dépend de la vitesse du missile
        Mafenetre.after(self.vitesse*10, lambda : self.deplacement(forme_missile, affich_alien, Canevas, Mafenetre, posx_alien, posy_alien, taille_alien))
        
    
    
