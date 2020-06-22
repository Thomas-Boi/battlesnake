from flask import Flask


def create_app(test_config=None):
    # init Flask app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is not None:
        app.config.from_mapping(test_config)

    from battlesnake.blueprints import (
        start_game, move,
        get_snake_info, end_game
    )
    app.register_blueprint(get_snake_info.bp)
    app.register_blueprint(start_game.bp)
    app.register_blueprint(end_game.bp)
    app.register_blueprint(move.bp)

    return app
