from flask import Blueprint, request, make_response
from battlesnake.utils.Snake import Snake
from battlesnake.utils import get_redis
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
        request_ = request.get_json()
        game_id = request_["game"]["id"]
        board = request_["board"]
    except TypeError:
        # request didn't have correct json data
        return make_response(
            "Request didn't have the expected data and was ignored.",
            400
        )
    except KeyError as err:
        return make_response(
            f"Request need to have the key: {err}.",
            400
        )

    redis_client = get_redis.get_redis()
    response_txt = ""
    response_code = 200

    # test if there are any snake
    if redis_client.get(game_id) is None:
        # most cases should go here. Create a new snake and track it.
        pickled_snake = pickle.dumps(Snake(board))
        redis_client.set(game_id, pickled_snake)
        response_txt = f"New snake initialized with id: {game_id}"
    else:
        response_txt = f"Start request invalid. There's already a snake with id: {game_id}."
        response_code = 400

    return make_response(response_txt, response_code)
