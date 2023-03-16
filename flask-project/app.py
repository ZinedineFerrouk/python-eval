# ------------------------------
# Imports
# ------------------------------
from flask import Flask, render_template
from classes.System import System

app = Flask(__name__)


# ------------------------------
# Route home par default dans laquelle on instancie la classe System et on renvoie le tableau python avec les données
# dans le front 'index.html' avec la méthode render_template
# ------------------------------
@app.route('/')
def index():
    return render_template('index.html', systeme=(System().to_dict()))
