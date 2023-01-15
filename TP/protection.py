from Vaisseau import vaisseau
largeur=10
hauteur=15
class Protections:
    def __init__(self,width,nbre_protections,posYprotections,resistance):
        self.x=width*self.Compteur/(nbre_protections+1)
        Protections.y=posYprotections
        self.Resistance=resistance
        
    def affichage(self,canevas)  :
        self.Apparence=canevas.create_rectangle(self.x,self.y,self.x+largeur,self.y+hauteur,width=2,outline='purple',fill='white')
        self.VieProtection=canevas.create_text(self.x+largeur/2,self.y+hauteur/2,text=str(self.Resistance),fill='red')
        
    def Update(self,canevas):
        self.Resistance-=1
        if self.Resistance>0:
            canevas.itemconfig(self.VieProtection,text=(str(self.Resistance)))
        else:
            self.Destruction()
    
    def Destruction(self,canevas):
        canevas.delete(self.Apparence)
        canevas.delete(self.VieProtection)
