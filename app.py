from flask import Flask, render_template, request
from simulation import Simulation
from l_before_r import LbeforeR
from expected_movements import ExpectedMovements
from invariant import InvariantSimulation

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("invariant.html")

@app.route("/random-walk")
def random_walk():
    return render_template("randomwalk.html")

@app.route("/graph")
def graph_example():
    return render_template("graph_example.html")

@app.route("/irreducible-aperiodic")
def irreducible():
    return render_template("irreducible.html")

@app.route("/vocabulary")
def vocabulary():
    return render_template("vocabulary.html")