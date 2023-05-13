import heapq  # импорт библиотеки для реализации кучи

def minimum_spanning_tree(graph):
    # Реализация алгоритма Прима для нахождения минимального остовного дерева графа
    n = len(graph)
    visited = [False] * n  # список посещенных вершин
    mst = []  # список ребер минимального остовного дерева
    start_vertex = 0  # начальная вершина
    visited[start_vertex] = True
    edges = [(cost, start_vertex, i) for i, cost in enumerate(graph[start_vertex])]  # список ребер, исходящих из начальной вершины

    heapq.heapify(edges)  # преобразование списка ребер в кучу

    while edges:
        cost, u, v = heapq.heappop(edges)  # извлечение ребра минимального веса
        if not visited[v]:
            visited[v] = True
            mst.append((u, v, cost))  # добавление ребра в минимальное остовное дерево
            for i, weight in enumerate(graph[v]):
                if not visited[i]:
                    heapq.heappush(edges, (weight, v, i))  # добавление ребер, исходящих из новой вершины в кучу
    return sum(weight for u, v, weight in mst)

# Чтение входных данных
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Вычисление и вывод результата
print(minimum_spanning_tree(graph))