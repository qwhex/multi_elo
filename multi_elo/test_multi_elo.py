from random import randint
from multi_elo import EloPlayer, calc_elo

K_FACTOR = 16

def test_4_players():
    elo_players = [
        EloPlayer(place=1, elo=1200),
        EloPlayer(place=2, elo=1100),
        EloPlayer(place=3, elo=1000),
        EloPlayer(place=4, elo=1300),
    ]
    assert calc_elo(elo_players, K_FACTOR) == [1220, 1112, 1004, 1264]


def test_2_players():
    elo_players1 = [
        EloPlayer(place=1, elo=1000),
        EloPlayer(place=2, elo=2000),
    ]
    # large change in scores
    assert calc_elo(elo_players1, K_FACTOR) == [1016, 1984]

    elo_players2 = [
        EloPlayer(place=1, elo=2000),
        EloPlayer(place=2, elo=1000),
    ]
    # no change in scores
    assert calc_elo(elo_players2, K_FACTOR) == [2000, 1000]


def test_2_players_same_place():
    elo_players = [
        EloPlayer(place=1, elo=1000),
        EloPlayer(place=1, elo=2000),
    ]
    assert calc_elo(elo_players, K_FACTOR) == [1008, 1992]


def test_custom_players():
    class CustomPlayer:
        def __init__(self, place):
            self.place = place

        @property
        def elo(self):
            return 2000

    elo_players = [
        CustomPlayer(place=1),
        CustomPlayer(place=2),
    ]
    assert calc_elo(elo_players, K_FACTOR) == [2008, 1992]