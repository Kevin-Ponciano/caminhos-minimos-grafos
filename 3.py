def prim(grafo):
    n = len(grafo)  # Número de vértices no grafo
    selecionados = [False] * n  # Marca todos os vértices como não selecionados
    selecionados[0] = True  # Seleciona o primeiro vértice
    arestas_mst = []  # Lista para armazenar as arestas da árvore geradora mínima (MST)

    for _ in range(n - 1):
        peso_minimo = float('inf')  # Inicializa o peso mínimo como infinito
        u, v = -1, -1  # Inicializa os vértices u e v

        # Encontra a aresta de menor peso conectando um vértice selecionado a um não selecionado
        for i in range(n):
            if selecionados[i]:
                for j in range(n):
                    if not selecionados[j] and grafo[i][j]:
                        if peso_minimo > grafo[i][j]:
                            peso_minimo = grafo[i][j]
                            u, v = i, j

        # Seleciona o vértice v e adiciona a aresta (u, v) à MST
        selecionados[v] = True
        arestas_mst.append((u, v))

    return arestas_mst


if __name__ == "__main__":
    # Exemplo de grafo como matriz de adjacências
    grafo = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    arestas_mst = prim(grafo)
    print("Arestas da MST:")
    for u, v in arestas_mst:
        print(f"({u}, {v})")
