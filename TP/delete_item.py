"""
    TP SpaceInvaders
    Crée Le 05/12/2022
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - créer le canvas 
               - implémentation des types de données
"""

#Fonction qui compare si la hitbox du premier item se touche avec la hitbox du second item et si oui supprime les deux items
def suppression_items(item1, item2, posx_item1, posy_item1, taille_item1, posx_item2, posy_item2, taille_item2, Canevas) :
    
    #Si l'item1 arrive par le bas à droite par rapport à l'item2 
    if posx_item1 >= posx_item2 and posy_item1 >= posy_item2 :
        #On compare leur hitbox selon leur postion relative entre eux
        if  posx_item1 - taille_item1 <= posx_item2 + taille_item2  and posy_item1 - taille_item1 <= posy_item2 + taille_item2 :
            #supprime les deux éléments
            Canevas.delete(item1,item2)
    #Si l'item1 arrive par le bas à gauche par rapport à l'item2
    if posx_item1 <= posx_item2 and posy_item1 >= posy_item2 :
        if  posx_item1 + taille_item1 >= posx_item2 - taille_item2  and posy_item1 - taille_item1 <= posy_item2 + taille_item2 :
            Canevas.delete(item1,item2)
    #Si l'item1 arrive par le haut à gauche par rapport à l'item2
    if posx_item1 <= posx_item2 and posy_item1 <= posy_item2 :
        if  posx_item1 + taille_item1 >= posx_item2 - taille_item2  and posy_item1 + taille_item1 >= posy_item2 - taille_item2 :
            Canevas.delete(item1,item2)
    #Si l'item1 arrive par le haut à gauche par rapport à l'item2
    if posx_item1 >= posx_item2 and posy_item1 <= posy_item2 :
        if  posx_item1 - taille_item1 <= posx_item2 + taille_item2  and posy_item1 + taille_item1 >= posy_item2 - taille_item2 :
            Canevas.delete(item1,item2)
    #On rappelle la fonction toutes les 20ms

