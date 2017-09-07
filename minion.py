from enemy import Enemy


class Minion(Enemy):
    """
        Minion class inherits from Enemy class.
        It is similar in all forms to the enemy class except that it will 
        move towards bomberman with probability 0.8.
    """

    def __init__(self, r, c):
        Enemy.__init__(self, r, c)
        self.random_prob = 0.2
