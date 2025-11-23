class BaseAgent:
    """
    Base class for all agents in the AlphaPuzzle project.
    Provides a common interface that all agents must follow.
    """

    def __init__(self, env):
        self.env = env

    def select_action(self, state):
        """
        Choose an action given the current state.
        Must be overridden by child classes.
        """
        raise NotImplementedError("select_action() must be implemented by the agent.")

    def train(self, episodes=1000):
        """
        Training loop for the agent.
        Override this in QAgent or MCTSAgent.
        """
        raise NotImplementedError("train() must be implemented by the agent.")
