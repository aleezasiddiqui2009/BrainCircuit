import random

class RandomAgent:
    def get_action(self, state):
        # Returns a random action (0 = no-op, 1 = move)
        return random.choice([0, 1])
