class Entity:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    """
        An abstract method which is overridden by the children classes
    """

    def check_move(self, r, c):
        pass
