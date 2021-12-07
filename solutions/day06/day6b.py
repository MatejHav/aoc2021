import numpy as np

data = np.array(open('6b.txt').read().split('\n'))

days = 256
original = np.array(data[0].split(',')).astype(np.int8)

for i in range(days // 2):
    original = original - 1
    w = original == -1
    count = len(original[w])
    original[w] = 6
    original = np.append(original, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

o1 = original[:np.int64(len(original)//2)]
o2 = original[np.int64(len(original)//2):]

for i in range(days // 2, days):
    o1 = o1 - 1
    w = o1 == -1
    count = len(o1[w])
    o1[w] = 6
    o1 = np.append(o1, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

for i in range(days // 2, days):
    o2 = o2 - 1
    w = o2 == -1
    count = len(o2[w])
    o2[w] = 6
    o2 = np.append(o2, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

print(len(o1) + len(o2))
