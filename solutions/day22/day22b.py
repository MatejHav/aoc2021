import numpy as np

data = np.array(open('22a.txt').read().split('\n'))


class Cube:

    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

    def count(self):
        return abs(self.x1 - self.x0) * abs(self.y1 - self.y0) * abs(self.z1 - self.z0)


def intersect(cube1, cube2):
    x0 = min(cube1.x0, cube2.x0)
    x1 = max(cube1.x0, cube2.x0)
    y0 = min(cube1.y0, cube2.y0)
    y1 = max(cube1.y0, cube2.y0)
    z0 = min(cube1.z0, cube2.z0)
    z1 = max(cube1.z0, cube2.z0)
    one = Cube(x0, x1, y0, y1, z0, z1)
    two = Cube(x1, cube1.x1, y0, y1, z0, z1)
    three = Cube(x0, x1, y0, cube1.y0, z0, z1)
    four = Cube(x0, x1, y0, y1, z0, cube1.z1)
    res = [one]
    if x0 < x1:
        res.append(two)
    if x0 < x1:
        res.append(three)
    if x0 < x1:
        res.append(four)
    return res


cubes = []

for i, line in enumerate(data):
    print(i)
    t = line.split(' ')
    d = t[1].split(',')
    x0 = int(d[0].split('..')[0][2:])
    x1 = int(d[0].split('..')[1])
    y0 = int(d[1].split('..')[0][2:])
    y1 = int(d[1].split('..')[1])
    z0 = int(d[2].split('..')[0][2:])
    z1 = int(d[2].split('..')[1])

    temp = []
    cube = Cube(x0, x1, y0, y1, z0, z1)
    for c in cubes:
        for r in intersect(c, cube):
            temp.append(r)
    cubes = temp
    print(len(cubes))

    if t[0] == 'on':
        cubes.append(cube)

print(np.sum([c.count() for c in cubes]))
