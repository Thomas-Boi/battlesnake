from battlesnake import get_redis
import pickle
from flask import Blueprint, request, g

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
    response = ""
    if deleted_amount == 1:
        response = f"Deleted snake with id: {game_id}"
    else:
        response = f"No snake was found with id: {game_id}."
    return response
