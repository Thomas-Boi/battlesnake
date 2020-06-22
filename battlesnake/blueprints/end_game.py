from battlesnake.utils import get_redis
from flask import Blueprint, request, make_response

bp = Blueprint("end_game", __name__)


@bp.route("/end", methods=["POST"])
def end_game():
    """
    End a game. Remove the Snake with the corresponding
    game id.
    API: https://docs.battlesnake.com/references/api#end
    :return: empty string "".
    """
    game_id = request.get_json()["game"]["id"]
    deleted_amount = get_redis.get_redis().delete(game_id)
    response_txt = ""
    response_code = 200

    if deleted_amount == 1:
        response_txt = f"Deleted snake with id: {game_id}"
    else:
        response_txt = f"No snake was found with id: {game_id}."
        response_code = 400

    return make_response(response_txt, response_code)
