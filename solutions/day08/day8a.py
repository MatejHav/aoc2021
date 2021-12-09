import numpy as np

data = np.array(open('8a.txt').read().split('\n'))

displays = []
count = 0
out = []
for line in data:
    t = {}
    t['in'] = line.split('|')[0].split(' ')
    t['out'] = line.split('|')[1].split(' ')
    for out in line.split('|')[1].split(' '):
        if len(out) == 2 or len(out) == 4 or len(out) == 3 or len(out) == 7:
            count += 1
    t['con'] = {}
    displays.append(t)
print(count)

