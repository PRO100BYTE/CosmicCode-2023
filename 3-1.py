import heapq

# функция для поиска кратчайшего пути
def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return cost
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))
    return -1

# считываем входные данные
n, m = map(int, input().split())
graph = {i: {} for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# ищем кратчайший путь от Земли до Луны
min_cost = dijkstra(graph, 1, n)

# выводим результат
print(min_cost)