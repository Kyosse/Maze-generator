from flask import Blueprint, render_template, request, flash
from maze_generator import *
from random import randint


# Défini dans Flask views comme repère pour les urls
views = Blueprint('views', __name__)

# Dans l'url, '/' désigne la page d'acceuil


# Défini le chemin et les méthodes pour lesquelles la fonction home() est activée
@views.route('/', methods=['GET', 'POST'])
def home():
    """
    Fonction activée à chaque chargement de la page ayant l'url ci-dessus récupérant les informations dans le form de la page html home.html

    Returns:
        Renvoie la page d'acceuil home.html si la requête est un GET
        Renvoie la page du labyrinthe maze.html ainsi que le chemin d'accès du labyrinthe si la requête est un POST
    """
    # Si la requête contient POST dans le header, c'est à dire que l'utilisateur à validé le form sur la page
    if request.method == 'POST':
        # Si la balise d'identifiant 'aleatoire-longueur' est cochée (Présente dans les données récupérées par le form)
        if request.form.get('aleatoire-longueur'):
            # Alors la valeur longueur est choisie aléatoirement
            longueur = randint(4, 70)
            # Et donc l'entrée et la sortie le sont également
            sortie = randint(0, int(longueur))
            entree = randint(0, int(longueur))
        else:  # Sinon on récupère la valeur de la longueur choisie par l'utilisateur
            longueur = request.form.get('valeur-longueur')
            # Si la balise d'identifiant 'aleatoire-entree' est cochée (Présente dans les données récupérées par le form)
            if request.form.get('aleatoire-entree'):
                # Alors la valeur entree est choisie aléatoirement
                entree = randint(0, int(longueur))
            else:  # Sinon on récupère la valeur de l'entrée choisie par l'utilisateur
                entree = request.form.get('valeur-entree')
            # Si la balise d'identifiant 'aleatoire-sortie' est cochée (Présente dans les données récupérées par le form)
            if request.form.get('aleatoire-sortie'):
                # Alors la valeur sortie est choisie aléatoirement
                sortie = randint(0, int(longueur))
            else:  # Sinon on récupère la valeur de la sortie choisis par l'utilisateur
                sortie = request.form.get('valeur-sortie')
        # Si la balise d'identifiant 'aleatoire-largeur' est cochée (Présente dans les données récupérées par le form)
        if request.form.get('aleatoire-largeur'):
            # Alors la valeur largeur est choisie aléatoirement
            largeur = randint(4, 70)
        else:  # Sinon on récupère la valeur de la largeur choisis par l'utilisateur
            largeur = request.form.get('valeur-largeur')

        # Grâce aux différentes valeurs récupérées ci-dessus on appel la fonction laby_web qui va réaliser un labyrinthe
        # Et renvoyer, en str, le chemin de l'image créée
        chemin_image = laby_web(longueur, largeur, entree, sortie)

        # Si l'entrée et la sortie n'ont pas été modifié on rappelle la possibilité de les modifier
        if int(entree) == 0 and int(sortie) == 0:
            # Flash permet d'envoyer un message sur la page actuelle
            flash("N'oubliez pas que vous pouvez sélectionner la position de l'entrée et de la sortie ", category='error')
        else:  # Sinon on affiche un message pour confirmer la création du labyrinthe
            flash('Création du labyrinthe réussie !', category='success')
        # On redirige vers la nouvelle page avec le chemin d'accès de l'image créée
        return render_template("maze.html", image_labyrinthe=chemin_image)
    # Sinon si la requête ne contient pas de POST on affiche la page d'acceuil
    return render_template("home.html")

# Dans l'url, '/Maze' désigne la page du labyrinthe


# Défini le chemin pour lequel la fonction maze() est activé
@views.route('/Maze')
def maze():
    return render_template("maze.html")
