from kata.planet import Planet


class Rover:
    def __init__(self, x: int, y: int, orientation: str, planet: Planet):
        self.x = x
        self.y = y
        self.bearing = orientation
        self.planet = planet

    def _action_turn(self, delta: str) -> bool:
        self.bearing = delta
        return True

    def _action_move(self, delta: list) -> bool:
        next_x, next_y = self.planet.get_coordinates(self.x + delta[0], self.y + delta[1])
        if not self.planet.check_obstacle(next_x, next_y):
            self.x = next_x
            self.y = next_y
            return True
        return False

    def _decode(self, command_key: str) -> bool:
        command = self.commands[command_key]
        delta = self.movement_keys[self.bearing][command_key]
        return command(self, delta)

    def move(self, commands: list) -> bool:
        for command in commands:
            if isinstance(command, str):
                command = command.upper()
                return self._decode(command)

    # commands to dispatch for each move key
    commands = {
        'F': _action_move,
        'B': _action_move,
        'R': _action_turn,
        'L': _action_turn
    }

    # Keys for actions to perform, based on current bearing
    movement_keys = {
        'N': {"F": [0, 1], "B": [0, -1], "L": "W", "R": "E"},
        'S': {"F": [0, -1], "B": [0, 1], "L": "E", "R": "W"},
        'E': {"F": [1, 0], "B": [-1, 0], "L": "N", "R": "S"},
        'W': {"F": [-1, 0], "B": [1, 0], "L": "S", "R": "N"}
    }
