def imprimir_valores(distancias, predecessores, n):
    print("distancias: ", end='')
    for i in range(n):
        print(f"{distancias[i]:>5}", end=' ')
    print("\npredecessores: ", end='')
    for i in range(n):
        print(f"{predecessores[i]:>5}", end=' ')
    print("\n")


def bellman_ford(grafo, n, inicio):
    # Inicializa os vetores de distâncias (d) e predecessores (s)
    distancias = [float('inf')] * n
    predecessores = [-1] * n
    distancias[inicio] = 0

    print("Valores iniciais:")
    imprimir_valores(distancias, predecessores, n)

    # Encontra os caminhos mínimos de comprimento 1
    for z in range(n):
        if grafo[inicio][z] != 0:
            distancias[z] = grafo[inicio][z]
            predecessores[z] = inicio

    print("Após a inicialização:")
    imprimir_valores(distancias, predecessores, n)

    # Encontra os caminhos mínimos de comprimento 2, 3, etc.
    for i in range(1, n):
        temporarias = distancias.copy()
        for z in range(n):
            if z != inicio:
                for p in range(n):
                    if grafo[p][z] != 0 and distancias[p] + grafo[p][z] < temporarias[z]:
                        temporarias[z] = distancias[p] + grafo[p][z]
                        predecessores[z] = p
        distancias = temporarias.copy()
        print(f"Após a iteração {i}:")
        imprimir_valores(distancias, predecessores, n)

    return distancias, predecessores


if __name__ == "__main__":
    # Exemplo de grafo como matriz de adjacências
    grafo = [
        [0, 6, 0, 7, 0],
        [0, 0, 5, 8, -4],
        [0, -2, 0, 0, 0],
        [0, 0, -3, 0, 9],
        [2, 0, 7, 0, 0]
    ]

    n = len(grafo)
    vertice_inicio = 0

    distancias, predecessores = bellman_ford(grafo, n, vertice_inicio)

    print("Distâncias mínimas a partir do vértice", vertice_inicio)
    for i in range(n):
        print(f"{vertice_inicio} -> {i}: {distancias[i]}")

    print("Vértices predecessores no caminho mínimo")
    for i in range(n):
        print(f"Predecessor de {i}: {predecessores[i]}")
