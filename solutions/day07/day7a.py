import numpy as np

data = np.array(open('7b.txt').read().split('\n')[0].split(',')).astype(np.int64)

maximum = data.max()
minimum = data.min()
fuel = np.zeros((len(data), maximum - minimum))

for crab, start in enumerate(data):
    for pos in range(maximum - minimum):
        fuel[crab, pos] = abs(start - pos)

sums = np.sum(fuel, axis=0)
print(np.min(sums))


