import random


class Pile():
    def __init__(self):
        self.pile = []

    def empiler(self, valeur):
        self.pile.append(valeur)

    def depiler(self):
        val = self.pile.pop()
        return val

    def sommet_pile(self):
        return self.pile[-1]

    def longueur(self):
        return len(self.pile)

    def est_vide(self):
        return len(self.pile) == 0

    def est_present(self, val):
        return val in self.pile


class Case:
    """Class Case qui permet de contenir différentes valeurs

    posn(int): valeur de la position en x
    posm(int): valeur de la position en y
    n(int): représente le 'mur' dans la direction nord (1 = mur | 0 = vide)
    o(int): ''
    s(int): ''
    e(int): ''
    exploree(int): permet de reconnaître si la case à été modifiée
    """

    def __init__(self, Posn, Posm, Nord=1, Ouest=1, Sud=1, Est=1, Exploree=0):
        self.posn = Posn
        self.posm = Posm
        self.n = Nord
        self.o = Ouest
        self.s = Sud
        self.e = Est
        self.exploree = Exploree

    def setNord(self, valeur):
        self.n = valeur

    def setOuest(self, valeur):
        self.o = valeur

    def setSud(self, valeur):
        self.s = valeur

    def setEst(self, valeur):
        self.e = valeur

    def setExploree(self, valeur):
        self.exploree = valeur

    def getNord(self):
        return self.n

    def getOuest(self):
        return self.o

    def getSud(self):
        return self.s

    def getEst(self):
        return self.e

    def getExploree(self):
        return self.exploree

    def getPosn(self):
        return self.posn

    def getPosm(self):
        return self.posm

    def __str__(self):
        str = f"Case{self.posn, self.posm, self.n, self.o, self.s, self.e}"
        return str

    def voisinNord(self, laby):
        """Méthode qui renvoie le voisin, dans la direction voulu, de la case

        Args:
            laby(obj): Labyrinthe contenant toutes les cases

        Returns:
            None: La case ne comporte pas de voisin
            Case(obj): La case de la direction voulu 
        """
        if self.posn == 0:  # Si la coordonnée x est égale à 0 alors la case est "collée" au bord donc elle n'a pas de voisin
            return None
        else:
            return laby[self.posn - 1][self.posm]

    def voisinOuest(self, laby):
        """Méthode qui renvoie le voisin, dans la direction voulu, de la case

        Args:
            laby(obj): Labyrinthe contenant toutes les cases

        Returns:
            None: La case ne comporte pas de voisin
            Case(obj): La case de la direction voulu 
        """
        if self.posm == 0:  # Si la coordonnée y est égale à 0 alors la case est "collée" au bord donc elle n'a pas de voisin
            return None
        else:
            return laby[self.posn][self.posm - 1]

    def voisinSud(self, laby):
        """Méthode qui renvoie le voisin, dans la direction voulu, de la case

        Args:
            laby(obj): Labyrinthe contenant toutes les cases

        Returns:
            None: La case ne comporte pas de voisin
            Case(obj): La case de la direction voulu 
        """
        if self.posn == (len(laby) - 1):  # Si la coordonnée x est égale à la longeur du labyrinthe alors la case est "collée" au bord donc elle n'a pas de voisin
            return None
        else:
            return laby[self.posn + 1][self.posm]

    def voisinEst(self, laby):
        """Méthode qui renvoie le voisin, dans la direction voulu, de la case

        Args:
            laby(obj): Labyrinthe contenant toutes les cases

        Returns:
            None: La case ne comporte pas de voisin
            Case(obj): La case de la direction voulu 
        """
        if self.posm == (len(laby[self.posn]) - 1):  # Si la coordonnée y est égale à la longeur du labyrinthe alors la case est "collée" au bord donc elle n'a pas de voisin
            return None
        else:
            return laby[self.posn][self.posm + 1]

    def voisins(self, laby):
        """Méthode qui renvoie les voisins de la case

        Args:
            laby(obj): Class Labyrinthe contenant toutes les cases

        Returns:
            liste_voisins(list): Liste contenant les voisins de la case
        """
        liste_voisins = []
        if self.voisinNord(laby) != None:
            liste_voisins.append(self.voisinNord(laby))
        if self.voisinOuest(laby) != None:
            liste_voisins.append(self.voisinOuest(laby))
        if self.voisinSud(laby) != None:
            liste_voisins.append(self.voisinSud(laby))
        if self.voisinEst(laby) != None:
            liste_voisins.append(self.voisinEst(laby))
        return liste_voisins


class Labyrinthe:
    def __init__(self, height=2, width=2):
        self.height = height
        self.width = width
        self.cells = []
        for i in range(0, self.height):
            self.cells.append([])
            for j in range(0, self.width):
                self.cells[i].append(Case(i, j))
        creation_laby(self, self.cells[0][0])

    def __str__(self):
        print('__' * (self.width * 2))
        for i in range(self.height):
            ligne = ''
            for j in range(self.width):
                str = ''
                ouest = self.cells[i][j].getOuest()
                nord = self.cells[i][j].getNord()
                est = self.cells[i][j].getEst()
                sud = self.cells[i][j].getSud()

                if ouest == 1:
                    str += '|'
                else:
                    str += ' '
                if sud == 1:
                    str += '__'
                else:
                    str += '  '
                if est == 1:
                    str += '|'
                else:
                    str += ' '
                ligne += str
            print(ligne)
        return ''

    def get_case(self, i, j):
        return self.cells[i][j]

    def affiche(self):
        temp_lab = []
        for i in range(0, self.height):
            temp_lab.append([])
            for j in range(0, self.width):
                temp_lab[i].append(self.cells[i][j].__str__())
        return temp_lab

    def connect(self, case_depart, case_voisin):
        x = case_voisin.getPosn() - case_depart.getPosn()
        y = case_voisin.getPosm() - case_depart.getPosm()

        if x == -1 and y == 0:  # Voisin nord
            case_depart.setNord(0)
            case_voisin.setSud(0)
        elif x == 1 and y == 0:  # Voisin sud
            case_depart.setSud(0)
            case_voisin.setNord(0)
        elif x == 0 and y == -1:  # Voisin ouest
            case_depart.setOuest(0)
            case_voisin.setEst(0)
        else:                      # Voisin est
            case_depart.setEst(0)
            case_voisin.setOuest(0)


def creation_laby(laby, depart):
    visites = []
    p = Pile()
    visites.append(depart)
    p.empiler(depart)
    while not p.est_vide():
        temp = p.sommet_pile()
        voisin = []
        for i in temp.voisins(laby.cells):
            if i not in visites and p.est_present(i) is False:
                voisin.append(i)
        if voisin != []:
            v = random.choice(voisin)
            laby.connect(temp, v)
            visites.append(v)
            v.setExploree(1)
            p.empiler(v)
        else:
            p.depiler()


laby = Labyrinthe(10, 5)
print(laby)
print(laby.affiche())
