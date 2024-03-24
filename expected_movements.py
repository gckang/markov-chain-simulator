from simulation import Simulation
import numpy as np

class ExpectedMovements:
    def __init__(self, number_states, goal, start, probability_matrix):
        self.simulation = Simulation(number_states, probability_matrix)
        self.starting_state = start
        self.goal_state = goal
        self.total_runs = 0
        self.total_moves = 0
        self.average = 0

    def simulation_move(self):
        self.simulation.change_state()
        self.total_moves += 1
        if self.simulation.get_current_state() == self.goal_state:
            self.total_runs += 1
            self.average = self.total_moves / self.total_runs
            self.simulation.set_current_state(self.starting_state)

    def simulate_number_trials(self, num_trials):
        while self.total_runs < num_trials:
            self.simulation_move()

A = np.array([[.2, .4, .4],
[.1, .5, .4],
[.6, .3, .1]])
sim = ExpectedMovements(3, 2, 0, A)
sim.simulate_number_trials(500)
print (sim.average)