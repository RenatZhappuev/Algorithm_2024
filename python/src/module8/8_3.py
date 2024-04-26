def dijkstra_algo(graph, start):
    dists = {node: float('infinity') for node in graph}
    dists[start] = 0
    queue = [start]
    visited = set()

    while queue:
        node = min(queue, key=lambda node: dists[node])
        queue.remove(node)
        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                dist = dists[node] + weight
                if dist < dists[neighbor]:
                    dists[neighbor] = dist
                    queue.append(neighbor)

    return dists


N, M, K, C = map(int, input().split())
capitals = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(M)]

graph = {i: {} for i in range(1, N + 1)} #
for Ui, Vi, Ti in roads:
    graph[Ui][Vi] = Ti
    graph[Vi][Ui] = Ti

dists = dijkstra_algo(graph, C)

results = [(capital, dists[capital]) for capital in capitals]
results.sort(key=lambda x: x[1])

for capital, time in results:
    print(capital, time)
