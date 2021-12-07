import numpy as np

data = np.array(open('6a.txt').read().split('\n'))

days = 256
original = np.array(data[0].split(',')).astype(np.int8)

for i in range(days // 2):
    original = original - 1
    # for j in range(len(copied)):
    #     if copied[j] == -1:
    #         copied[j] = original[j]
    #         original = np.append(original, 6)
    #         copied = np.append(copied, 8)
    w = original == -1
    count = len(original[w])
    original[w] = 6
    original = np.append(original, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

o1 = original[0::2*int(len(original)//3)]
o2 = original[2*int(len(original)//3)::len(original)]

for i in range(days // 2, days):
    o1 = o1 - 1
    # for j in range(len(copied)):
    #     if copied[j] == -1:
    #         copied[j] = original[j]
    #         original = np.append(original, 6)
    #         copied = np.append(copied, 8)
    w = o1 == -1
    count = len(o1[w])
    o1[w] = 6
    o1 = np.append(o1, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

for i in range(days // 2, days):
    o2 = o2 - 1
    # for j in range(len(copied)):
    #     if copied[j] == -1:
    #         copied[j] = original[j]
    #         original = np.append(original, 6)
    #         copied = np.append(copied, 8)
    w = o2 == -1
    count = len(o2[w])
    o2[w] = 6
    o2 = np.append(o2, [8 for j in range(count)]).astype(np.int8)
    print(f'Day {i if i >= 10 else "0" + str(i)}')

print(len(o1) + len(o2))
