from flask import Flask, request
from battlesnake.Snake import Snake
from typing import Dict

# init Flask app
app = Flask(__name__)

# tracks the games that are being run
games: Dict[str, Snake] = {}


@app.route("/", methods=["GET"])
def get_battlesnake_info():
    """
    Get information about my Battlesnake.
    :return: the battlesnake_info.json file
    """
    with open("./battlesnake_info.json", "r") as info:
        return info.read()


@app.route("/start", methods=["POST"])
def start_game():
    """
    Start a game by creating a Snake and add it
    to the games dictionary.
    :return: None.
    """
    game_id = request.get_json()["game"]["id"]
    try:
        # test if there any snake
        any_snake = games[game_id]
        if type(any_snake) == Snake:
            print(f"Start game request invalid: There's already a snake with id: {game_id}.")
    except KeyError:
        # most cases should go here. Create a new snake and track it.
        games[game_id] = Snake(game_id)
    finally:
        return ""


@app.route("/end", methods=["POST"])
def end_game():
    """
    End a game. Remove the Snake with the corresponding
    game id.
    :return: None.
    """
    game_id = request.get_json()["game"]["id"]
    try:
        del games[game_id]
    except KeyError:
        print(f"End game request invalid: There is no Snake with that id {game_id}")
    finally:
        return ""


if __name__ == "__main__":
    app.run(debug=True)
