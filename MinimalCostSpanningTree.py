class Graph:
    def __init__(self, n):
        #This is the constructor for the Graph class. It initializes a new Graph instance.n is the number of vertices in the graph.
        self.v = n
        #Stores the number of vertices in the graph.
        self.adjMatrix = [[0] * n for _ in range(n)]
        #Creates an n x n adjacency matrix to represent the graph. Initially, all values are set to 0, indicating no edges between any vertices


    def add(self, u, v, w):
        if 0 <= u < self.v and 0 <= v < self.v:
            #Sets the weight w for the edge between vertices u and v. Since it's an undirected graph, both u, v and v, u are set.
            self.adjMatrix[u][v] = w
            self.adjMatrix[v][u] = w

    def remove(self, u, v):
        if 0 <= u < self.v and 0 <= v < self.v:
            #Sets the corresponding values in the adjacency matrix back to 0, effectively removing the edge.
            self.adjMatrix[u][v] = 0
            self.adjMatrix[v][u] = 0

    def min_expense(self):
        visited = [False] * self.v
        min_cost = 0
        #Initializes a priority queue (implemented as a list), used for selecting the next vertex to visit based on the lowest weight (or cost).

        priority_queue = [(0, 0, 0)]

        while priority_queue:
            #This is where the core logic for calculating the minimum expense is implemented.
#It pops an element from the priority queue, checks if the vertex has been visited, and if not, adds its weight to the total cost.
#It then iterates through all adjacent vertices, adding them to the priority queue if they haven't been visited.
#The priority queue is sorted by weight, ensuring that the vertex with the lowest weight is processed next.
            weight, current, parent = priority_queue.pop(0)
            if not visited[current]:
                visited[current] = True
                min_cost += weight
                for i in range(self.v):
                    if self.adjMatrix[current][i] > 0 and not visited[i]:
                        priority_queue.append((self.adjMatrix[current][i], i, current))
                priority_queue.sort(key=lambda x: x[0])

        return min_cost


if __name__ == "__main__":
    graph = Graph(6)
    connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.min_expense())  # 15

    graph.remove(2, 3)

    print(graph.min_expense())  # 16
