N = int(input())
cosmonauts = []
for i in range(N):
    cosmonaut = input().split()
    name = ' '.join(cosmonaut[:-1])
    days = int(cosmonaut[-1])
    cosmonauts.append((name, days))
cosmonauts.sort(key=lambda x: x[1], reverse=True)
for cosmonaut in cosmonauts:
    print(cosmonaut[0], cosmonaut[1])