"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import math
from scipy.spatial import distance

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    #78.21% w/40 games
    #75.93% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's num of moves divided by num of blank spaces minus opponent's num of moves divided by num of blank spaces. AKA heuristic10
    return float(len(game.get_legal_moves(player)) / len(game.get_blank_spaces()) - len(game.get_legal_moves(game.get_opponent(player))) / len(game.get_blank_spaces()))

def heuristic1(game, player):
    #70.36% w/40 games
    #74.07% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's number of moves squared minus opponent's number of moves squared.
    return float(len(game.get_legal_moves(player))**2 - len(game.get_legal_moves(game.get_opponent(player)))**2)

def heuristic2(game, player):
    #76.43% w/40 games
    #72.00% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    blanks = len(game.get_blank_spaces())
    #Returns player's num of moves times blank spaces minus opponent's num of moves times blank spaces.
    return float(len(game.get_legal_moves(player)) * blanks - len(game.get_legal_moves(game.get_opponent(player))) * blanks)

def heuristic3(game, player):
    #67.50% w/40 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's num of moves times blank spaces minus opponent's num of moves.
    return float(len(game.get_legal_moves(player)) * len(game.get_blank_spaces()) - len(game.get_legal_moves(game.get_opponent(player))))

def heuristic4(game, player):
    #68.21% w/40 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's num of moves times blank spaces
    return float(len(game.get_legal_moves(player)) * len(game.get_blank_spaces()))

def heuristic5(game, player):
    #75.36% w/40 games
    #75.61% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    blanks = len(game.get_blank_spaces())
    player_location = game.get_player_location(player)
    opp_location = game.get_player_location(game.get_opponent(player))

    #Returns player's num of moves times blanks plus player's distance from center square minus opponent's num of moves times blanks plus opponent's distance from center square.
    return float(len(game.get_legal_moves(player)) * blanks + math.sqrt(((player_location[0] - 3) ** 2 + (player_location[1] - 3) ** 2)) - len(game.get_legal_moves(game.get_opponent(player))) * blanks + math.sqrt(((opp_location[0] - 3) ** 2 + (opp_location[1] - 3) ** 2)))

def heuristic6(game, player):
    #69.29% w/40 games
    #71.93% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_location = game.get_player_location(player)
    opp_location = game.get_player_location(game.get_opponent(player))

    #Returns player's num of moves times player's distance from center minus opponent's num of moves times opponent's distance from center.
    return float(len(game.get_legal_moves(player)) * math.sqrt(((player_location[0] - 3) ** 2 + (player_location[1] - 3) ** 2)) - len(game.get_legal_moves(game.get_opponent(player))) * math.sqrt(((opp_location[0] - 3) ** 2 + (opp_location[1] - 3) ** 2)))

def heuristic7(game, player):
    #73.21% w/40 games
    #74.04% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_location = game.get_player_location(player)
    opp_location = game.get_player_location(game.get_opponent(player))

    #Returns player's num of moves times opponent's distance from center minus opponent's num of moves times player's distance from center.
    return float(len(game.get_legal_moves(player)) * math.sqrt(((opp_location[0] - 3) ** 2 + (opp_location[1] - 3) ** 2)) - len(game.get_legal_moves(game.get_opponent(player))) * math.sqrt(((player_location[0] - 3) ** 2 + (player_location[1] - 3) ** 2)) )

def heuristic8(game, player):
    #73.21% w/40 games
    #73.32% w/40 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    #This is id improved optimized to be faster.
    return float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))

def heuristic9(game, player):
    #75.36% w/40 games
    #73.43% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's num of moves divided by num of blank spaces
    return float(len(game.get_legal_moves(player)) / len(game.get_blank_spaces()))

def heuristic10(game, player):
    #78.21% w/40 games
    #75.93% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Returns player's num of moves divided by num of blank spaces minus opponent's num of moves divided by num of blank spaces.
    return float(len(game.get_legal_moves(player)) / len(game.get_blank_spaces()) - len(game.get_legal_moves(game.get_opponent(player))) / len(game.get_blank_spaces()))

def heuristic11(game, player):
    #73.21%, 71.07% w/40 games
    #72.32% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    #Returns player's distance from opponent times difference of player's num of moves minus opponent's num of moves.
    return math.sqrt((player_loc[0] - player_loc[1])**2 + (opp_loc[0] - opp_loc[1])**2) * float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))

def heuristic12(game, player):
    #67.14% w/40 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    #Returns player's distance from opponent times difference of player's num of moves minus opponent's num of moves.
    return abs(player_loc[0] - opp_loc[0]) + abs(player_loc[1] - opp_loc[1]) * float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))

def heuristic13(game, player):
    #66.07 w/40 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    #Returns player's distance from center times difference of player's num of moves minus opponent's num of moves.
    return abs(player_loc[0] - 3) + abs(player_loc[1] - 3) * float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))

def heuristic14(game, player):
    #72.14% w/60 games
    #72.46% w/400 games
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(game.get_opponent(player))

    #Returns player's distance from center minus num of blank spaces divided by percentage of board spaces empty minus num of opponent's moves.
    return float(len(game.get_legal_moves(player)) + (player_loc[0] - 3) + abs(player_loc[1] - 3) - len(game.get_blank_spaces()) / float(game.width * game.height) - len(game.get_legal_moves(game.get_opponent(player))))

class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=5, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10., is_student=False):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout
        self.is_student = is_student

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if not legal_moves:
            return (-1, -1)

        if self.is_student:
            if (3,3) in legal_moves:
                return (3, 3)

        selected_move = legal_moves[0]
        score = float('-inf')

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.iterative:
                depth = 1
                while True:
                    if self.method == 'minimax':
                        val, move = self.minimax(game, depth)
                    elif self.method == 'alphabeta':
                        val, move = self.alphabeta(game, depth)
                    if val > score:
                        score = val
                        selected_move = move
                    depth += 1
            else:
                if self.method == 'minimax':
                    val, selected_move = self.minimax(game, self.search_depth)
                elif self.method == 'alphabeta':
                    val, selected_move = self.alphabeta(game, self.search_depth)
            return selected_move

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return selected_move

        # Return the best move from the last completed search iteration
        return selected_move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        best_score = float('-inf') if maximizing_player else float('+inf')
        best_move = (-1,-1)

        if depth == 0:
            return self.score(game, game.active_player if maximizing_player else game.inactive_player), best_move

        for move in game.get_legal_moves():
            new_board = game.forecast_move(move)
            val, _ = self.minimax(new_board, depth - 1, not maximizing_player)

            if maximizing_player:
                if val > best_score:
                    best_score = val
                    best_move = move
            else:
                if val < best_score:
                    best_score = val
                    best_move = move
        return best_score, best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        best_score = float('-inf') if maximizing_player else float('+inf')
        best_move = (-1,-1)

        if depth == 0:
            return self.score(game, game.active_player if maximizing_player else game.inactive_player), best_move

        for move in game.get_legal_moves():
            new_board = game.forecast_move(move)
            val, _ = self.alphabeta(new_board, depth - 1, alpha, beta, not maximizing_player)

            if maximizing_player:
                if val > best_score:
                    best_score = val
                    best_move = move
                if val >= beta:
                    return best_score, best_move
                alpha = max(alpha, best_score)
            else:
                if val < best_score:
                    best_score = val
                    best_move = move
                if val <= alpha:
                    return best_score, best_move
                beta = min(beta, best_score)
        return best_score, best_move
