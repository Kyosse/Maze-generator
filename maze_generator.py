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
        return f"Case{self.posn, self.posm, self.n, self.o, self.s, self.e}"

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
        self.toutes_lignes = []
        for i in range(0, self.height):
            self.cells.append([])
            for j in range(0, self.width):
                self.cells[i].append(Case(i, j))
        self.creation_laby(self.cells[0][0])

    def entree_sortie(self, x, y, direction):
        case = self.cells[x][y]
        if direction == "Ouest":
            case.setOuest(0)
        else:
            case.setEst(0)

    def creation_laby(self, depart):
        visites = []
        p = Pile()
        visites.append(depart)
        p.empiler(depart)
        while not p.est_vide():
            temp = p.sommet_pile()
            voisin = []
            for i in temp.voisins(self.cells):
                if i not in visites and p.est_present(i) is False:
                    voisin.append(i)
            if voisin != []:
                v = random.choice(voisin)
                self.connect(temp, v)
                visites.append(v)
                v.setExploree(1)
                p.empiler(v)
            else:
                p.depiler()

    def get_visuel(self):
        self.toutes_lignes.append('___' * (self.width))
        for i in range(self.height):
            ligne = ''
            for j in range(self.width):
                str = ''
                ouest = self.cells[i][j].getOuest()
                sud = self.cells[i][j].getSud()

                if ouest == 1:
                    str += '|'
                else:
                    str += ' '
                if sud == 1:
                    str += '__'
                else:
                    str += '  '
                ligne += str
            ligne += '|'
            self.toutes_lignes.append(ligne)
        return self.toutes_lignes

    def __str__(self):
        self.get_visuel()
        for ligne in self.toutes_lignes:
            print(ligne)
        return ''

    def affiche_valeur(self):
        temp_laby = []
        for i in range(0, self.height):
            temp_laby.append([])
            for j in range(0, self.width):
                temp_laby[i].append(self.cells[i][j].__str__())
        return temp_laby

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

    def write_svg(self, filename):
        """Write an SVG image of the maze to filename."""

        aspect_ratio = self.height / self.width
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.width, width / self.height

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""

            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
                  .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).

            for x in range(self.height):
                for y in range(self.width):

                    if self.cells[x][y].getEst() == 1:

                        x1 = x * scx
                        y1 = (y + 1) * scy
                        x2 = (x + 1) * scx
                        y2 = (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)

                    if self.cells[x][y].getSud() == 1:

                        x1, y1, x2, y2 = (x + 1) * scx, y * \
                            scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)

            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            print('</svg>', file=f)


def laby_web(longueur, largeur, val_dep, val_arrivee):
    laby = Labyrinthe(longueur, largeur)
    laby.entree_sortie(val_dep, 0, "Ouest")
    laby.entree_sortie(val_arrivee, len(largeur), "Est")
    laby.write_svg("website/static/images/maze_web.svg")
    return laby.get_visuel()


laby = Labyrinthe(10, 10)
print(laby)
laby.write_svg("maze.svg")
print(laby.affiche_valeur())
