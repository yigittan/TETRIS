from grid import OccupiedPositionException
from grid import TetrisGrid
from grid import TetrisVirtualGrid
from shape import Shape
from shape import create_shape
import random

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (0, 0, 0)


class Tetris:
    def __init__(self) -> None:
        self.grid = TetrisGrid(10, 10)
        self.virtual_grid = TetrisVirtualGrid(10, 10, self.grid.sync)
        self.shape_generator = RandomShapeGenerator(0, 4)

        self.active_shape: Shape = self.shape_generator.generate()
        self.held_shape: Shape = None

        self.score = 0
        self.level = 0

    def play(self) -> None:
        """play starts the game loop
        Initialize the grid and the active shape
        Start gravity thread to move the active shape down
        """
        pass

    def gameover(self) -> None:
        """gameover ends the game, output the score and level"""
        pass

    def move_left(self):
        """move the active shape left direction"""
        try:
            self.virtual_grid.relocate_shape(self.active_shape, 0, -1)
        except OccupiedPositionException:
            pass

    def move_right(self):
        """move the active shape right direction"""
        try:
            self.virtual_grid.relocate_shape(self.active_shape, 0, 1)
        except OccupiedPositionException:
            pass

    def move_down(self):
        """move the active shape down direction"""
        try:
            self.virtual_grid.relocate_shape(self.active_shape, 1, 0)
        except OccupiedPositionException:
            self.active_shape = self.shape_generator.generate()
            self.virtual_grid.add_shape(self.active_shape)

    def move_ground(self):
        """move the active shape to the ground"""
        try:
            while True:
                self.virtual_grid.relocate_shape(self.active_shape, 1, 0)
        except OccupiedPositionException:
            self.active_shape = self.shape_generator.generate()
            self.virtual_grid.add_shape(self.active_shape)

    def hold(self) -> None:
        """hold the active shape, If there is already a held shape, swap them"""
        try:
            # create tmp held shape variable to not set held shape when replace fails
            tmp_held_shape = self.held_shape
            if tmp_held_shape is None:
                tmp_held_shape = self.shape_generator.generate()

            self.virtual_grid.replace_shape(self.active_shape, tmp_held_shape)

            self.held_shape = tmp_held_shape
            self.active_shape, self.held_shape = self.held_shape, self.active_shape
        except OccupiedPositionException:
            pass


class RandomShapeGenerator:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.shapes = ['T', "Z", "L", "I", "S"]
        self.colors = [RED, BLUE, YELLOW, WHITE]

    def generate(self) -> Shape:
        shape_type = random.choice(self.shapes)
        shape_color = random.choice(self.colors)

        return create_shape(shape_type, self.row, self.col, shape_color)



if __name__ == "__main__":
    print('hello world')
