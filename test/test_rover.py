import random
from unittest import TestCase

from mrk import Rover, Planet


class BaseRoverTest(TestCase):
    def setUp(self) -> None:
        self.planet = Planet(5, 5)
        self.rover = Rover(0, 0, "N", self.planet)


class TestRoverActionTurn(BaseRoverTest):
    def test_bearing_updated(self):
        self.rover._action_turn("W")
        assert self.rover.current_bearing == "W"


class TestRoverActionMove(BaseRoverTest):
    def test_move_with_no_obstacle(self):
        assert self.rover._action_move([1, 0]) is True
        assert self.rover.x == 1
        assert self.rover.y == 0
        assert self.rover._action_move([0, 1]) is True
        assert self.rover.x == 1
        assert self.rover.y == 1
        assert self.rover._action_move([-1, 0]) is True
        assert self.rover.x == 0
        assert self.rover.y == 1
        assert self.rover._action_move([0, -1]) is True
        assert self.rover.x == 0
        assert self.rover.y == 0

    def test_move_with_obstacle(self):
        self.planet.set_obstacle(1, 0)
        assert self.planet.check_obstacle(1, 0)
        assert self.rover._action_move([1, 0]) is False


class TestRoverDecode(BaseRoverTest):
    def test_move_action(self):
        command, delta = self.rover._decode("F")
        assert command.__name__ == self.rover._action_move.__name__
        assert delta == [0, 1]

    def test_turn_action(self):
        command, delta = self.rover._decode("L")
        assert command.__name__ == self.rover._action_turn.__name__
        assert delta == "W"


class TestRoverMove(BaseRoverTest):
    def test_all_valid_actions(self):
        commands = ["F", "B", "L", "R"]
        assert self.rover.move(
            [random.choice(commands) for _ in range(1000)]
        ) is True

    def test_command_letter_not_supported(self):
        assert self.rover.move(["G"]) is False
        assert self.rover.x == 0 and self.rover.y == 0 and self.rover.current_bearing == "N"
        assert self.rover.move(["F","F","G"]) is False
        assert self.rover.x == 0 and self.rover.y == 0 and self.rover.current_bearing == "N"
        assert self.rover.move(["F","G","R"]) is False
        assert self.rover.x == 0 and self.rover.y == 0 and self.rover.current_bearing == "N"

    def test_obstacle_found(self):
        self.planet.set_obstacle(0, 1)
        assert self.rover.move(["F"]) is False
