import torch
import torch.nn as nn
import torch.nn.functional as F


class ValueNetwork(nn.Module):
    """
    A simple fully-connected neural network that takes the puzzle state
    and predicts a single value (how good the state is).
    """

    def __init__(self, input_size, hidden_size=128):
        super(ValueNetwork, self).__init__()

        # Layers
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, 1)  # Output: scalar value

    def forward(self, x):
        """
        Forward pass for the network.
        """
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        value = torch.tanh(self.fc3(x))  # Keeps output between -1 and 1
        return value
