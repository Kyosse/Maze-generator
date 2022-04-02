from flask import Blueprint, render_template, request, flash
from maze_generator import *
views = Blueprint('views', __name__)

"""
INFO A RETENIR
mettre @login_required entre @views.route(...) et def ...
pour empecher d'accèder à la page sans être connecté

"""


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        x_val = request.form.get('x')
        y_val = request.form.get('y')
        laby_web(x_val, y_val)
        flash('Création du labyrinthe réussie !', category='success')

    return render_template("home.html")


@views.route('/Maze')
def maze():
    return render_template("Maze.html")
