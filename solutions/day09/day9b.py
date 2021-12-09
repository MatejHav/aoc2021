import numpy as np

data = np.array(open('9a.txt').read().split('\n'))

array = []
for line in data:
    array.append(np.array([1 if letter == '9' else 0 for letter in line]).astype(np.int64))
array = np.array(array)

basins = []
visited = []

def find_basin(x, y):
    if x < 0 or x >= array.shape[0] or y < 0 or y >= array.shape[1] or array[x, y] == 1:
        return []

    visited.append(f'{x}, {y}')
    left = []
    right = []
    up = []
    down = []
    if f'{x-1}, {y}' not in visited:
        left = find_basin(x-1, y)
    if f'{x+1}, {y}' not in visited:
        right = find_basin(x+1, y)
    if f'{x}, {y-1}' not in visited:
        up = find_basin(x, y-1)
    if f'{x}, {y+1}' not in visited:
        down = find_basin(x, y+1)

    result = [[x, y]]
    for r in left:
        result.append(r)
    for r in right:
        result.append(r)
    for r in up:
        result.append(r)
    for r in down:
        result.append(r)

    return result


for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if f'{i}, {j}' in visited or array[i, j] == 1:
            continue
        basins.append(find_basin(i, j))

basins = sorted(basins, key=len, reverse=True)

print(len(basins[0]) * len(basins[1]) * len(basins[2]))

