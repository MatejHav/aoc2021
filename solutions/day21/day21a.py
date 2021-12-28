import numpy as np

data = np.array(open('21a.txt').read().split('\n'))

pos1 = 5
pos2 = 0
points1 = 0
points2 = 0
n = 1
i = 0
while points1 < 1000 and points2 < 1000:
    move = 3*n + 3
    i += 3
    if n % 2 == 1:
        pos1 = (pos1 + move) % 10
        points1 += pos1 + 1
    else:
        pos2 = (pos2 + move) % 10
        points2 += pos2 + 1
    n += 3

print(points1, points2, i)
print(min(points1, points2) * i)
