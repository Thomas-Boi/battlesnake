import pickle
from battlesnake import get_redis
from flask import Blueprint, request, jsonify

bp = Blueprint("move", __name__)


@bp.route("/move", methods=["POST"])
def move():
    """
    Move the snake based on the request's current condition.
    API: https://docs.battlesnake.com/references/api#move
    :return: empty string "".
    """
    try:
        redis_client = get_redis.get_redis()
        request_ = request.get_json()
        board = request_["board"]
        game = request_["game"]
        snake_info = request_["you"]

        my_snake = pickle.loads(redis_client.get(game["id"]))
        next_move = my_snake.decide_next_move(board, snake_info)
        return jsonify({"move": next_move})
    except AttributeError:
        print("move(): Can't find a snake with that game id")
        return ""
