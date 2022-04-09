from website import create_app # Va chercher la fonction create_app dans le fichier __init__

"""
Ce programme permet de lancer "l'émulateur" serveur FLASK
Pour lancer ce fichier, il suffit d'installer le module flask via la console grâce à la commande :

pip install flask

Puis lancer ce fichier pour lancer le site, ensuite aller sur votre navigateur et taper http://127.0.0.1:5000/
"""

app = create_app()  # Initialise le serveur et ses modules

if __name__ == '__main__':  # Lance et maintien le serveur lancé
    app.run(debug=True)
