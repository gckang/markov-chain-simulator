from simulation import Simulation
import numpy as np

class InvariantSimulation:
    def __init__(self, number_states, probability_matrix):
        self.simulation = Simulation(number_states, probability_matrix)
        self.number_hits = [0] * number_states
        self.invariant_distribution = [0.0] * number_states
        self.total_moves = 0

    def getInvariant(self):
        return self.invariant_distribution
    
    def getTotalMoves(self):
        return self.total_moves

    def simulation_move(self):
        self.simulation.change_state()
        self.total_moves += 1
        self.number_hits[self.simulation.get_current_state()] += 1
        for i in range(len(self.number_hits)):
            if self.number_hits[i] == 0:
                self.invariant_distribution[i] = 0
            else:
                self.invariant_distribution[i] = self.number_hits[i] / self.total_moves
        return self.simulation.get_current_state()

    def repeat_simulation(self, number_moves):
        for _ in range(number_moves):
            self.simulation_move()