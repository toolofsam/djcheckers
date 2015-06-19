"""
This file handles positioning and movements 
"""
from game_settings import GameSettings
settings = GameSettings()


def where_can_i_go(grid, n):
    """Determines the blocks (and numbers that are around a specified block."""
    _max = (settings.per_row ** 2)

    # start with a empty list
    around_me = []
    l = [-1, -9, -8, -7, 1, 7, 8, 9]
    for i in l:
        if not n+i > settings.per_row ** 2 and not n+i < int(0):
            around_me.append(n + i)

    return around_me

