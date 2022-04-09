import random
import time


class Pile():
    """
    Class Pile basique, s'éxécute en suivant la règle du Last In First Out
    """

    def __init__(self):
        self.pile = []

    def empiler(self, valeur):
        # Permet de mettre une valeur en haut de la pile
        self.pile.append(valeur)

    def depiler(self):
        return self.pile.pop()  # Permet d'enlever la dernière valeur de la pile

    def sommet_pile(self):
        return self.pile[-1]  # Renvoie la valeur du sommet du la pile

    def longueur(self):
        return len(self.pile)  # Renvoie la longueur de la pile

    def est_vide(self):
        return len(self.pile) == 0  # Renvoie True si la pile est vide

    def est_present(self, val):
        return val in self.pile  # Renvoie True si la valeur cherchée est dans la pile


class Case:
    """Class Case qui permet de contenir différentes valeurs
    __init__ :
    posn(int): valeur de la position dans la grille en x
    posm(int): valeur de la position dans la grille en y
    n(int): représente le 'mur' dans la direction nord (1 = mur | 0 = vide)
    o(int): représente le 'mur' dans la direction ouest (1 = mur | 0 = vide)
    s(int): représente le 'mur' dans la direction sud (1 = mur | 0 = vide)
    e(int): représente le 'mur' dans la direction est (1 = mur | 0 = vide)
    exploree(int): permet de reconnaître si la case à été modifiée (0 = 'non-découvert' | 1 = 'découvert')
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
        """Méthode permettant de changer la valeur de l'attribut du mur Nord

        Args:
            valeur(int)
        """
        self.n = valeur

    def setOuest(self, valeur):
        """Méthode permettant de changer la valeur de l'attribut du mur Ouest

        Args:
            valeur(int)
        """
        self.o = valeur

    def setSud(self, valeur):
        """Méthode permettant de changer la valeur de l'attribut du mur Sud

        Args:
            valeur(int)
        """
        self.s = valeur

    def setEst(self, valeur):
        """Méthode permettant de changer la valeur de l'attribut du mur Est

        Args:
            valeur(int)
        """
        self.e = valeur

    def setExploree(self, valeur):
        """Méthode permettant de changer la valeur de l'attribut exploree 

        Args:
            valeur(int)
        """
        self.exploree = valeur

    def getNord(self):
        """
        Méthode permettant de récupérer à l'attribut n
        """
        return self.n

    def getOuest(self):
        """
        Méthode permettant de récupérer à l'attribut o
        """
        return self.o

    def getSud(self):
        """
        Méthode permettant de récupérer à l'attribut s
        """
        return self.s

    def getEst(self):
        """
        Méthode permettant de récupérer à l'attribut e
        """
        return self.e

    def getExploree(self):
        """
        Méthode permettant de récupérer à l'attribut exploree
        """
        return self.exploree

    def getPosn(self):
        """
        Méthode permettant de récupérer à l'attribut posn
        """
        return self.posn

    def getPosm(self):
        """
        Méthode permettant de récupérer à l'attribut posm
        """
        return self.posm

    def __str__(self):
        """
        Méthode permettant d'afficher les valeurs des attributs de la case
        """
        return f"Case{self.posn, self.posm, self.n, self.o, self.s, self.e}"

    def voisinNord(self, laby):
        """Méthode qui renvoie le voisin, dans la direction voulu, de la case

        Args:
            laby(obj): Labyrinthe contenant toutes les cases

        Returns:
            None: La case ne comporte pas de voisin dans la direction souhaitée
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
            None: La case ne comporte pas de voisin dans la direction souhaitée
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
            None: La case ne comporte pas de voisin dans la direction souhaitée
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
            None: La case ne comporte pas de voisin dans la direction souhaitée
            Case(obj): La case de la direction voulu
        """
        if self.posm == (len(laby[self.posn]) - 1):  # Si la coordonnée y est égale à la longeur du labyrinthe alors la case est "collée" au bord donc elle n'a pas de voisin
            return None
        else:
            return laby[self.posn][self.posm + 1]

    def voisins(self, laby):
        """Méthode qui renvoie les voisins de la case dans toutes les directions, si elle en possède

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
    """Class Labyrinthe qui créer une grille composée de class Case, de taille longueur par largeur.
    __init__ :
    height(int) : représente la longueur, minimum 2 car c'est plus petit est inutile pour avoir un labyrinthe 
    width(int) : représente la largeur, minimum 2 car c'est plus petit est inutile pour avoir un labyrinthe
    cells(list) : tableau contenant la "grille" avec toutes les cases
    every_lines(list) : tableau utilisé pour la représentation du labyrinthe dans la console, il contient chaque "ligne" 
    """

    def __init__(self, height=2, width=2):
        self.height = height
        self.width = width
        self.cells = []
        self.every_lines = []
        # Création de la grille avec le nombres de case en fonction de la longueur & largeur
        for i in range(0, self.height):
            # Initialisation de chaque ligne qui va contenir les cases
            self.cells.append([])
            for j in range(0, self.width):
                # Ajout de chaque case avec l'appelle de la class Case
                self.cells[i].append(Case(i, j))
        self.creation_laby()  # Appelle de la fonction permettant de tracer le labyrinthe

    def creation_laby(self):
        """
        Méthode qui va créer le labyrinthe grâce au principe de parcours en profondeur

        Ne renvoie rien mais modifie le labyrinthe afin qu'il soit dit "parfait"
        """
        visites = []
        p = Pile()  # Appel de la class Pile
        depart = self.cells[0][0]
        visites.append(depart)
        p.empiler(depart)
        while not p.est_vide():
            temp = p.sommet_pile()  # temp récupère la case le plus au dessus de la pile
            voisin = []
            for i in temp.voisins(self.cells):  # Parmis tous les voisins de temp
                # On prend seulement ceux non visités et non présents dans la pile
                if i not in visites and p.est_present(i) is False:
                    voisin.append(i)
            if voisin != []:  # Si la liste des voisins de temp n'est pas vide
                v = random.choice(voisin)  # Un parmis eux est choisi au hasard
                # Le mur entre temp et ce voisin est alors cassé
                self.connect(temp, v)
                # v est alors placé dans visites, et est exploree, pour eviter de repasser par cette case
                visites.append(v)
                v.setExploree(1)
                p.empiler(v)  # On s'occupe alors du cas de v, qui devient temp
            else:
                p.depiler()  # on dépile la pile si aucun voisin de temp n'est disponible

    def entree_sortie(self, x, y, direction):
        """
        Méthode qui permet de créer les entrée/sortie du labyrinthe en fonction de la direction donnée en paramètre

        Args: 
            x(int)
            y(int)
            direction(str)

        Ne renvoie rien mais modifie les valeurs des cases concernées
        """
        case = self.cells[x][y]
        if direction == "Est":
            case.setEst(0)
        else:
            case.setOuest(0)

    def get_visuel(self):
        """
        Méthode permettant la création d'un labyrinthe affichable dans la console
        Ne récupère que les valeurs de Ouest et de Sud de chaque case pour éviter les répétitions (Est d'une case = Ouest de son voisin)

        Return: un tableau avec le str de chacune des lignes du labyrinthe
        """
        self.every_lines.append(
            '___' * (self.width))  # Permet d'afficher le contour supérieur du labyrinthe
        for i in range(self.height):  # Parcours toute la hauteur du labyrinthe
            ligne = ''
            for j in range(self.width):  # Parcours toute la largeur du labyrinthe
                str = ''
                # Récupère la valeur du mur Ouest de la case
                ouest = self.cells[i][j].getOuest()
                # Récupère la valeur du mur Sud de la case
                sud = self.cells[i][j].getSud()
                # Place un mur | si besoin, laisse un trou sinon
                if ouest == 1:
                    str += '|'
                else:
                    str += ' '
                # Place un mur __ si besoin, laisse un trou sinon
                if sud == 1:
                    str += '__'
                else:
                    str += '  '
                ligne += str
            ligne += '|'  # Coutour (gauche) du labyrinthe
            self.every_lines.append(ligne)
        return self.every_lines

    def __str__(self):
        """
        Permet d'afficher dans la console lors d'un print(), le labyrinthe créé par get_visuel() en chaine de caractère
        """
        self.get_visuel()  # Appel la fonction pour avoir le visuel "console" du labyrinthe
        for ligne in self.every_lines:
            print(ligne)
        return ''

    def affiche_valeur(self):
        """
        Méthode permettant l'affichage des cases du labyrinthe dans la console

        Return: Un tableau comprenant les valeurs de toute les case du labyrinthe dans la console
        """
        temp_laby = []  # Création d'une liste contenant les valeurs du labyrinthe
        # Parcours de tout le labyrinthe
        for i in range(0, self.height):
            temp_laby.append([])
            for j in range(0, self.width):
                # temp_laby prend, à chaque tour de booucle, les valeurs de la case correspondant aux coordonnées
                temp_laby[i].append(self.cells[i][j].__str__())
        return temp_laby

    def connect(self, case_depart, case_voisin):
        """
        Fonction qui prend en paramètre deux cases voisines, calcule le mur voisin entre ces deux cases 
        et le "supprime" des deux cases en attribuant leurs valeur à 0

        Args :
            case_depart(obj) : une case appartenant au labyrinthe
            case_voisin(obj) : une case voisine à la case_depart

        Ne renvoie rien mais modifie les cases entrées en paramètres
        """
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

    def write_svg(self, filename, entree):
        """
        Méthode permettant de transformer le labyrinthe en une image SVG

        Args :
            filename(str) : Le nom du fichier svg qui va être créé (si on rentre un chemin avant le nom, l'image sera créé dans le chemin renseigné)
            entree(int) : coordonnée x d'une case représentant l'entrée du labyrinthe

        Ne renvoie rien mais créé une image SVG 
        """

        # Calcule le ratio de l'image en fonction de la longueur & largeur
        aspect_ratio = self.height / self.width
        padding = 10  # Rempli le labyrinthe tout autour avec cette valeur

        # Hauteur et largeur du labyrinthe (sans contours), en pixels
        height = 600
        width = int(height * aspect_ratio)

        # Facteurs d'échelle pour lier les coordonnées aux pixels
        scy, scx = height / self.width, width / self.height

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Ecris la commande pour dessiner un mur dans le fichier de l'image SVG"""
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(ww_x1,
                  ww_y1, ww_x2, ww_y2), file=ww_f)

        # Créer le fichier SVG
        with open(filename, 'w') as f:
            # Initialisation du style pour le SVG
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'.format(
                height + 2 * padding, width + 2 * padding,
                -padding, -padding, height + 2 * padding, width + 2 * padding), file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)

            # Double boucle qui reprend le principe de la fonction get_visuel()
            # Va alors dessiner les murs Sud et Est de chaque case, si présents
            for x in range(self.height):
                for y in range(self.width):
                    # On vérifie si la case possède un mur Est
                    if self.cells[x][y].getEst() == 1:
                        # Puis on calcule les différentes coordonnées pour pouvoir tracer un vecteur repésentant le mur
                        x1 = x * scx
                        y1 = (y + 1) * scy
                        x2 = (x + 1) * scx
                        y2 = (y + 1) * scy
                        write_wall(f, y1, x1, y2, x2)
                    # On vérifie si la case possède un mur Est
                    if self.cells[x][y].getSud() == 1:
                        # Puis on calcule les différentes coordonnées pour pouvoir tracer un vecteur repésentant le mur
                        x1 = (x + 1) * scx
                        y1 = y * scy
                        x2 = (x + 1) * scx
                        y2 = (y + 1) * scy
                        write_wall(f, y1, x1, y2, x2)

            # Dessine alors les murs Nord et Ouest, non dessinés par les procédures précédentes
            # Mur Nord
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(height), file=f)
            # Calcule des coordonnées du départ
            y1 = entree * scx
            y2 = (entree + 1) * scx
            # Le mur Ouest doit d'abord être dessiné du début jusqu'à la première coordonnée de l'entrée
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(y1), file=f)
            # Puis de la fin de l'entrée jusqu'à le bas du labyrinthe, c'est à dire que l'on laisse un vide pour l'entrée
            print(
                '<line x1="0" y1="{}" x2="0" y2="{}"/>'.format(y2, width), file=f)
            print('</svg>', file=f)


