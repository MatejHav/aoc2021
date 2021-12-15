import numpy as np
from queue import PriorityQueue

data = np.array(open('15b.txt').read().split('\n'))


from collections import defaultdict
from heapq import *

# https://gist.github.com/kachayev/5990802
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None


temp = []
for factor in range(5):
    for line in data:
        t = []
        for l in line:
            t.append((int(l) + factor) if int(l) + factor <= 9 else (int(l) + factor) % 10 + 1)
        for l in line:
            t.append((int(l) + factor + 1) if int(l) + factor + 1 <= 9 else (int(l) + factor + 1) % 10 + 1)
        for l in line:
            t.append((int(l) + factor + 2) if int(l) + factor + 2 <= 9 else (int(l) + factor + 2) % 10 + 1)
        for l in line:
            t.append((int(l) + factor + 3) if int(l) + factor + 3 <= 9 else (int(l) + factor + 3) % 10 + 1)
        for l in line:
            t.append((int(l) + factor + 4) if int(l) + factor + 4 <= 9 else (int(l) + factor + 4) % 10 + 1)
        temp.append(t)
temp = np.array(temp)
g = []
h = temp.shape[0]
w = temp.shape[1]
for x in range(temp.shape[0]):
    for y in range(temp.shape[1]):
        if x > 0:
            g.append((h * (x - 1) + y, h * x + y, temp[x, y]))
            g.append((h * x + y, h * (x - 1) + y, temp[x - 1, y]))
        if x < h - 1:
            g.append((h * (x + 1) + y, h * x + y, temp[x, y]))
            g.append((h * x + y, h * (x + 1) + y, temp[x + 1, y]))
        if y > 0:
            g.append((h * x + y - 1, h * x + y, temp[x, y]))
            g.append((h * x + y, h * x + y - 1, temp[x, y - 1]))
        if y < w - 1:
            g.append((h * x + y + 1, h * x + y, temp[x, y]))
            g.append((h * x + y, h * x + y + 1, temp[x, y + 1]))

print(dijkstra(g, 0, w * h - 1)[0])
