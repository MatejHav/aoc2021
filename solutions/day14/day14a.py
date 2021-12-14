import numpy as np

data = np.array(open('14b.txt').read().split('\n'))

start = data[0]
rules = {}
steps = 40

for line in data[2:]:
    t = line.split(' -> ')
    rules[t[0]] = t[0][0] + t[1]

def score(s):
    unique, counts = np.unique(list(s), return_counts=True)
    return counts.max() - counts.min()


for step in range(steps):
    print(step)
    new_string = []
    for i in range(1, len(start)):
        pair = f'{start[i - 1]}{start[i]}'
        if pair in rules:
            pair = rules[pair]
        new_string.append(pair)
    new_string.append(start[-1])
    start = ''.join(new_string)
print(score(start))