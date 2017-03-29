multi\_elo
==========

Python ELO score calculator for more than two players

Usage:
------

.. code:: python

    from random import randint
    from multi_elo import EloPlayer, calc_new_elos

    # generating random players
    elo_players = [EloPlayer(place=place, elo=randint(1200, 1800))
                   for place in range(1, 5)]

    print('Original ELO scores:')
    for place, player in enumerate(elo_players, start=1):
        print('{}: {}'.format(place, player.elo))

    # setting the K factor
    k_factor = 16

    # calculating new ELO scores
    new_elos = calc_new_elos(elo_players, k_factor)

    print('\nNew ELO scores:')
    for place, new_elo in enumerate(new_elos, start=1):
        print('{}: {}'.format(place, new_elo))

