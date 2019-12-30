multi_elo
=========

Python `ELO`_ score calculator for more than two players. It can be used
e.g. for a 4 player multiplayer match and for team-based games as well.

Install
-------

``pip install multi_elo``

Compatibility
-------------

Python 3.5+

Usage
-----

.. code:: python

   from random import randint
   from multi_elo import EloPlayer, calc_elo

   # Generate players with random ELO.
   # It can be a list of any elements having the `place` and `elo` properties.
   elo_players = [EloPlayer(place=place, elo=randint(1200, 1800))
                  for place in range(1, 5)]

   print('Original ELO scores:')
   for player in enumerate(elo_players, start=1):
       print(f'{i}: #{player.place} ({player.elo})')

   # Set the K factor (optional)
   k_factor = 16

   # Calculate new ELO scores
   new_elos = calc_elo(elo_players, k_factor)

   print('\nNew ELO scores:')
   for i, new_elo in enumerate(new_elos, start=1):
       print(f'{i}: {new_elo}')

Development
===========

.. code:: bash

   # install dependencies
   pip install requirements_dev.txt
   # run tests with all of the supported python interpreters
   tox
   # or only with the currently active python interpreter
   pytest

.. _ELO: https://en.wikipedia.org/wiki/Elo_rating_system