# https://www.youtube.com/watch?v=xDrLSOxaFrA

# disjoint set union(DSU)

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, x, y):
    parent[x] = y
    return parent


def kruskals(g_nodes, g_from, g_to, g_weight):
    parent = [i for i in range(g_nodes + 1)]
    E = [[i, j, k] for i, j, k in zip(g_from, g_to, g_weight)]
    i = e = res = 0
    E.sort(key=lambda a: a[-1])
    while e < g_nodes - 1:
        u, v, w = E[i]
        xr = find(parent, u)
        yr = find(parent, v)
        if xr != yr:
            e += 1
            res += w
            parent = union(parent, xr, yr)
        i += 1
    return res



g_nodes, g_edges = map(int, input("Enter Vertex and Edges : ").rstrip().split())  # scan numbers of nodes and edges
g_from = [0] * g_edges
g_to = [0] * g_edges
g_weight = [0] * g_edges
for i in range(g_edges):

    g_from[i], g_to[i], g_weight[i] = map(int, input("Enter Vi , Vj and Weight : ").rstrip().split())
res = kruskals(g_nodes, g_from, g_to, g_weight)
print('Result ', res)

# 4 6
# 1 2 5
# 1 3 3
# 4 1 6
# 2 4 7
# 3 2 4
# 3 4 5
# output : 12
