from config import ROWS, COLUMNS, PERCENT_BOXES, PERCENT_ENEMIES
import numpy as np

"""
    The Board class represents the state of the board.
        0   => Air
        1   => Wall
        2   => Bricks
        3   => Bomberman
        4   => Enemies
        5   => Bombs
        6   => Explosion Complete
        > 6 => To explode
"""


class Board:
    """
        Constructor of Board class. 
        
        canvas => A numpy 2D matrix of integers which represent different characters
                  It represents the current state of game
        game_area => A list of list which is used for rendering the game
        explosions => A list of 2 element tuples storing the row, col of exploding cells
        is_bomb => Checks for existence of bomb
        enemies => A list of objects storing all the instances of various enemies in the board
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.canvas = np.zeros((rows, columns))
        self.game_area = [["aaaa" for i in range(columns)] for j in range(2*rows)]
        self.explosions = []
        self.is_bomb = -1
        self.enemies = []
        self.score = 0
        self.level = 1

    """
        Fills the canvas (Game Matrix) with all the characters
    """

    def fillcanvas(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if i + j == 0 :
                    self.canvas[i, j] = 3
                elif i % 2 and j % 2:
                    self.canvas[i, j] = 1
                elif i <= 2 and j <= 2:
                    self.canvas[i, j] = 0
                else:
                    rand = np.random.random_sample()
                    if rand < PERCENT_BOXES:
                        self.canvas[i, j] = 2
                    elif rand < PERCENT_ENEMIES[self.level]:
                        self.canvas[i, j] = 4

bd = Board(ROWS, COLUMNS)
bd.fillcanvas()