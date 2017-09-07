from board import bd
from bomberman import bman
from helper import getch
from bomb import bomb
from enemy import Enemy
from minion import Minion
from boss import Boss
from termcolor import cprint, colored
from config import LIVES_1, LIVES_2, WIN, GAME_OVER, LEVEL_1, LEVEL_2, LEVEL_3
import numpy as np
import os
import time


class Game:

    """
        A function to render (Print) the board.
    """

    def render(self):
        os.system('clear')
        print("Score: ", bd.score, " Lives: ", bman.lives, " Level: ", bd.level)
        board_mapping = {
            0: '    ',
            1: 'XXXX',
            2: '****',
            5: bomb.cur_val(),
            6: '^^^^',
            7: '^^^^',
            8: '^^^^',
        }
        """
            This loop is responsible for mapping the canvas to game_board
        """
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] == 3:
                    bd.game_area[2*row][col] = "[^^]"
                    bd.game_area[2*row+1][col] = " ][ "
                elif bd.canvas[row, col] == 4:
                    for enemy in bd.enemies:
                        if enemy.r == row and enemy.c == col:
                            if enemy.__class__.__name__ == "Enemy":
                                bd.game_area[2*row][col] = colored("<**>", 'red', attrs=['bold'])
                                bd.game_area[2*row+1][col] = colored(" () ", 'red', attrs=['bold'])
                            elif enemy.__class__.__name__ == "Minion":
                                bd.game_area[2*row][col] = colored("<**>", 'yellow', attrs=['bold'])
                                bd.game_area[2*row+1][col] = colored(" () ", 'yellow', attrs=['bold'])
                            else:
                                bd.game_area[2*row][col] = colored("<**>", 'cyan', attrs=['bold'])
                                bd.game_area[2*row+1][col] = colored(" () ", 'cyan', attrs=['bold'])
                else:
                    bd.game_area[2*row][col] = board_mapping[bd.canvas[row, col]]
                    bd.game_area[2*row+1][col] = board_mapping[bd.canvas[row, col]]

        self.__vertical_border()
        self.__vertical_border()
        for row in range(2*bd.rows):
            print('###', end='')
            for col in range(bd.columns):
                if bd.game_area[row][col] == "[^^]" or bd.game_area[row][col] == " ][ ":
                    cprint(bd.game_area[row][col], 'blue', attrs=['bold'], end='')
                elif bd.game_area[row][col] == "****":
                    cprint(bd.game_area[row][col], 'magenta', attrs=['bold'], end='')
                elif bd.game_area[row][col] == "^^^^":
                    cprint(bd.game_area[row][col], 'green', attrs=['bold'], end='')
                elif bd.game_area[row][col] == "%%%%" or "2222" == \
                        bd.game_area[row][col] or bd.game_area[row][col] == "1111" or bd.game_area[row][col] == "0000":
                    cprint(bd.game_area[row][col], 'green', attrs=['bold'], end='')
                else:
                    print(bd.game_area[row][col], end='')
            print('###')
        self.__vertical_border()
        self.__vertical_border()

    @staticmethod
    def __vertical_border():
        print('###', end='')
        for col in range(4*bd.columns):
            print('#', end='')
        print('###')

    @staticmethod
    def game_over():
        os.system('clear')
        print(GAME_OVER)
        time.sleep(2)
        print("Oops, you died. Your final score is: ", bd.score)
        time.sleep(1)
        exit()

    @staticmethod
    def game_win():
        os.system('clear')
        print(WIN)
        time.sleep(2)
        print("You Won !!!! Your final score is: ", bd.score)
        time.sleep(1)
        exit()

    @staticmethod
    def debug():
        print("bman.r: ", bman.r, " bman.c: ", bman.c)
        print("bd.explosions: ", bd.explosions)
        print("bd.is_bomb: ", bd.is_bomb)
        print("bomb.r: ", bomb.r, " bomb.c: ", bomb.c)
        print("time for explosion: ", time.time() - bomb.created_at)
        print("time: ", time.time() - beginning_time)
        print("enemies: ", bd.enemies)

    @staticmethod
    def create_enemies():
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] == 4:
                    if bd.level == 1:
                        bd.enemies.append(Enemy(row, col))
                    elif bd.level == 2:
                        rand = np.random.random_sample()
                        if rand < 0.4:
                            bd.enemies.append(Enemy(row, col))
                        else:
                            bd.enemies.append(Minion(row, col))
                    elif bd.level == 3:
                        rand = np.random.random_sample()
                        if rand < 0.2:
                            bd.enemies.append(Enemy(row, col))
                        elif rand < 0.5:
                            bd.enemies.append(Minion(row, col))
                        else:
                            bd.enemies.append(Boss(row, col))

    @staticmethod
    def decrease_lives():
        os.system('clear')
        bman.lives -= 1
        if bman.lives == 1:
            print(LIVES_1)
        elif bman.lives == 2:
            print(LIVES_2)
        time.sleep(2)
        bd.canvas[bman.r, bman.c] = 0
        bd.canvas[0, 0] = 3
        bman.r = 0
        bman.c = 0
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] >= 5:
                    bd.canvas[row, col] = 0

    @staticmethod
    def reinitialize_board():
        bd.game_area = [["aaaa" for i in range(bd.columns)] for j in range(2 * bd.rows)]
        bd.explosions = []
        bd.is_bomb = -1
        bd.enemies = []
        bd.canvas = np.zeros((bd.rows, bd.columns))
        bd.fillcanvas()
        game.create_enemies()
        bman.r = 0
        bman.c = 0
        bman.num_bombs = 1
        bomb.r = -2
        bomb.c = -2
        os.system('clear')

    """
        The function which implements the main game loop. 
        It is an infinite loop which ends only when user presses 'q'
        or game is over/won.
    """

    def game_loop(self):
        while True:
            self.render()
            key = getch()

            if key == 'a':
                if bman.c > 0:
                    if (bman.r, bman.c - 1) in bd.explosions:
                        if bman.lives > 1:
                            self.decrease_lives()
                        else:
                            self.game_over()
                    else:
                        bman.move(0, -1)
            elif key == 's':
                if bman.r < bd.rows:
                    if (bman.r + 1, bman.c) in bd.explosions:
                        if bman.lives > 1:
                            self.decrease_lives()
                        else:
                            self.game_over()
                    else:
                        bman.move(1, 0)
            elif key == 'd':
                if bman.c < bd.columns:
                    if (bman.r, bman.c + 1) in bd.explosions:
                        if bman.lives > 1:
                            self.decrease_lives()
                        else:
                            self.game_over()
                    else:
                        bman.move(0, 1)
            elif key == 'w':
                if bman.r > 0:
                    if (bman.r - 1, bman.c) in bd.explosions:
                        if bman.lives > 1:
                            self.decrease_lives()
                        else:
                            self.game_over()
                    else:
                        bman.move(-1, 0)
            elif key == 'b' and bd.is_bomb != 1:
                bman.drop_bomb()
            elif key == 'q':
                self.game_over()

            if bd.is_bomb == 1:
                bomb.update()
                bomb.update_explosion()
            elif bd.is_bomb == 0 and bd.explosions == []:
                bman.num_bombs = 1
                bomb.r = -2
                bomb.c = -2

            for enemy in bd.enemies:
                enemy.move()
                if enemy.r == bman.r and enemy.c == bman.c:
                    if bman.lives > 1:
                        self.decrease_lives()
                    else:
                        self.game_over()
                elif (enemy.r, enemy.c) in bd.explosions:
                    bd.score += 100
                    bd.enemies.remove(enemy)

            if (bman.r, bman.c) in bd.explosions or [bman.r, bman.c] in bd.enemies:
                if bman.lives > 1:
                    self.decrease_lives()
                else:
                    self.game_over()

            if not bd.enemies:
                time.sleep(1)
                if bd.level == 3:
                    self.game_win()
                else:
                    bd.level += 1
                    self.reinitialize_board()
                    if bd.level == 2:
                        print(LEVEL_2)
                    else:
                        print(LEVEL_3)
                    time.sleep(2)

game = Game()
beginning_time = time.time()
game.create_enemies()
print(LEVEL_1)
time.sleep(2)
game.game_loop()
