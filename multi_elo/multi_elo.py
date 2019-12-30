from math import pow
from collections import namedtuple, defaultdict
from itertools import permutations
from random import randint


EloPlayer = namedtuple('EloPlayer', 'place elo')


def _calc_s(player1, player2):
    if player1.place < player2.place:
        return 1.0
    if player1.place == player2.place:
        return 0.5
    return 0.0


def _calc_ea(player1, player2):
    return 1 / (1.0 + pow(10.0, (player2.elo - player1.elo) / 400.0))


def _calc_elo_change(player1, player2, k):
    s = _calc_s(player1, player2)
    ea = _calc_ea(player1, player2)
    return round(k * (s - ea))


def calc_elo(players, k=32):
    n = len(players)
    player_to_player = list(permutations(range(n), 2))

    elo_changes = defaultdict(int)
    for i, j in player_to_player:
        elo_changes[i] += _calc_elo_change(players[i], players[j], k)

    return [players[i].elo + elo_changes[i] for i in range(n)]
