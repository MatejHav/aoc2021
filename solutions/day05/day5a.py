import numpy as np

data = np.array(open('5a.txt').read().split('\n'))

lines = list()
x = list()
y = list()
for line in data:
    f = line.split(' -> ')
    x1 = int(f[0].split(',')[0])
    y1 = int(f[0].split(',')[1])
    x2 = int(f[1].split(',')[0])
    y2 = int(f[1].split(',')[1])
    if True:
        lines.append([(x1, y1), (x2, y2)])
        x.append(x1)
        x.append(x2)
        y.append(y1)
        y.append(y2)

x = np.array(x)
y = np.array(y)
output = np.zeros((x.max() + 1, y.max() + 1))
for line in lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x = x1
    y = y1
    x2 = line[1][0]
    y2 = line[1][1]
    dx = 0 if x1 == x2 else 1 if x1 < x2 else -1
    dy = 0 if y1 == y2 else 1 if y1 < y2 else -1
    #print(f'START: {x1}, {y1} -> {x2}, {y2}')
    while abs(x) != x2 or abs(y) != y2:
        output[int(x), int(y)] += 1
        x += dx
        y += dy
        #print(x, y)
    output[int(x), int(y)] += 1
print(len(output[output >= 2]))
