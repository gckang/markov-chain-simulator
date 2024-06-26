from simulation import Simulation
import numpy as np

class LbeforeR:
    def __init__(self, number_states, bad, goal, starting, probability_matrix):
        self.simulation = Simulation(number_states, probability_matrix)
        self.bad_state = bad
        self.goal_state = goal
        self.starting_state = starting
        self.num_bad_num_goal = [0, 0]
        self.total = 0
        self.goal_to_bad = 0
        self.simulation.set_current_state(starting)

    def get_ratio(self):
        return self.goal_to_bad
    
    def get_total(self):
        return self.total
    
    def get_num_bad_num_goal(self):
        return self.num_bad_num_goal

    def simulation_move(self):
        self.simulation.change_state()
        current_state = self.simulation.get_current_state()
        if current_state == self.goal_state:
            self.num_bad_num_goal[1] += 1
            self.total += 1   
            self.goal_to_bad = self.num_bad_num_goal[1] / self.total     
        elif current_state == self.bad_state:
            self.num_bad_num_goal[0] += 1
            self.total += 1 
            self.goal_to_bad = self.num_bad_num_goal[1] / self.total
        self.simulation.set_current_state(self.starting_state)
        return self.simulation.get_current_state

    def simulate_number_trials(self, num_trials):
        while self.total < num_trials:
            self.simulation_move()