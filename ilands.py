def build_graph(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)] 

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                graph[(i, j)] = []
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 1:
                        graph[(i, j)].append((ni, nj))
    return graph

def bfs(start, graph, visited):
    queue = [start]
    island = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                island.append(neighbor)
    return island

def find_islands(matrix):
    graph = build_graph(matrix)
    visited = set()
    islands = []

    for node in graph:
        if node not in visited:
            island = bfs(node, graph, visited)
            islands.append(island)
    return islands

filename = 'lab_5/matrix.txt'
with open(filename, 'r') as f:
    matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]

islands = find_islands(matrix)

output = 'lab_5/output.txt'
with open(output, 'w') as f:
    f.write(f"islands : {len(islands)}\n")
    for i, island in enumerate(islands, 1):
        f.write(f"island  {i}: {island}\n")
