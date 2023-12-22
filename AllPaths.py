class Graph:
#Create a graph then we can create a structure of this graph.
    def __init__(self, n):
        self.n = n
        #put a matrix in n*n size.
        self.graph = [[float('inf')] * n for _ in range(n)]
        #same vertix to same one should be 0
        for i in range(n):
            self.graph[i][i] = 0
#add the length of the vertix to vertix 
    def add(self, u, v, w):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.graph[u][v] = w
#remove the edge between vertixs.
    def remove(self, u, v):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.graph[u][v] = float('inf')
            if u == v:
                self.graph[u][v] = 0