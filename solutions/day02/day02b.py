import numpy as np

data = np.array(open('2.txt').read().split('\n'))

depth = 0
hor = 0
aim = 0

for line in data:
    l = line.split(' ')
    if l[0] == 'forward':
        hor += int(l[1])
        depth += int(l[1]) * aim
    if l[0] == 'up':
        aim -= int(l[1])
    if l[0] == 'down':
        aim += int(l[1])

print(depth * hor)