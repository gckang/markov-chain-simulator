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