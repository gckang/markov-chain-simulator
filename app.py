from flask import Flask, render_template, request, jsonify
# from flask_visjs import VisJS4, Network
from simulation import Simulation
from l_before_r import LbeforeR
from expected_movements import ExpectedMovements
from invariant import InvariantSimulation
import numpy as np

app = Flask(__name__)

# VisJS4().init_app(app)

number_states = None
probability_matrix = None
network = None
invariant_sim = None

@app.route("/", methods=["GET", "POST"])

def invariant():
    global number_states, probability_matrix
    number_states = 0  # Example number of states
    probability_matrix = [[]]
    # probability_matrix = [[0.2, 0.5, 0.3], [0.4, 0.3, 0.3], [0.1, 0.2, 0.7]]  # Example probability matrix
    if request.method == "POST":
        number_states = int(request.form.get("numberStatesInput"))
        probability_matrix = [[0.0] * number_states for x in range(number_states)]
        # for x in number_states:
        #     network.add_node(x, shape='circle')
    return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix, network=network)

@app.route("/table", methods=["POST"])
def process_invariant_table():
    global number_states, probability_matrix
    for i in range(number_states):
        for j in range(number_states):
            probability_matrix[i][j] = float(request.form.get(f"probability{i}{j}"))
            # if probability_matrix[i][j] > 0:
            #     network.add_edge(i, j, value=probability_matrix[i][j])
    print(probability_matrix)
    return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix, network=network)


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