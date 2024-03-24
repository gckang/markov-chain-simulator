from simulation import Simulation

class LbeforeR:
    def __init__(self, number_states, bad, goal, starting):
        self.simulation = Simulation(number_states)
        self.bad_state = bad
        self.goal_state = goal
        self.starting_state = starting
        self.num_bad_num_goal = [0, 0]
        self.total = 0
        self.goal_to_bad = 0
        self.simulation.set_current_state(starting)

    def simulation_move(self):
        self.simulation.change_state()
        current_state = self.simulation.get_current_state()
        if current_state == self.goal_state:
            self.num_bad_num_goal[1] += 1
        elif current_state == self.bad_state:
            self.num_bad_num_goal[0] += 1
        self.total += 1
        self.goal_to_bad = self.num_bad_num_goal[1] / self.total
        self.simulation.set_current_state(self.starting_state)

    def simulate_number_trials(self, num_trials):
        while self.total < num_trials:
            self.simulation_move()