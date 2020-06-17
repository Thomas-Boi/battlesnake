from . import Snake
import pickle
from . import get_redis
from flask import Blueprint, request

bp = Blueprint("move", __name__)


@bp.route("/move", methods=["POST"])
def move():
    """
    Move the snake based on the request's current condition.
    API: https://docs.battlesnake.com/references/api#move
    :return: empty string "".
    """
