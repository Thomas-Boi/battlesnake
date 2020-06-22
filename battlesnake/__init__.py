from flask import Flask, request
from battlesnake.Snake import Snake
from typing import Dict


def create_app(test_config=None):
    # init Flask app
    app = Flask(__name__, instance_relative_config=True)

    # tracks the games that are being run
    games: Dict[str, Snake] = {}

    if test_config is not None:
        app.config.from_mapping(test_config)

    from . import get_snake_info, start_game
    app.register_blueprint(get_snake_info.bp)
    app.register_blueprint(start_game.bp)


    return app
