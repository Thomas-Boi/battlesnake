from battlesnake.utils.MoveEnum import Move
from copy import copy


class HeadScenario:
    def __init__(self, move: Move, head: dict):
        self._move = move
        holder = HeadScenario.find_head_scenario(move, head)
        self._head_scenario = holder

    @property
    def move(self):
        return self._move

    @property
    def head_scenario(self):
        return self._head_scenario

    def __str__(self):
        return f"move: {self._move}\n" \
               f"head_scenario: {self._head_scenario}\n"

    def __repr__(self):
        return str(self)

    @staticmethod
    def find_head_scenario(move: Move, head: dict):
        """
        Find the head scenarios based on the parameters.
        :param move: the move the snake might take.
        :param head: the coordinates that track the head.
        :return: the coordinates that track the head
        if it move in the self.move direction.
        """
        head_scenario = copy(head)
        if move == Move.UP:
            head_scenario["y"] += 1
        elif move == Move.DOWN:
            head_scenario["y"] -= 1
        elif move == Move.LEFT:
            head_scenario["x"] -= 1
        elif move == Move.RIGHT:
            head_scenario["x"] += 1
        return head_scenario
