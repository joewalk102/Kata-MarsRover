from mrk import Planet


class Rover:
    def __init__(self, x: int, y: int, orientation: str, planet: Planet):
        self.x = x
        self.y = y
        self.current_bearing = orientation
        self.planet = planet

    def _action_turn(self, delta: str) -> bool:
        # No checks needed, perform turn.
        self.current_bearing = delta
        return True

    def _action_move(self, delta: list) -> bool:
        # Get coordinates of the proposed move.
        next_x, next_y = self.planet.get_coordinates(self.x + delta[0], self.y + delta[1])
        # Check for obstacles at the new location.
        if self.planet.check_obstacle(next_x, next_y):
            return False
        # If there is no obstacle, move.
        self.x = next_x
        self.y = next_y
        return True

    def _decode(self, command_key: str) -> tuple:
        command = self.commands[command_key]
        delta = self.movement_keys[self.current_bearing][command_key]
        return command, delta

    def move(self, command_list: list) -> bool:
        if set(command_list) - {"F", "B", "L", "R"}:
            # There should be nothing in `command_list` that is not
            # in the second set. Only "FBLR" commands are supported.
            return False
        for command_key in command_list:
            command_key = command_key.upper()
            command_fn, delta =  self._decode(command_key)
            if not command_fn(self, delta):
                return False
        return True

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
