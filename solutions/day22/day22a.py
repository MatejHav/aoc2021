import numpy as np

data = np.array(open('22b.txt').read().split('\n'))

res = np.zeros((101, 101, 101))

for line in data:
    t = line.split(' ')
    d = t[1].split(',')
    x0 = int(d[0].split('..')[0][2:])
    x1 = int(d[0].split('..')[1])
    y0 = int(d[1].split('..')[0][2:])
    y1 = int(d[1].split('..')[1])
    z0 = int(d[2].split('..')[0][2:])
    z1 = int(d[2].split('..')[1])

    if x0 < -50 or x1 > 50 or y0 < -50 or y1 > 50 or z0 < -50 or z1 > 50:
        continue

    for x in range(50 + x0, 50 + x1 + 1):
        for y in range(50 + y0, 50 + y1 + 1):
            for z in range(50 + z0, 50 + z1 + 1):
                res[x, y, z] = 1 if t[0] == 'on' else 0

print(np.sum(res))
