from battlesnake.utils.MoveEnum import Move
from battlesnake.utils.HeadScenario import HeadScenario
import math
from typing import List


class BestMovePlanner:
    @staticmethod
    def get_best_scenario(scenarios: List[HeadScenario],
                          head: dict, foods: List[dict]) -> HeadScenario:
        """
        Get the best scenario from the scenarios. This means
        the snake will hunt for food, it won't trap itself with
        its own body or others (if possible), and trap other snake.
        :param scenarios: the possible scenarios. It must have at least
        :param head: the coordinate of the snake's head.
        :param foods: the coordinates of the food on the board.
        one scenario that was chosen by the get_safe_move().
        :return: the best possible Move the Snake can take at
        that time.
        """
        try:
            # if there's only one scenario, there's no point checking
            # whether it's right or wrong
            if len(scenarios) == 1:
                return scenarios[0]

            nearest_food = BestMovePlanner \
                .find_nearest_food(head, foods)

            best_scenario = BestMovePlanner.find_scenario_closest_to_food(
                scenarios, nearest_food
            )
            return best_scenario
        except IndexError:
            print("get_best_scenario: scenarios need at least one element")
            return HeadScenario(Move.DEFAULT, head)

    @staticmethod
    def find_nearest_food(head: dict, foods: List[dict]) -> dict:
        """
        Find the nearest food source to the snake's head.
        :param head: the coordinate of the snake's head.
        :param foods: the coordinates of the food on the board.
        :return: the coordinate of the closet food.
        """
        nearest_food = foods[0]
        nearest_path = math.inf
        for food in foods:
            path = BestMovePlanner.find_path_between_points(head, food)
            if path < nearest_path:
                nearest_path = path
                nearest_food = food
        return nearest_food

    @staticmethod
    def find_path_between_points(point_a: dict, point_b: dict) -> float:
        """
        Get the straight line path from the snake's head
        to the target.
        :param point_a: a dict coordinate containing x and y.
        :param point_b: a dict coordinate containing x and y.
        :return: the length of the path.
        """
        x_dist = point_a["x"] - point_b["x"]
        y_dist = point_a["y"] - point_b["y"]
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

    @staticmethod
    def find_scenario_closest_to_food(scenarios: List[HeadScenario],
                                      food: dict) -> HeadScenario:
        """
        Find the scenario that's closest to the food source.
        :param scenarios: the scenarios that we can take.
        :param food: the coordinates of the food on the board.
        :return: the closest scenario.
        """
        closest_scenario = scenarios[0]
        closest_path = math.inf
        for scenario in scenarios:
            path = BestMovePlanner.find_path_between_points(scenario.head_scenario, food)
            if path < closest_path:
                closest_path = path
                closest_scenario = scenario
        return closest_scenario
