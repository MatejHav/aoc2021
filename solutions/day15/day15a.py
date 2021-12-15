import numpy as np
from queue import PriorityQueue

data = np.array(open('15a.txt').read().split('\n'))

# https://stackabuse.com/dijkstras-algorithm-in-python/
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

    def dijkstra(graph, start_vertex, end):
        D = {v: float('inf') for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            if current_vertex == end:
                break

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D


temp = []
for line in data:
    t = []
    for l in line:
        t.append(int(l))
    temp.append(t)
temp = np.array(temp)
g = Graph(temp.shape[0] * temp.shape[1])
h = temp.shape[0]
w = temp.shape[1]
for x in range(temp.shape[0]):
    for y in range(temp.shape[1]):
        if x > 0:
            g.add_edge(h * (x - 1) + y, h * x + y, temp[x, y])
            g.add_edge(h * x + y, h * (x - 1) + y, temp[x - 1, y])
        if x < h - 1:
            g.add_edge(h * (x + 1) + y, h * x + y, temp[x, y])
            g.add_edge(h * x + y, h * (x + 1) + y, temp[x + 1, y])
        if y > 0:
            g.add_edge(h * x + y - 1, h * x + y, temp[x, y])
            g.add_edge(h * x + y, h * x + y - 1, temp[x, y - 1])
        if y < w - 1:
            g.add_edge(h * x + y + 1, h * x + y, temp[x, y])
            g.add_edge(h * x + y, h * x + y + 1, temp[x, y + 1])

print(g.dijkstra(0, h * w - 1)[w * h - 1])
