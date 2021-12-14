import numpy as np

data = np.array(open('14b.txt').read().split('\n'))

start = data[0]
rules = {}
steps = 40
un = set()

for line in data[2:]:
    t = line.split(' -> ')
    rules[t[0]] = (t[0][0] + t[1], t[1] + t[0][1])
    un.add(t[0][0])
    un.add(t[0][1])
    un.add(t[1])

un = list(un)
pairs = {}
for one in un:
    for two in un:
        pairs[f'{one}{two}'] = 0

def score(s):
    counts = np.zeros(27)
    for key in s:
        counts[ord(key[0])-65] += s[key]
    counts[ord(start[-1]) - 65] += 1
    return counts.max() - counts[counts != 0].min()


for p in [f'{start[i - 1]}{start[i]}' for i in range(1, len(start))]:
    pairs[p] += 1

for step in range(steps):
    change = {}
    for pair in pairs:
        if pairs[pair] > 0 and pair in rules:
            one, two = rules[pair]
            if pair in change:
                change[pair] += 0
            else:
                change[pair] = 0

            if one in change:
                change[one] += pairs[pair]
            else:
                change[one] = pairs[pair]

            if two in change:
                change[two] += pairs[pair]
            else:
                change[two] = pairs[pair]
    for c in change:
        pairs[c] = change[c]
print(score(pairs))