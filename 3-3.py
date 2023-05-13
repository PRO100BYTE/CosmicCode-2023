from collections import defaultdict
import heapq

# Класс графа
class Graph:
    def init(self):
        self.edges = defaultdict(list)
        self.weights = {}

    # Метод добавления ребра
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

# Функция для поиска кратчайшего пути в графе
def dijkstra(graph, start, end):
    # Инициализация необходимых переменных
    distances = {node: float('inf') for node in graph.edges}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    # Алгоритм Дейкстры
    while queue:
        (current_distance, current_node) = heapq.heappop(queue)
        if current_node == end:
            return distances[end]
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor in graph.edges[current_node]:
            distance = current_distance + graph.weights[(current_node, neighbor)]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return -1

# Считывание входных данных
n, m = map(int, input().split())
start = input().strip()
end = input().strip()
fuel = int(input().strip())

graph = Graph()

# Добавление ребер в граф
for i in range(m):
    from_node, to_node, weight = input().split()
    weight = int(weight)
    graph.add_edge(from_node, to_node, weight)
    graph.add_edge(to_node, from_node, weight)

# Поиск кратчайшего пути и вычисление необходимого топлива
min_fuel = dijkstra(graph, start, end)
if min_fuel == -1 or min_fuel > fuel:
    print(-1)
else:
    print(min_fuel)