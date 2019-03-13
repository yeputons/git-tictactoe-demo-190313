class Field:
    EMPTY, X, O = range(3)

    def __init__(self):
        self.field = [
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
        ]

    def winner(self):
        for y in range(3):
            if (self.field[y][0] == self.field[y][1] ==
                    self.field[y][2] != self.EMPTY):
                return self.field[y][0]
        for x in range(3):
            if (self.field[0][x] == self.field[1][x] ==
                    self.field[2][x] != self.EMPTY):
                return self.field[0][x]
        if (self.field[0][0] == self.field[1][1] ==
                self.field[2][2] != self.EMPTY):
            return self.field[1][1]
        if (self.field[0][2] == self.field[1][1] ==
                self.field[2][0] != self.EMPTY):
            return self.field[1][1]
