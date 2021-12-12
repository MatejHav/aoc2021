import numpy as np

data = np.array(open('11a.txt').read().split('\n'))

octopus = np.zeros((10, 10))
steps = 100
flashes = 0

for x, line in enumerate(data):
    for y, digit in enumerate(line):
        octopus[x, y] = int(digit)

for step in range(steps):
    visited = list()
    while len(visited) != len(octopus[octopus == 9]):
        indices = zip(*np.where(octopus == 9))
        for index in indices:
            oc = octopus[index[0], index[1]]
            if index not in visited:
                visited.append(index)
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if index[0] + dx < 0 or index[0] + dx >= 10 or index[1] + dy < 0 or index[1] + dy >= 10 \
                                or (dx == 0 and dy == 0):
                            continue
                        octopus[index[0] + dx, index[1] + dy] = min(9, octopus[index[0] + dx, index[1] + dy] + 1)
    flashes += len(visited)
    octopus = octopus + 1
    for index in visited:
        octopus[index[0], index[1]] = 0


print(flashes)
