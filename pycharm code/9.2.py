class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        total = 0
        for u, v, weight in result:
            print("%d to %d = %d" % (u, v, weight))
            total = total+weight
        print("The Total Cost : ",total)


vertex = int(input("Enter Total Vertex : "))
edges = int(input("Enter Total Edges : "))
g = Graph(vertex)
for i in range(edges):
    data = [int(x) for x in input("Enter Vi , Vj and Weight : ").split()]
    g.add_edge(data[0], data[1], data[2])
g.kruskal_algo()

# 5 7
# 0 1 4
# 0 2 8
# 1 2 1
# 1 3 3
# 2 3 7
# 2 4 3
# 3 4 8
# Output = 11