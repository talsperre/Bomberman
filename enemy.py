from entity import Entity
from board import bd
from bomberman import bman
import numpy as np


class Enemy(Entity):
    def __init__(self, r, c):
        Entity.__init__(self, r, c)
        self.random_prob = 0.6

    """
        This method checks if a given moves is valid or not.
        Parent method has been overridden in this class.
    """

    def check_move(self, dr, dc):
        if 0 <= self.r + dr < bd.rows and 0 <= self.c + dc < bd.columns:
            if bd.canvas[self.r + dr, self.c + dc] in [0, 3, 6, 7, 8]:
                return True
            return False
        return False

    """
        To move the Enemy in random direction with probability (0.6) and towards the bomberman
        with probability 0.4.
    """

    def move(self):
        if bd.canvas[self.r, self.c] < 5:
            bd.canvas[self.r, self.c] = 0
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        if np.random.random_sample() < self.random_prob:
            rand = np.random.randint(4)
            if self.check_move(dr[rand], dc[rand]):
                self.r = self.r + dr[rand]
                self.c = self.c + dc[rand]
        else:
            dz = self.best_direction()
            self.r = self.r + dz[0]
            self.c = self.c + dz[1]
        if (self.r, self.c) not in bd.explosions:
            bd.canvas[self.r, self.c] = 4

    """
        Goes through all the directions and finds the best direction (Nearest to Bomberman)
    """

    def best_direction(self):
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        manhattan_dis = 10000
        final_dir = [0, 0]
        for pos in range(4):
            if self.check_move(dr[pos], dc[pos]):
                cur_dis = abs(bman.r - self.r - dr[pos]) + abs(bman.c - self.c - dc[pos])
                if cur_dis <= manhattan_dis:
                    manhattan_dis = cur_dis
                    final_dir = [dr[pos], dc[pos]]
        return final_dir
