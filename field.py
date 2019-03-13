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
            if (self.field[y][0] != self.EMPTY and
                all(self.field[y][x] == self.field[y][x]
                    for x in range(3))):
                return self.field[y][0]
        for x in range(3):
            if (self.field[0][x] != self.EMPTY and
                all(self.field[y][x] == self.field[y][x]
                    for y in range(3))):
                return self.field[0][x]
        if (self.field[0][0] == self.field[1][1] ==
                self.field[2][2] != self.EMPTY):
            return self.field[1][1]
        if (self.field[0][2] == self.field[1][1] ==
                self.field[2][0] != self.EMPTY):
            return self.field[1][1]
