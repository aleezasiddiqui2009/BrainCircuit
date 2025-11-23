from alphapuzzle.env.env import AlphaPuzzleEnv

def play():
    env = AlphaPuzzleEnv(size=4)
    env.reset()
    env.render()

if __name__ == "__main__":
    play()
