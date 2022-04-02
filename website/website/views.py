from flask import Blueprint, render_template, request, flash
from maze_generator import *
from random import randint

views = Blueprint('views', __name__)

"""
INFO A RETENIR
mettre @login_required entre @views.route(...) et def ...
pour empecher d'accèder à la page sans être connecté

"""


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('aleatoire-longueur'):
            longueur = randint(4, 100)
        else:
            longueur = request.form.get('valeur-longueur')
        if request.form.get('aleatoire-largeur'):
            largeur = randint(4, 100)
        else:
            largeur = request.form.get('valeur-largeur')
        if request.form.get('aleatoire-depart'):
            depart = randint(4, longueur)
        else:
            depart = request.form.get('valeur-depart')
        if request.form.get('aleatoire-arrivee'):
            arrivee = randint(4, longueur)
        else:
            arrivee = request.form.get('valeur-arrivee')
        print(longueur, largeur, depart, arrivee)
        laby_web(longueur, largeur, depart, arrivee)
        flash('Création du labyrinthe réussie !', category='success')
        return render_template("Maze.html")
    return render_template("home.html")


@views.route('/Maze')
def maze():
    return render_template("Maze.html")
