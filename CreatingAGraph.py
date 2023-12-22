class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add(self, u, v):
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove(self, u, v):
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def dft(self, start):
        visited = [False] * self.n
        self._dft_helper(start, visited)
        print()

    def _dft_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for neighbor in sorted(self.adj_list[vertex]):  # Sort the neighbors
            if not visited[neighbor]:
                self._dft_helper(neighbor, visited)

    def bft(self, start):
        visited = [False] * self.n
        queue = [start]
        visited[start] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in sorted(self.adj_list[vertex]):  # Sort the neighbors
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

# Example usage
if __name__ == "__main__":
    graph = Graph(8)
    connections = ((0, 6), (0, 7), (1, 0),
                   (1, 2), (2, 3), (3, 6),
                   (4, 3), (5, 4), (5, 6), 
                   (6, 1), (6, 2), (6, 7))

    for u, v in connections:
        graph.add(u, v)

    graph.dft(0)
    graph.bft(7)

    graph.remove(7, 0)
    graph.remove(5, 4)
    graph.remove(2, 1)

    graph.dft(0)
    graph.bft(7)