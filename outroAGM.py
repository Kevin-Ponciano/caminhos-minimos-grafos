def encontrar(raiz, i):
    while raiz[i] != i:
        i = raiz[i]
    return i


def unir(raiz, rank, x, y):
    raiz_x = encontrar(raiz, x)
    raiz_y = encontrar(raiz, y)
    if raiz_x != raiz_y:
        if rank[raiz_x] > rank[raiz_y]:
            raiz[raiz_y] = raiz_x
        elif rank[raiz_x] < rank[raiz_y]:
            raiz[raiz_x] = raiz_y
        else:
            raiz[raiz_y] = raiz_x
            rank[raiz_x] += 1


def algoritmo_kruskal(grafo):
    n = len(grafo)  # Número de vértices no grafo
    mst = []  # Lista de arestas da árvore geradora mínima (MST)
    arestas = []

    # Cria a lista de arestas a partir da matriz de adjacências
    for i in range(n):
        for j in range(i + 1, n):
            if grafo[i][j] != 0:
                arestas.append((grafo[i][j], i, j))

    # Ordena as arestas em ordem crescente de peso
    arestas.sort()

    raiz = list(range(n))
    rank = [0] * n

    for peso, u, v in arestas:
        if encontrar(raiz, u) != encontrar(raiz, v):
            unir(raiz, rank, u, v)
            mst.append((u, v, peso))
            if len(mst) == n - 1:  # Se MST contém todos os vértices do grafo
                break

    return mst


if __name__ == "__main__":
    # Exemplo de grafo como matriz de adjacências
    grafo = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    arestas_mst = algoritmo_kruskal(grafo)
    print("Arestas da MST:")
    for u, v, peso in arestas_mst:
        print(f"({u}, {v}) com peso {peso}")
