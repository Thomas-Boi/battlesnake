import pickle
from battlesnake.utils import get_redis
from flask import (
    Blueprint, request, jsonify, make_response
)
from werkzeug.exceptions import BadRequest
import traceback

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

        stringy_snake = redis_client.get(request_["game"]["id"])
        if stringy_snake is None:
            raise BadRequest("The game id you provided is invalid.")

        my_snake = pickle.loads(
            stringy_snake
        )
        next_move = my_snake.decide_next_move(
            request_["board"], snake_info=request_["you"]
        )

        return jsonify({"move": next_move})
    except AttributeError:
        return make_response(
            "Request didn't have the expected data and was ignored.",
            400
        )
    except BadRequest as e:
        traceback.print_tb(e.__traceback__, limit=5)
        print(e)
        return make_response(
            e,
            400
        )
    except Exception as e:
        traceback.print_tb(e.__traceback__, limit=5)
        print(e)
        return make_response(
            jsonify({"error": "An error has occurred. Please let the owner of this snake know."}),
            500
        )
