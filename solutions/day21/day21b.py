import numpy as np

wins = {0: 0, 1: 0}


def play(pos1, pos2, points1, points2, turn, factor):
    if points1 >= 21:
        wins[0] += factor
        return
    if points2 >= 21:
        wins[1] += factor
        return
    if turn % 2 == 1:
        for res in range(3, 10):
            # 3 - 1
            # 4 - 3
            # 5 - 6
            # 6 - 7
            # 7 - 6
            # 8 - 3
            # 9 - 1
            f = 1 if res == 3 or res == 9 else 3 if res == 4 or res == 8 else 6 if res == 5 or res == 7 else 7
            play(pos1 + res, pos2, points1 + (pos1 + res) % 10, points2, turn + 1, factor * f)
        return
    for res in range(3, 10):
        f = 1 if res == 3 or res == 9 else 3 if res == 4 or res == 8 else 6 if res == 5 or res == 7 else 7
        play(pos1, pos2 + res, points1, points2 + (pos2 + res) % 10, turn + 1, factor * f)


def solve():
    pos1 = 3  # 5
    pos2 = 7  # 0
    play(pos1, pos2, 0, 0, 1, 1)
    return max(wins[0], wins[1])


print(solve())
