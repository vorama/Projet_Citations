from flask import Flask, jsonify
'''import la classe Flask et la fonction jsonify depuis le module flask
on pourait faire comme suite:
from flask import Flask
from flask import jsonify
Mais ça apporterait rien à par de la lisibilité pour les débutants
'''
import random
#import le module random


app = Flask(__name__)
''' flash back du cours de python:
Flask = la classe
app = une instance
__name__ = ma futur variable
'''

citations = [
# "citations" une liste de dictionnaire. Chaque {} représente un dictionnaire avec, sur chaques lignes, 2 clés(quote + author) et deux valeurs 
    {"quote": "Tout est possible à qui rêve, ose, travaill et n'abandonne jamais.", "author": "Xavier Dolan"},
    {"quote": "Ceux qui ne font rien de se trompent jamias", "author": "Théodore de Banvill"},
    {"quote": "Vous ne pouvez pas être ce gamin qui reste figé en haut d'un toboggan en réfléchissant. Vous devez glisser", "author": "Tina Fey"},
    
]


# Route pour la racine (/), ajoutée ici
@app.route('/')
def home():
    return "Bienvenue sur l'API Citations!"


@app.route('/quote', methods=['GET'])
def donner_une_citation ():
    return jsonify(random.choice(citations))
    # donner un citation random de la liste présédente

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
    # Exécute le serveur sur le port 5000

