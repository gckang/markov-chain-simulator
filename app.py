from flask import Flask, render_template, request, jsonify
from simulation import Simulation
from l_before_r import LbeforeR
from expected_movements import ExpectedMovements
from invariant import InvariantSimulation

app = Flask(__name__)

number_states = None
probability_matrix = None
invariant_sim = None

@app.route("/")
def invariant():
    number_states = 3  # Example number of states
    probability_matrix = [[0.2, 0.5, 0.3], [0.4, 0.3, 0.3], [0.1, 0.2, 0.7]]  # Example probability matrix
    return render_template("invariant.html", number_states=number_states, probability_matrix=probability_matrix)

# @app.route("/simulate_step", methods=['POST'])
# def simulate_step():
#     global number_states, probability_matrix, invariant_sim
#     data = request.get_json()
#     number_states = int(data['number_states'])
#     if invariant_sim is None:
#         # Initialize invariant_sim if not initialized yet
#         probability_matrix = [[0.0] * number_states for _ in range(number_states)]
#         invariant_sim = InvariantSimulation(number_states, probability_matrix)
    
#     invariant_sim.simulation_move()
    
#     # You may need to format the data to send back to the client
#     # For example:
#     # response = {
#     #     'nodes': updated_nodes,
#     #     'edges': updated_edges
#     # }
#     # return jsonify(response)
#     return jsonify({'message': 'Step simulated successfully'})