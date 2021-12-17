import numpy as np

data = np.array(open('17a.txt').read().split('\n'))

target = [[195, -93], [238, -67]]
#target = [[20, -10], [30, -5]]

A = target[0][0]
xMax = A
yMax = 1000

def simulate(dx, dy):
    x = 0
    y = 0
    res = 0
    r = 0
    hit = False
    while x <= target[1][0] and y >= target[0][1]:
        if target[0][0] <= x <= target[1][0] and target[0][1] <= y <= target[1][1]:
            hit = True
            if res > r:
                r = res
        x += dx
        y += dy
        dx += -1 if dx > 0 else 0
        dy += -1
        if y > res:
            res = y
    return r

res = 0
for dx in range(xMax):
    for dy in range(yMax):
        print(dx, dy)
        r = simulate(dx, dy)
        if r > res:
            res = r

print(res)

