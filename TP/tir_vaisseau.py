"""
    TP4
    Crée Le 09/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe tir du vaisseau 
               - implémentation de la classe tir du vaisseau 

"""


#Tir du vaisseau
class missile_vaisseau:
    def __init__(self, x, y, apparence):
        self.x = x
        self.y = y
        self.apparence = apparence
      
    def afficher(self, Canevas):
        Canevas.create_line(self.x , self.y-4 , self.x ,self.y , opacity = "1", fill='white')

    def deplacement(self, Canevas, Mafenetre):
        self.y -= 5
        Canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        Mafenetre.after(20, self.deplacement)
        
    def destruction(self, Canevas):
        points = 0
        if self.y < 0:
            Canevas.delete(self.apparence)
        else:
            if self.y >= alien.y and self.y <= alien.x + 30 and self.x <= alien.x + 30 and self.x >= alien.x :
                Canevas.delete(self.apparence)
                Canevas.delete(alien)
                points += 1
