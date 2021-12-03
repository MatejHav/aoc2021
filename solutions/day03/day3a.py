import numpy as np

data = np.array(open('3a.txt').read().split('\n'))

gamma = 0
epsilon = 0
usage = []
for i in range(len(data[0])):
    usage.append([0, 0])

for line in data:
    for i in range(len(line)):
        if line[i] == '1':
            usage[i][1] += 1
        else:
            usage[i][0] += 1

for i in range(len(usage)):
    if usage[i][0] >= usage[i][1]:
        epsilon += 2**(len(usage) - 1 - i)
    else:
        gamma += 2**(len(usage) - 1 - i)

print(gamma * epsilon)