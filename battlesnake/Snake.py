class Snake:
    def __init__(self, game_id):
        self._game_id = game_id

    @property
    def game_id(self) -> str:
        return self._game_id


