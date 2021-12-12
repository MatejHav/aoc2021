import numpy as np

data = np.array(open('12a.txt').read().split('\n'))

edges = {}

for line in data:
    s = line.split('-')
    if s[0] not in edges:
        edges[s[0]] = set()
    if s[1] not in edges:
        edges[s[1]] = set()
    edges[s[0]].add(s[1])
    edges[s[1]].add(s[0])


def dfs(current, visited1, visited2, twice):
    if current == 'end':
        return 1

    if current.islower():
        if current == 'start':
            visited1.add(current)
            visited2.add(current)
        else:
            if current in visited1:
                visited2.add(current)
                twice = True
            else:
                visited1.add(current)

    res = 0
    for node in edges[current]:
        if node.isupper() or (not twice and node not in visited2) or (node not in visited1):
            res += dfs(node, visited1.copy(), visited2.copy(), twice)
    return res


print(dfs('start', set(), set(), False))
