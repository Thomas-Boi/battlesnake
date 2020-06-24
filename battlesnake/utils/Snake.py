from typing import List
from battlesnake.utils.MoveEnum import Move
from battlesnake.utils.SafeMovePlanner import SafeMovePlanner
from battlesnake.utils.BestMovePlanner import BestMovePlanner
from battlesnake.utils.HeadScenario import HeadScenario


class Snake:
    def __init__(self, board):
        """
        Init a Snake.
        :param board: information about the current board.
        """
        # extract dimensions because these values won't change
        self.board_height = board["height"]
        self.board_width = board["width"]

        # init these values without values cause they change often
        self.head = None
        self.body = None
        self.other_snakes = None
        self.last_move = None
        self.food = None
        self.health = None

    def decide_next_move(self, board: dict, snake_info: dict) -> str:
        """
        Decide the next move the snake is going to take.
        The next move must be within bound of the board and
        not hit other snakes.
        :param board: information about the current board.
        :param snake_info: information about my snake.
        :return: the value of a Move enum member (aka a str).
        """
        # always call this first so we have the best data
        self.extract_info(board, snake_info)
        safe_scenarios = SafeMovePlanner.get_safe_moves(
            self.head, self.last_move, self.board_width,
            self.board_height, self.body, self.other_snakes
        )

        best_scenario = BestMovePlanner.get_best_scenario(
            safe_scenarios, self.head, self.food)
        return best_scenario.move.value

    def extract_info(self, board: dict, snake_info: dict) -> None:
        """
        Extract the info from the parameters and track them
        with our instance variables.
        :param board: information about the current board.
        :param snake_info: information about my snake.
        :return: None
        """
        self.head = snake_info["head"]
        self.body = snake_info["body"]
        self.health = snake_info["health"]

        all_snakes = board["snakes"]
        # remove my snake
        all_snakes.remove(snake_info)
        self.other_snakes = all_snakes
        self.food = board["food"]
