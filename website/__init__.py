from flask import Flask
import os


def create_app():
    """
    Fonction initialisant les différents partis du serveur
    """
    app = Flask(__name__) # Initialisation du noyau
    app.config['SECRET_KEY'] = 'clé-secret'  # Clé secret global permet de sécuriser le serveur

    # Dossier_image est une liste qui contient les différents éléments présents dans le dossier images du site
    dossier_image = os.listdir(os.path.join(app.static_folder, 'images'))
    for i in range(2, len(dossier_image)): # Boucle qui supprime les fichier en "trop"(en commençant à 2 pour ne pas
        os.remove(os.path.join(app.static_folder, "images/" + dossier_image[i])) # supprimer le logo par erreur)

    # Import le fichier views qui s'occupe de la gestion des url
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app
