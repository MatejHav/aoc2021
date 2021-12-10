import numpy as np

data = np.array(open('6a.txt').read().split('\n'))

days = 256
original = np.array(data[0].split(',')).astype(np.int8)

count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in original:
    count[fish] += 1

for i in range(days):
    temp = count[0]
    count[0] = count[1]
    count[1] = count[2]
    count[2] = count[3]
    count[3] = count[4]
    count[4] = count[5]
    count[5] = count[6]
    count[6] = count[7] + temp
    count[7] = count[8]
    count[8] = temp

print(sum([count[k] for k in count]))
