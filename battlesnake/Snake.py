from enum import Enum


class Move(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = 'right'


class Snake:
    name = "BOI!"

    def decide_next_move(self, board, snake_info) -> str:
        """
        Decide the next move the snake is going to take.
        The next move must be within bound of the board and
        not hit other snakes.
        :param board: information about the current board.
        :param snake_info: information about the snake.
        :return: the value of a Move enum member.
        """
        return Move.UP.value
