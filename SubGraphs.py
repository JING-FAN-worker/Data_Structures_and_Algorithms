class Graph:
#Create a graph and its structure
    def __init__(self, n):
        self.n = n
        self.graph = {i: [] for i in range(n)}
        self.visited = [False] * n
#check if there already existed a node, if there isn't a node then we need to create a new node.
    def add(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)
#We should remove the edge of both vertex
    def remove(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)
#to find the link list and put the neighbor to the same list
    def _dfs(self, vertex):
        #Go to check them one by one
        self.visited[vertex] = True
        for neighbor in self.graph[vertex]:
            #If we haven't visited this node then we begin another search
            if not self.visited[neighbor]:
                self._dfs(neighbor)
#to count how many subgraphs in the the graph
    def subgraphs(self):
        self.visited = [False] * self.n
        count = 0
        for vertex in range(self.n):
            #if there isn't a list then we should begin another one
            if not self.visited[vertex]:
                self._dfs(vertex)
                count += 1
        return count



if __name__ == "__main__":
    graph = Graph(6)
    connections = ((0, 4), (2, 1),
                   (2, 5), (3, 0),
                   (5, 1))
    for u, v in connections:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)
        
    print(graph.subgraphs())  # 1
