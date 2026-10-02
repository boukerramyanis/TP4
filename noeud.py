import matplotlib.pyplot as plt 

class Noeud :
    def __init__(self,val,enfant):
        self.val=val
        self.enfant=enfant

    def ajouter_noeud(self,n):
        self.enfant.append(n)

    def affichage_polonais(self):
        print(self.val,end=" ")
        for enf in self.enfant:
            enf.affichage_polonais()

    def evaluer(self, dic):

        if isinstance(self.val, int):
            return float(self.val)

        if isinstance(self.val, float):
            return self.val

        if isinstance(self.val, str):

            if self.val == "+":
                valeur1 = self.enfant[0].evaluer(dic)
                valeur2 = self.enfant[1].evaluer(dic)
                return valeur1 + valeur2

            if self.val == "-":
                valeur1 = self.enfant[0].evaluer(dic)
                valeur2 = self.enfant[1].evaluer(dic)
                return valeur1 - valeur2

            if self.val == "*":
                valeur1 = self.enfant[0].evaluer(dic)
                valeur2 = self.enfant[1].evaluer(dic)
                return valeur1 * valeur2

            if self.val in dic:
                return float(dic[self.val])

            raise ValueError("La variable " + self.val + " n'a pas de valeur")


    def tracer(self, variable, valeurs):
        resultats = []

        for valeur in valeurs:
            dic = {variable: valeur}
            resultats.append(self.evaluer(dic))

        plt.plot(valeurs, resultats)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.show()

        
        


                

                
        

            

