from enum import Enum


class Move(Enum):
    """
    All the possible moves that a Snake can make.
    """
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = 'right'
