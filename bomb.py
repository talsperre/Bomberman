from board import bd
from entity import Entity
from config import EXPLODE_TIME
import time

"""
    This class represents a Bomb.
    It inherits from the Entity class.
"""


class Bomb(Entity):
    """
        Constructor of Bomb class
        
        created_at => Stores the time when it was created
        explode_time => The time it takes for the bomb to explode
    """

    def __init__(self, r, c):
        Entity.__init__(self, r, c)
        self.created_at = time.time()
        self.explode_time = EXPLODE_TIME

    """
        This method checks if a given moves is valid or not.
        Parent method has been overridden in this class
    """

    def check_move(self, dr, dc):
        if 0 <= self.r + dr < bd.rows and 0 <= self.c + dc < bd.columns:
            if bd.canvas[self.r + dr, self.c + dc] in [0, 2, 3, 4]:
                return True
            return False
        return False

    """
        This method marks all the positions that are going to explode on the board
    """

    def explode(self):
        bd.canvas[self.r, self.c] = 6
        bd.explosions.append((self.r, self.c))
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        for pos in range(4):
            if self.check_move(dr[pos], dc[pos]):
                if bd.canvas[self.r + dr[pos], self.c + dc[pos]] == 2:
                    bd.score += 20
                bd.canvas[self.r + dr[pos], self.c + dc[pos]] = 6
                bd.explosions.append((self.r + dr[pos], self.c + dc[pos]))

    """
        It calls the explode method when the time after bomb drop > explode_time
    """

    def update(self):
        if time.time() - self.created_at > self.explode_time:
            self.explode()

    """
        It updates and removes the explosions from the board after 3 frames
    """

    @staticmethod
    def update_explosion():
        for explosion in bd.explosions:
            bd.canvas[explosion[0], explosion[1]] += 1
            if bd.canvas[explosion[0], explosion[1]] >= 8:
                bd.canvas[explosion[0], explosion[1]] = 0
                bd.explosions = []
                bd.is_bomb = 0

    def cur_val(self):
        cur_time = int(time.time() - self.created_at)
        if cur_time == 1:
            return "0000"
        elif cur_time == 0:
            return "1111"
        else:
            return "%%%%"

bomb = Bomb(-2, -2)
