#!/usr/bin/env python3

from field import Field


class TestField:
    def test_winner_empty(self):
        f = Field()
        assert f.winner() is None

    def test_winner_row(self):
        f = Field()
        f.field[1][0] = Field.X
        f.field[1][1] = Field.X
        f.field[1][2] = Field.X
        assert f.winner() == Field.X
