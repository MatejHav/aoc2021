import numpy as np

data = np.array(open('13b.txt').read().split('\n'))

dots = []
folds = []
array = []
for line in data:
    if ',' in line:
        dots.append(np.array(line.split(',')).astype(np.int64))
    if 'fold' in line:
        t = line.split(' ')[2]
        folds.append(np.array([0 if t.split('=')[0] == 'x' else 1, np.int64(t.split('=')[1])]))
dots = np.array(dots)
max_x = np.max([t[0] for t in dots])
max_y = np.max([t[1] for t in dots])
array = np.zeros((max_x + 1, max_y + 1))
for dot in dots:
    array[dot[0], dot[1]] = 1


def fold(axis, value):
    if axis == 1:
        for x in range(value, array.shape[0]):
            for y in range(array.shape[1]):
                array[value - x][y] = min(1, array[x][y] + array[value - x][y])
                array[x][y] = 0
    if axis == 0:
        for x in range(array.shape[0]):
            for y in range(value, array.shape[1]):
                array[x][value - y] = min(1, array[x][y] + array[x][value - y])
                array[x][y] = 0

fold(folds[0][0], folds[0][1])
print(np.sum(array))
