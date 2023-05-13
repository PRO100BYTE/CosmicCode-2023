def countConfigurations(m, coords):
    combinations = [
        [[1, 2]],
        [[1], [2]],
        [[2], [1]],
        [[1, 2, 3]],
        [[1, 3], [2, 3]],
        [[1, 2], [2, 3]],
        [[2, 3], [1, 2]],
        [[1, 2], [1, 3], [2, 3]],
        [[1, 3], [2, 3], [1, 2]],
        [[1, 2, 3, 4]]
    ]

    def canPlace(a, b):
        if a[0] == b[0] and a[2] == b[2] and a[1] < b[3] and b[1] < a[3]:
            return True # вертикальное расположение
        elif a[1] == b[1] and a[3] == b[3] and a[0] < b[2] and b[0] < a[2]:
            return True # горизонтальное расположение
        else:
            return False # в остальных случаях петали не накладываются друг на друга

    def dfs(a, used, graph):
        used[a] = True
        for b in graph[a]:
            if not used[b]:
                dfs(b, used, graph)

    def isConnected(graph):
        used = [False] * m
        dfs(0, used, graph)
        for i in range(m):
            if not used[i]:
                return False
        return True

    def generateGraph(combo):
        graph = [[] for _ in range(m)]
        for a, b in combo:
            if canPlace(coords[a-1], coords[b-1]):
                graph[a-1].append(b-1)
                graph[b-1].append(a-1)
        return graph

    cnt = 0
    for i in range(len(combinations[m])):
        combo = combinations[m][i]
        graph = generateGraph(combo)
        if isConnected(graph):
            cnt += 1
    return cnt


n = int(input())
for i in range(n):
    m = int(input())
    coords = [list(map(int, input().split())) for j in range(m)]
    res = countConfigurations(m, coords)
    print(res)