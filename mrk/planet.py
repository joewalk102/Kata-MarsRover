from typing import Optional


class Planet:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    @staticmethod
    def position_key(x: int, y: int) -> Optional[str]:
        if isinstance(x, int) and isinstance(y, int):
            return f"{x:d}:{y:d}"

    def get_coordinates(self, x: int, y: int) -> tuple:
        next_x = x % self.width
        next_y = y % self.height
        return next_x, next_y

    def set_obstacle(self, x, y):
        key = self.position_key(x, y)
        self.obstacles.add(key)
        return self.check_obstacle(x, y)

    def check_obstacle(self, x, y):
        key = self.position_key(x, y)
        return key in self.obstacles
