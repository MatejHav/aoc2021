import numpy as np

data = np.array(open('13c.txt').read().split('\n'))

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

def fold(dots, axis, value):
    check = set()
    for dot in dots:
        if dot[axis] > value:
            dot[axis] = value - abs(value - dot[axis])
        check.add(f'{dot[0]},{dot[1]}')


    return np.array([np.array(d.split(',')).astype(np.int64) for d in list(check)])

for f in folds:
    dots = fold(dots, f[0], f[1])
max_x = np.max([t[0] for t in dots]) + 1
max_y = np.max([t[1] for t in dots]) + 1
res = ''
check = [f'{dot[0]},{dot[1]}' for dot in dots]
for y in range(- 2, max_y + 2):
    for x in range(-2, max_x + 2):
        if f'{x},{y}' in check:
            res += '#'
        else:
            res += '_'
    res += '\n'
print(res)