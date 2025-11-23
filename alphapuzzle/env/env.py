class AlphaPuzzleEnv:
    def __init__(self, size=4):
        self.size = size
        self.reset()

    def reset(self):
        # Create a blank puzzle board
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        return self.board

    def step(self, action):
        # Placeholder step function (you will expand later)
        reward = -1
        done = False
        info = {}
        return self.board, reward, done, info

    def render(self):
        for row in self.board:
            print(row)
