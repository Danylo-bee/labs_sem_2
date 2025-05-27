def read_edges_from_csv(filename):
    edges = []

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            u, v, w = parts[0].strip(), parts[1].strip(), int(parts[2])
            edges.append((w, u, v))

    weight, mst = min_distanse(edges)
    if weight == -1:
        print(weight)
    else:
        print("Minimum Distance:", weight)
        print("MST edges:")
        for edge in mst:
            print(edge)


def min_distanse(edges):
    if not edges:
        return -1, []

    parent = {}
    rank = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
        return True

    nodes = set()
    for _, u, v in edges:
        nodes.add(u)
        nodes.add(v)
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    edges.sort()
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if union(u, v):
            mst.append((weight, u, v))
            total_weight += weight
            if len(mst) == len(nodes) - 1:
                break

    if len(mst) != len(nodes) - 1:
        return -1, []

    return total_weight, mst


read_edges_from_csv("lab_8/communication_wells.csv")
