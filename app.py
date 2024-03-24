from flask import Flask, render_template, request, jsonify
from simulation import Simulation
from l_before_r import LbeforeR
from expected_movements import ExpectedMovements
from invariant import InvariantSimulation
import numpy as np

app = Flask(__name__)

number_states = 0
probability_matrix = [[0.0] * number_states for x in range(number_states)]
network = None
invariant_sim = None

@app.route("/", methods=["GET", "POST"])

def invariant():
    global number_states, probability_matrix
    # number_states = 0
    # probability_matrix = [[]]
    probability_matrix = [[0.2, 0.5, 0.3], [0.4, 0.3, 0.3], [0.1, 0.2, 0.7]]  # Example probability matrix
    if request.method == "POST":
        number_states = int(request.form.get("numberStatesInput"))

    print("Probability Matrix in Flask:", probability_matrix) 
    return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix)

@app.route("/table", methods=["POST"])
def process_invariant_table():
    global number_states, probability_matrix
    probability_matrix = [[0.0] * number_states for x in range(number_states)]
    for i in range(number_states):
        for j in range(number_states):
            probability_matrix[i][j] = float(request.form.get(f"probability{i}{j}"))

    print(probability_matrix)
    return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix)


# @app.route("/simulate_step", methods=['POST'])
# def simulate_step_invariant():
#     global number_states, probability_matrix, invariant_sim
#     if invariant_sim is None:
#         # Initialize invariant_sim if not initialized yet
#         invariant_sim = InvariantSimulation(number_states, probability_matrix)
    
#     invariant_sim.simulation_move()
    
#     # You may need to format the data to send back to the client
#     # For example:
#     # response = {
#     #     'nodes': updated_nodes,
#     #     'edges': updated_edges
#     # }
#     # return jsonify(response)
#     return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix, network=network)

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