def laby_web(longueur, largeur, val_entree, val_sortie):
    """
    Fonction utilisée uniquement pour la partie Flask interface web.
    Elle reçoit les paramètres envoyés par l'utilisateur et créé un labyrinthe de ces paramètres
    Args:
        longueur(int): Longueur du labyrinthe
        largeur(int): Largeur du labyrinthe
        val_entree(int): Placement sur la longueur de l'entrée
        val_sortie(int): Placement sur la longueur de la sortie

    Returns:
        (str) : renvoie le chemin et le nom de l'image du labyrinthe créé
    """
    # Appel de la class Labyrinthe
    laby = Labyrinthe(int(longueur), int(largeur))
    # Ajout de l'entrée
    laby.entree_sortie(int(val_entree), 0, "Ouest")
    # Ajout de la sortie
    laby.entree_sortie(int(val_sortie), int(largeur) - 1, "Est")
    codage = time.time()  # On prend une valeur aléatoire pour nommé l'image
    # On est obligé de nommer d'une manière différente chaque image créée car sinon on peut
    # Avoir des problèmes de cache sur le serveur et la même image s'affichera malgré le changement de fichier
    # Pour y remédier on nomme chaque image distinctement et on envoie son nom au serveur
    chemin_image = "images/maze_web" + \
        str(codage).split(".")[0] + ".svg"  # Chemin + le nom de l'image
    # Appel de la fonction permettant de créer l'image sous forme d'un fichier svg
    laby.write_svg("website/static/" + chemin_image, int(val_entree))
    return chemin_image


"""
# Pour effectuer les tests, supprimer les guillemets et lancer ce programme (maze_generator.py)
# Testes de création de labyrinthe
for i in range(0, 10):
    # Valeur de taille aléatoire
    longueur = random.randint(4, 70)
    largeur = random.randint(4, 70)
    # Création du labyrinthe
    laby = Labyrinthe(longueur, largeur)
    # Création de l'entrée et de la sortie
    entree = random.randint(0, longueur - 1)
    laby.entree_sortie(entree, 0, "Ouest")
    laby.entree_sortie(random.randint(0, longueur - 1), largeur - 1, "Est")
    # Création de l'image
    laby.write_svg("maze" + str(i) + ".svg", entree)
    print(laby)
"""
