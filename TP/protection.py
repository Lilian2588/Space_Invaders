
"""
    TP SpaceInvaders
    Crée Le 14/01/2023
    Réalisé par Glemet Augustin et Saglibene Lilian 
    Objectif : - création de fichier unique pour la classe protection

"""
#déclaration des variables permettant de dimensionner les protections
largeur = 40
hauteur = 15

class Protections:
    pos = 0
    #constructeur
    def __init__(self,width,nbre_protections,posYprotections,resistance):
        Protections.pos += 1
        self.pos = Protections.pos
        self.x = width*self.pos/(nbre_protections+1)
        Protections.y = posYprotections
        self.Resistance = resistance
    #Méthode permettant d'afficher les protections
    def affichage(self,canevas)  :
        self.Apparence = canevas.create_rectangle(self.x,self.y,self.x+largeur,self.y+hauteur,width=2,outline='purple',fill='white')
        self.VieProtection = canevas.create_text(self.x+largeur/2,self.y+hauteur/2,text=str(self.Resistance),fill='red')
    #Méthode qui permet de mettre à jour la resistance de la protection en cas d'impact
    def Update(self,canevas):
        self.Resistance -= 1
        if self.Resistance>0:
            canevas.itemconfig(self.VieProtection,text = (str(self.Resistance)))
        else:
            self.Destruction()
    #Méthode qui permet de faire disparaitre  la protection dans le cas où sa résistance atteint 0 
    def Destruction(self,canevas):
        canevas.delete(self.Apparence)
        canevas.delete(self.VieProtection)
