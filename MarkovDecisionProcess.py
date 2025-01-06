import numpy as np
import json
import os


class MarkovDecisionProcess:
    def __init__(self):
        self.states = set()
        self.terminal_states = set()
        self.actions = {}
        self.policy = open(str(os.getcwd())+"/"+"OptimalPolicy/policyIteration.json", "r")
        self.policy = json.load(self.policy)

    # all possible states in game
    def generate_states(self):
        # define function to generate all states
        def _brute_states():
            # 0: no move, 1: X, 2: O
            all_board_config = set()
            for values in np.ndindex(3, 3, 3, 3, 3, 3, 3, 3, 3):
                state = tuple(values)
                all_board_config.add(state)
            return all_board_config

        # define function to check if there are two winners at the same time
        def _check_if_two_winners(state):
            count_h, count_v = 0, 0
            for i in range(3):
                if (state[i * 3] == state[i * 3 + 1] == state[i * 3 + 2] and state[i * 3] == 1) or (
                        state[i * 3] == state[i * 3 + 1] == state[i * 3 + 2] and state[i * 3] == 2):
                    count_h += 1
                if (state[i] == state[i + 3] == state[i + 6] and state[i] == 1) or (
                        state[i] == state[i + 3] == state[i + 6] and state[i] == 2):
                    count_v += 1
            if count_h == 2 or count_v == 2:
                return True
            return False

        # initialise states with possible and impossible states
        self.states = _brute_states()

        # remove states that are not possible
        for state in self.states.copy():
            # suppose that the computer is always X, if no. of X > O, then remove state
            if state.count(1) > state.count(2):
                self.states.remove(state)
            # if abs. difference in the number of X and O > 2, then remove state
            elif abs(state.count(1) - state.count(2)) > 1:
                self.states.remove(state)
            # if there are 2 winners at the same time, then remove state
            elif _check_if_two_winners(state):
                self.states.remove(state)

    # terminal states
    def terminal_state(self):
        # all possible states and updates states when game is over
        for state in self.states:
            if self.win(state):
                self.terminal_states.add(state)
            elif state.count(0) == 0:
                self.terminal_states.add(state)

    # action set
    def generate_actions(self):
        # define function for all possible states and update the possible actions for each state
        for state in self.states():
            self.actions[state] = None
            if state not in self.terminal_states:
                self.actions[state] = []
                for i in range(9):
                    if state[i] == 0:
                        self.actions[state].append(i)

    # transition function
    def transition_function(self, state):
        # define function that takes a state and returns the probability of each possible next state
        # if the game is over
        if state in self.terminal_states:
            return 0
        # if the game is not over, return 1/(number of possible actions - 1) for 0
        else:
            return 1 / (len(self.actions[state]) - 1)

    # reward function
    def reward_function(self, state):
        # define function that takes a state and returns the reward of the state
        if self.win(state) == 1:
            return 1
        if self.win(state) == 2:
            return -1
        return 0

    def win(self, state):
        for i in range(3):
            if state[i * 3] == state[i * 3 + 1] == state[i + 3 + 2] and state[i * 3] != 0:
                return state[i * 3]
            if state[i] == state[i + 3] == state[i + 6] and state[i] != 0:
                return state[i]
            if state[4] == state[6] == state[8] and state[4] != 0:
                return state[4]
            elif state[0] == state[4] == state[8] and state[0] != 0:
                return state[0]
            else:
                return False

    def possible_next_states(self, state, action):
        new_state = list(state)
        new_state[action] = 1
        if self.win(new_state):
            return []
        possible_next_states = []
        for i, case in enumerate(new_state):
            next_new_state = new_state.copy()
            if case == 0:
                next_new_state[i] == 2
                possible_next_states.append(tuple(next_new_state))
        return possible_next_states

    def improved_transition_probability(self, state, action):
        # define function that takes a state and returns the probability of each possible
        # next state inspired from value iteration policy

        # if the game is over, return 0
        if state in self.terminal_states:
            return 0
        # if the game is not over, return 1/number of possible actions for 0
        else:
            return 1 if action == self.policy[state] else 0
