from typing import List
from battlesnake.utils.MoveEnum import Move
from battlesnake.utils.HeadScenario import HeadScenario


class Snake:
    default_move = Move.UP

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

    def decide_next_move(self, board, snake_info) -> str:
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
        safe_scenarios = self.get_safe_moves()
        best_scenario = self.get_best_scenario(safe_scenarios)
        return best_scenario.move.value

    def extract_info(self, board, snake_info) -> None:
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
        # remove my snake from this list
        all_snakes.remove(snake_info)
        self.other_snakes = all_snakes
        self.food = board["food"]

    def get_safe_moves(self) -> List[HeadScenario]:
        """
        Get the possible moves that are safe to make within
        1 square. The next move must be within bound of the
        board and not hit other snakes/myself.
        :return: a list of safe Head_Scenarios. If all moves are bad, pick
        Move.UP as the default.
        """
        scenarios = self.get_available_scenarios()
        safe_scenarios = self.check_boundary(scenarios)
        safe_scenarios = self.check_my_body(safe_scenarios)
        return self.check_other_snake(safe_scenarios)

    def get_available_scenarios(self) -> List[HeadScenario]:
        """
        Get the available scenarios that the snake can take (these aren't
        safe or the best ones). This means all the moves EXCEPT the
        opposite of the the last move.
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
            invalid_direction = opposites_directions[self.last_move]
            all_moves.remove(invalid_direction)
        except KeyError:
            pass
        finally:
            all_scenarios = [
                HeadScenario(move, self.head) for move in all_moves
            ]
            return all_scenarios

    def check_boundary(self, scenarios: List[HeadScenario]) -> List[HeadScenario]:
        """
        Check for moves that won't make the snake get out of the
        boundary.
        :param scenarios: a list of possible HeadScenarios.
        :return: a list of safe Moves that won't go out of bound.
        If all moves are bad, the list will only contain a HeadScenario
        with the move property equals to Move.UP.
        """
        safe_scenarios = []
        for scenario in scenarios:
            if 0 <= scenario.head_scenario["x"] < self.board_width \
                    and 0 <= scenario.head_scenario["y"] < self.board_height:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Snake.default_move, self.head))
        return safe_scenarios

    def check_my_body(self, scenarios: List[HeadScenario]) -> List[HeadScenario]:
        """
        Check for moves so that the Snake won't hit itself.
        :param scenarios: a list of Moves.
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
            for body_part in self.body:
                if scenario.head_scenario == body_part:
                    hit_snake = True
                    break
            if not hit_snake:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Snake.default_move, self.head))
        return safe_scenarios

    def check_other_snake(self, scenarios: List[HeadScenario]) -> List[HeadScenario]:
        """
        Check for moves so that the Snake won't hit other Snake.
        :param scenarios: a list of Moves.
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
            for snake in self.other_snakes:
                for body_part in snake["body"]:
                    if scenario.head_scenario == body_part:
                        hit_snake = True
                        break
                if hit_snake:
                    break
            if not hit_snake:
                safe_scenarios.append(scenario)

        if len(safe_scenarios) == 0:
            safe_scenarios.append(HeadScenario(Snake.default_move, self.head))
        return safe_scenarios

    def get_best_scenario(self, scenarios: List[HeadScenario]) -> HeadScenario:
        """
        Get the best scenario from the scenarios. This means
        the snake will hunt for food, it won't trap itself with
        its own body or others (if possible), and trap other snake.
        :param scenarios: the possible scenarios. It must have at least
        one scenario that was chosen by the get_safe_move().
        :return: the best possible Move the Snake can take at
        that time.
        """
        try:
            # if there's only one scenario, there's no point checking
            # whether it's right or wrong
            if len(scenarios) == 1:
                return scenarios[0]
            return scenarios[0]
        except IndexError:
            print("get_best_scenario: scenarios need at least one element")
            return HeadScenario(Snake.default_move, self.head)

    def find_food(self, scenarios: List[HeadScenario]) -> None:
        """
        Find a path to the nearest food source.
        :return: None
        """
        pass
