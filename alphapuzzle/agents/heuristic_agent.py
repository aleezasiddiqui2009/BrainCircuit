from alphapuzzle.game import Game
import random

class HeuristicAgent:
    """
    A simple heuristic agent that tries to pick moves 
    that are closer to the goal state.
    """

    def __init__(self, name="HeuristicAgent"):
        self.name = name

    def choose_move(self, game: Game):
        # Get all valid moves
        moves = game.valid_moves()

        # If no moves, return None
        if not moves:
            return None

        # Basic heuristic:
        # Prefer moves that reduce the Manhattan distance to the goal state

        best_move = None
        best_score = float("inf")

        for move in moves:
            # Make a copy of the game
            copied = game.copy()

            # Apply the move to the copied game
            copied.apply_move(move)

            # Compute heuristic score
            score = copied.manhattan_distance()

            # Pick the smallest distance
            if score < best_score:
                best_score = score
                best_move = move

        # If everything ties, pick random
        if best_move is None:
            best_move = random.choice(moves)

        return best_move
