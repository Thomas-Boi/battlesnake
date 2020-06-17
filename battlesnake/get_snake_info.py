from flask import Blueprint, send_file

bp = Blueprint("get_snake_info", __name__)


@bp.route("/", methods=["GET"])
def get_battlesnake_info():
    """
    Get information about my Battlesnake.
    API: https://docs.battlesnake.com/references/api#undefined
    :return: the battlesnake_info.json file
    """
    return send_file("battlesnake_info.json", mimetype="application/json")
