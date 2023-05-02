INF = float('inf')

def floyd_warshall(graph):
    dist = [[graph[i][j] if graph [i][j] != 0 else INF for j in range(len(graph))] for i in range(len(graph))]

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][i])

    return dist

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

distances = floyd_warshall(graph)

for i in range(len(distances)):
    for j in range(len(distances)):
        print(f"Shortest path from {i} to {j} is {distances[i][j]}")

