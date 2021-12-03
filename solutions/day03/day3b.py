import numpy as np

data = np.array(open('3a.txt').read().split('\n'))


def split(a, n):
    if len(a) == 1 or n == -1:
        return (len(a), a[0]) if len(a) > 0 else (0, None)

    return {'1': (len(a[[check(am, n) for am in a]]), split(a[[check(am, n) for am in a]], n - 1)),
            '0': (len(a[[not check(am, n) for am in a]]), split(a[[not check(am, n) for am in a]], n - 1))}


def check(a, n):
    return a[len(a) - 1 - n] == '1'


splits = split(data, len(data[0]) - 1)


def to_dec(a):
    a = str(a)
    s = 0
    for i in range(len(a)):
        s += int(a[i]) * 2 ** (len(a) - 1 - i)
    return s


def count_oxy(a):
    print('oxy: ', a)
    if type(a) == tuple:
        return a
    if a['1'][0] == 1 and (a['0'][0] <= 1):
        return a['1'][1]
    if a['0'][0] == 1 and a['1'][0] == 0:
        return a['0'][1]

    return count_oxy(a['1'][1] if a['1'][0] >= a['0'][0] else a['0'][1])


def count_life(a):
    print('life: ', a)
    if type(a) == tuple:
        return a
    if a['0'][0] == 1 and (a['1'][0] == 1):
        return a['0'][1]
    if a['0'][0] == 1 and a['1'][0] == 0:
        return a['0'][1]
    if a['1'][0] == 1 and a['0'][0] == 0:
        return a['1'][1]

    return count_life(a['1'][1] if a['1'][0] < a['0'][0] else a['0'][1])


oxygen = to_dec(count_oxy(splits)[1])
life = to_dec(count_life(splits)[1])

print(oxygen * life)
