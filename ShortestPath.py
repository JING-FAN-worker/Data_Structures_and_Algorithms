import heapq
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(n)}
    
    def add(self, u, v, w):
        self.adj[u].append((v, w))
    
    def remove(self, u, v):
        self.adj[u] = [item for item in self.adj[u] if item[0] != v]
    
    def shortest_path(self, start, end):
        distances = [float('inf')] * self.n
        distances[start] = 0
        prev = [None] * self.n
        queue = [(0, start)]
        while queue:
            dist, current_vertex = heapq.heappop(queue)
            if current_vertex == end:
                return self._reconstruct_path(prev, start, end)
            for neighbor, weight in self.adj[current_vertex]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev[neighbor] = current_vertex
                    heapq.heappush(queue, (new_dist, neighbor))
        return -1
    
    def _reconstruct_path(self, prev, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = prev[current]
        path.reverse()
        a = ''
        for i in path:
            a = a + str(i) + ' '
        b = -1
        return print(a) if path[0] == start else print(b)

if __name__ == "__main__":
    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
             (1, 4,  3), (2, 3,  7), (2, 5, 25),
             (3, 4, 12), (3, 5, 15), (3, 6,  4),
             (3, 7, 15), (3, 8, 20), (4, 7,  2),
             (5, 8,  2), (6, 7,  8), (6, 8, 13),
             (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)   # 0 2 3 6 7 9
    graph.remove(3, 6)
    graph.remove(5, 6)
    graph.shortest_path(0, 9)   # 0 2 3 5 8 9