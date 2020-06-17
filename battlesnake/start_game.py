from flask import Blueprint, request
from battlesnake import Snake
from . import get_redis
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
    game_id = request.get_json()["game"]["id"]
    redis_client = get_redis.get_redis()

    # test if there are any snake
    if type(redis_client.get(game_id)) is None:
        # most cases should go here. Create a new snake and track it.
        redis_client.set(game_id, pickle.dumps(Snake(game_id)))
    else:
        print(f"Start game request invalid: There's already a snake with id: {game_id}.")
    return ""
