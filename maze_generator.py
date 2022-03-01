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

    def __str__(self):
        str = f"Case{self.posn, self.posm, self.n, self.o, self.s, self.e}"
        return str

    def voisinNord(self, laby):
        if self.posn == 0:
            return None
        else:
            return laby[self.posn - 1][self.posm]

    def voisinOuest(self, laby):
        if self.posm == 0:
            return None
        else:
            return laby[self.posn][self.posm - 1]

    def voisinSud(self, laby):
        if self.posn == (len(laby) - 1):
            return None
        else:
            return laby[self.posn + 1][self.posm]

    def voisinEst(self, laby):
        if self.posm == (len(laby[self.posn]) - 1):
            return None
        else:
            return laby[self.posn][self.posm + 1]

    def voisins(self, laby):
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

    def est_bloque(self, laby):
        tmp = 0
        for i in self.voisins(laby):
            if i.getExploree() == 1:
                tmp += 1
        if tmp == len(self.voisins(laby)):
            return True
        else:
            return False


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
            up = ''
            down = ''
            for j in range(self.width):
                str_up = ''
                str_down = ''
                ouest = self.cells[i][j].getOuest()
                nord = self.cells[i][j].getNord()
                est = self.cells[i][j].getEst()
                sud = self.cells[i][j].getSud()

                if ouest == 1:
                    str_down += '|'
                else:
                    str_down += ' '
                if sud == 1:
                    str_down += '__'
                else:
                    str_down += '  '
                if est == 1:
                    str_down += '|'
                else:
                    str_down += ' '

                # up += str_up
                down += str_down
            # print(up)
            print(down)
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

    def casser_murs(self, depart):
        mur_a_casser = random.randint(1, 4)
        if mur_a_casser == 1:
            res = depart.voisinNord(self.cells)
            if res == None or res.exploree == 1 and self.toutes_explorees() is False:
                self.casser_murs(depart)
            else:
                depart.setNord(0)
                res.setSud(0)
        elif mur_a_casser == 2:
            res = depart.voisinOuest(self.cells)
            if res == None or res.exploree == 1 and self.toutes_explorees() is False:
                self.casser_murs(depart)
            else:
                depart.setOuest(0)
                res.setEst(0)
        elif mur_a_casser == 3:
            res = depart.voisinSud(self.cells)
            if res == None or res.exploree == 1 and self.toutes_explorees() is False:
                self.casser_murs(depart)
            else:
                depart.setSud(0)
                res.setNord(0)
        else:
            res = depart.voisinEst(self.cells)
            if res == None or res.exploree == 1 and self.toutes_explorees() is False:
                self.casser_murs(depart)
            else:
                depart.setEst(0)
                res.setOuest(0)

    def toutes_explorees(self):
        for tab in self.cells:
            for case in tab:
                if case.getExploree() == 0:
                    return False
        return True


def creation_laby(laby, depart):
    visites = []
    fermes = []
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
            if v.est_bloque(laby.cells) == True:
                pass
            else:
                laby.casser_murs(v)
            visites.append(v)
            v.setExploree(1)
            p.empiler(v)
        else:
            fermes.append(temp)
            p.depiler()


laby = Labyrinthe(10, 10)
print(laby)
print(laby.affiche())
