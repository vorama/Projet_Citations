from flask import Flask, jsonify
import random


app = Flask(__name__)

citations = [
    {"citation1": "Tout est possible à qui rêve, ose, travaill et n'abandonne jamais.", "auteur": "Xavier Dolan"},
    {"citation2": "Ceux qui ne font rien de se trompent jamias", "auteur": "Théodore de Banvill"},
    {"citation3": "Vous ne pouvez pas être ce gamin qui reste figé en haut d'un toboggan en réfléchissant. Vous devez glisser", "auteur": "Tina Fey"},
    
]

@app.route('/quote', methods=['GET'])

def donner_une_citation ():
    return jsonify(random.choice(citations))
    # donner un citation random de la liste présédente

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
    # Exécute le serveur sur le port 5000

