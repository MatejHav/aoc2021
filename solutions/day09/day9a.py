import numpy as np

data = np.array(open('9a.txt').read().split('\n'))

array = []
for line in data:
    array.append(np.array([letter for letter in line]).astype(np.int64))
array = np.array(array)

mins = []

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        x = i - 1
        y = j - 1
        x2 = i + 1
        y2 = j + 1
        if x < 0:
            x = 1
        if y < 0:
            y = 1
        if x2 >= array.shape[0]:
            x2 = array.shape[0] - 2
        if y2 >= array.shape[1]:
            y2 = array.shape[1] - 2

        if np.min([array[x, j], array[x2, j], array[i, y], array[i, y2]]) > array[i, j]:
            mins.append(1 + array[i, j])

print(sum(mins))