from flask import Blueprint, request
from battlesnake.Snake import Snake
from battlesnake import get_redis
import pickle

bp = Blueprint("start_game", __name__)


@bp.route("/start", methods=["POST"])
def start_game():
    """
    Start a game by creating a Snake and add it
    to the games dictionary.
    API: https://docs.battlesnake.com/references/api#start
    :return: empty string "".
    """
    try:
        game_id = request.get_json()["game"]["id"]
    except TypeError:
        # request didn't have correct json data
        return "Request didn't have the expected data and was ignored."

    redis_client = get_redis.get_redis()
    response = ""

    # test if there are any snake
    if redis_client.get(game_id) is None:
        # most cases should go here. Create a new snake and track it.
        redis_client.set(game_id, pickle.dumps(Snake()))
        response = f"New snake initialized with id: {game_id}"
    else:
        response = f"Start request invalid. There's already a snake with id: {game_id}."
    return response
