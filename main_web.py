from website import create_app

"""




http://datumologist.com/post/3

Lancer ce fichier pour lancer le site ensuite aller sur http://127.0.0.1:5000/
"""

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
