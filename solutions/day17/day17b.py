import numpy as np

data = np.array(open('17a.txt').read().split('\n'))

target = [[195, -93], [238, -67]]
#target = [[20, -10], [30, -5]]

A = target[1][0]
xMax = A + 1
yMax = 1000

def simulate(dx, dy):
    x = 0
    y = 0
    while x <= target[1][0] and y >= target[0][1]:
        if target[0][0] <= x <= target[1][0] and target[0][1] <= y <= target[1][1]:
            return True
        x += dx
        y += dy
        dx += -1 if dx > 0 else 0
        dy += -1
    return False

count = 0
for dx in range(xMax):
    print(dx)
    for dy in range(-yMax, yMax):
        if simulate(dx, dy):
            count += 1

print('Result: ', count)
