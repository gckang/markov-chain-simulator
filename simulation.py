import random
import numpy as np

class Simulation:

    def __init__(self, number_states, probability_matrix):
        self.number_states = number_states
        self.current_state = 0
        self.probability_matrix = probability_matrix
        self.simulation_probability_matrix = None
        self.set_probability_matrix(probability_matrix)

    def set_probability_matrix(self, matrix):
        Simulation.probability_matrix = matrix
        Simulation.simulation_probability_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            last_positive = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    Simulation.simulation_probability_matrix[i][j] = 0
                else:
                    Simulation.simulation_probability_matrix[i][j] = Simulation.simulation_probability_matrix[i][last_positive] + matrix[i][j]
                    last_positive = j

    def set_current_state(self, index):
        if index < len(Simulation.probability_matrix):
            self.current_state = index

    def get_current_state(self):
        return self.current_state

    def change_state(self):
        random_val = random.random()
        new_state_index = 0
        for i in range(self.number_states):
            if random_val <= Simulation.simulation_probability_matrix[self.current_state][i]:
                new_state_index = i
                break
        self.current_state = new_state_index