def dijkstra(grafo, inicio, fim):
    n = len(grafo)  # Número de vértices no grafo
    distancias = [float('inf')] * n  # Inicializa distâncias como infinito
    predecessores = [-1] * n  # Inicializa predecessores como -1
    visitados = [False] * n  # Marca todos os vértices como não visitados
    distancias[inicio] = 0  # A distância do vértice inicial para ele mesmo é 0

    for _ in range(n):
        u = -1
        # Encontra o vértice não visitado com a menor distância
        for i in range(n):
            if not visitados[i] and (u == -1 or distancias[i] < distancias[u]):
                u = i

        # Se a menor distância é infinito, os vértices restantes são inacessíveis a partir do início
        if distancias[u] == float('inf'):
            break

        visitados[u] = True

        # Atualiza as distâncias dos vizinhos do vértice u
        for v, peso in grafo[u]:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u

    # Se a distância para o vértice final ainda é infinito, não há caminho
    if distancias[fim] == float('inf'):
        print("Não existe caminho entre os vértices", inicio, "e", fim)
        return

    # Reconstrói o caminho mínimo
    caminho = []
    while fim != -1:
        caminho.insert(0, fim)
        fim = predecessores[fim]

    print("Distância mínima:", distancias[caminho[-1]])
    print("Caminho mínimo:", " -> ".join(map(str, caminho)))


if __name__ == "__main__":
    # Exemplo de grafo como lista de adjacências
    grafo = {
        0: [(1, 1), (2, 4)],
        1: [(2, 2), (3, 5)],
        2: [(3, 1)],
        3: []
    }

    vertice_inicio = 0
    vertice_fim = 3

    dijkstra(grafo, vertice_inicio, vertice_fim)
