from entity import Entity
from board import bd
from bomb import bomb
import time


class Bomberman(Entity):
    def __init__(self, r, c):
        Entity.__init__(self, r, c)
        self.lives = 3
        self.num_bombs = 1

    """
        This method checks if a given moves is valid or not.
        Parent method has been overridden in this class
    """

    def check_move(self, dr, dc):
        if 0 <= self.r + dr < bd.rows and 0 <= self.c + dc < bd.columns:
            if bd.canvas[self.r + dr, self.c + dc] in [0, 4, 6, 7, 8]:
                return True
            return False
        return False

    """
        To move the Bomberman in whichever direction the user requires when possible
    """

    def move(self, dr, dc):
        if self.check_move(dr, dc):
            if bd.canvas[self.r, self.c] < 5:
                bd.canvas[self.r, self.c] = 0
            self.r = self.r + dr
            self.c = self.c + dc
            bd.canvas[self.r, self.c] = 3

    """
        To drop the bomb at the current coordinates of Bomberman
    """

    def drop_bomb(self):
        if self.num_bombs > 0:
            bd.canvas[self.r, self.c] = 5
            bomb.r = self.r
            bomb.c = self.c
            bomb.created_at = time.time()
            bman.num_bombs = 0
            bd.is_bomb = 1

bman = Bomberman(0, 0)
