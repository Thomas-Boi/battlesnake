from battlesnake.utils.MoveEnum import Move
from battlesnake.utils.HeadScenario import HeadScenario
from typing import List


class SafeMovePlanner:
    @staticmethod
    def get_safe_moves(head: dict, last_move: Move,
                       board_width: int, board_height: int,
                       body: List[dict], other_snakes: List[dict]) -> List[HeadScenario]:
        """
        Get the possible moves that are safe to make within
        1 square. The next move must be within bound of the
        board and not hit other snakes/myself.
        :param head: the coordinate of the snake's head.
        :param last_move: the last move of the snake.
        :param board_width: the width of the board.
        :param board_height: the height of the board.
        :param body: the coordinates of the snake's body.
        :param other_snakes: a list of the other snakes on the board.
        :return: a list of safe Head_Scenarios. If all moves are bad, pick
        Move.UP as the default.
        """
        scenarios = SafeMovePlanner \
            .get_available_scenarios(head, last_move)

        safe_scenarios = SafeMovePlanner.check_boundary(
            scenarios, board_width, board_height, head)

        safe_scenarios = SafeMovePlanner.check_my_body(
            safe_scenarios, head, body)

        return SafeMovePlanner.check_other_snake(
            safe_scenarios, head, other_snakes)

    @staticmethod
    def get_available_scenarios(head: dict, last_move: Move) -> List[HeadScenario]:
        """
        Get the available scenarios that the snake can take (these aren't
        safe or the best ones). This means all the moves EXCEPT the
        opposite of the the last move.
        :param head: the coordinate of the snake's head.
        :param last_move: the last move of the snake.
        :return: a list of HeadScenarios.
        """
        all_moves = [
            Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT
        ]

        # remove the opposite of last move
        opposites_directions = {
            Move.UP: Move.DOWN,
            Move.DOWN: Move.UP,
            Move.LEFT: Move.RIGHT,
            Move.RIGHT: Move.LEFT,
        }

        try:
            invalid_direction = opposites_directions[last_move]
            all_moves.remove(invalid_direction)
        except KeyError:
            pass
        finally:
            all_scenarios = [
                HeadScenario(move, head) for move in all_moves
            ]
            return all_scenarios

    @staticmethod
    def check_boundary(scenarios: List[HeadScenario],
                       width: int, height: int, head: dict) -> List[HeadScenario]:
        """
        Check for moves that won't make the snake get out of the
        boundary.
        :param scenarios: a list of possible HeadScenarios.
        :param width: the width of the board.
        :param height: the height of the board.
        :param head: the coordinate of the snake's head.
        :return: a list of safe Moves that won't go out of bound.
        If all moves are bad, the list will only contain a HeadScenario
        with the move property equals to Move.UP.
        """
        safe_scenarios = []
        for scenario in scenarios:
            if 0 <= scenario.head_scenario["x"] < width \
                    and 0 <= scenario.head_scenario["y"] < height:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Move.DEFAULT, head))
        return safe_scenarios

    @staticmethod
    def check_my_body(scenarios: List[HeadScenario],
                      head: dict, body: List[dict]) -> List[HeadScenario]:
        """
        Check for moves so that the Snake won't hit itself.
        :param scenarios: a list of Moves.
        :param head: the coordinate of the snake's head.
        :param body: the coordinates of the snake's body.
        :return: a list of safe Moves that won't hit myself.
        If all moves are bad, the list will only contain a HeadScenario
        with the move property equals to Move.UP.
        """
        # if there's only one scenario, there's no point checking
        # whether it's right or wrong
        if len(scenarios) == 1:
            return scenarios

        safe_scenarios = []
        for scenario in scenarios:
            hit_snake = False
            for body_part in body:
                if scenario.head_scenario == body_part:
                    hit_snake = True
                    break
            if not hit_snake:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Move.DEFAULT, head))
        return safe_scenarios

    @staticmethod
    def check_other_snake(scenarios: List[HeadScenario],
                          head: dict, other_snakes: List[dict]) -> List[HeadScenario]:
        """
        Check for moves so that the Snake won't hit other Snake.
        :param scenarios: a list of Moves.
        :param head: the coordinate of the snake's head.
        :param other_snakes: a list of the other snakes on the board.
        :return: a list of safe Moves that won't hit other snake.
        If all moves are bad, the list will only contain a HeadScenario
        with the move property equals to Move.UP.
        """
        # if there's only one scenario, there's no point checking
        # whether it's right or wrong
        if len(scenarios) == 1:
            return scenarios

        safe_scenarios = []
        for scenario in scenarios:
            hit_snake = False
            for snake in other_snakes:
                for body_part in snake["body"]:
                    if scenario.head_scenario == body_part:
                        hit_snake = True
                        break
                if hit_snake:
                    break
            if not hit_snake:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Move.DEFAULT, head))
        return safe_scenarios
