from enemy import Enemy
from bomb import bomb
from bomberman import bman


class Boss(Enemy):
    """
        Minion class inherits from Enemy class.
        It will move away from the bomb and nearer to the enemy with a probability 0.9
        It uses a heuristic such that the best possible move is played by the enemy
    """
    def __init__(self, r, c):
        Enemy.__init__(self, r, c)
        self.random_prob = 0.1

    """
        It overrides the best direction method of Enemy class which it inherits
    """

    def best_direction(self):
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        manhattan_dis = 1000
        final_dir = [0, 0]
        for pos in range(4):
            if self.check_move(dr[pos], dc[pos]):
                cur_bomb_dis = abs(bomb.r - self.r - dr[pos]) + abs(bomb.c - self.c - dc[pos])
                cur_bomberman_dis = abs(bman.r - self.r - dr[pos]) + abs(bomb.c - self.c - dc[pos])
                cur_dis = 10/cur_bomb_dis + cur_bomberman_dis/10
                if cur_dis <= manhattan_dis:
                    manhattan_dis = cur_dis
                    final_dir = [dr[pos], dc[pos]]
        return final_dir
