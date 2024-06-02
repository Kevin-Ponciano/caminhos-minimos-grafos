def ler_grafo():
    n = int(input("Entre com o número de vértices: "))
    grafo = {i: [] for i in range(n)}

    print("Entre com as arestas no formato 'u v', uma por linha (digite 'fim' para terminar):")
    while True:
        linha = input().strip()
        if linha == 'fim':
            break
        partes = linha.split()
        if len(partes) != 2:
            print("Entrada inválida, por favor entre com as arestas no formato 'u v'.")
            continue
        try:
            u, v = map(int, partes)
            if u >= n or v >= n or u < 0 or v < 0:
                print("Vértices fora do intervalo permitido.")
                continue
            grafo[u].append(v)
            grafo[v].append(u)  # Se o grafo for direcionado, remova esta linha
        except ValueError:
            print("Entrada inválida, por favor entre com números inteiros.")

    return grafo


def dfs(grafo, vertice, visitados):
    visitados[vertice] = True
    print(vertice, end=' ')

    for vizinho in grafo[vertice]:
        if not visitados[vizinho]:
            dfs(grafo, vizinho, visitados)


def executar_dfs(grafo, vertice_inicial):
    visitados = [False] * len(grafo)
    print("DFS a partir do vértice", vertice_inicial)
    dfs(grafo, vertice_inicial, visitados)
    print()


def bfs(grafo, vertice_inicial):
    visitados = [False] * len(grafo)
    fila = [vertice_inicial]
    visitados[vertice_inicial] = True
    frente = 0

    print("BFS a partir do vértice", vertice_inicial)
    while frente < len(fila):
        vertice = fila[frente]
        frente += 1
        print(vertice, end=' ')

        for vizinho in grafo[vertice]:
            if not visitados[vizinho]:
                fila.append(vizinho)
                visitados[vizinho] = True
    print()


class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave


def inserir(raiz, chave):
    if raiz is None:
        return No(chave)
    else:
        if raiz.valor < chave:
            raiz.direita = inserir(raiz.direita, chave)
        else:
            raiz.esquerda = inserir(raiz.esquerda, chave)
    return raiz


def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.valor, end=' ')
        em_ordem(raiz.direita)


def pre_ordem(raiz):
    if raiz:
        print(raiz.valor, end=' ')
        pre_ordem(raiz.esquerda)
        pre_ordem(raiz.direita)


def pos_ordem(raiz):
    if raiz:
        pos_ordem(raiz.esquerda)
        pos_ordem(raiz.direita)
        print(raiz.valor, end=' ')


def construir_e_percorrer_bst():
    valores = list(map(int, input("Entre com uma lista de inteiros: ").split()))
    raiz = None
    for valor in valores:
        raiz = inserir(raiz, valor)

    print("Escolha o tipo de busca (em_ordem, pre_ordem, pos_ordem):")
    tipo_busca = input().strip().lower()

    if tipo_busca == "em_ordem":
        em_ordem(raiz)
    elif tipo_busca == "pre_ordem":
        pre_ordem(raiz)
    elif tipo_busca == "pos_ordem":
        pos_ordem(raiz)
    else:
        print("Tipo de busca inválido")
    print()


if __name__ == "__main__":
    while True:
        print("Escolha a operação:")
        print("1: Ler grafo e executar DFS")
        print("2: Ler grafo e executar BFS")
        print("3: Construir e percorrer BST")
        print("4: Sair")
        escolha = int(input())

        if escolha == 1:
            grafo = ler_grafo()
            vertice_inicial = int(input("Entre com o vértice inicial para DFS: "))
            executar_dfs(grafo, vertice_inicial)
        elif escolha == 2:
            grafo = ler_grafo()
            vertice_inicial = int(input("Entre com o vértice inicial para BFS: "))
            bfs(grafo, vertice_inicial)
        elif escolha == 3:
            construir_e_percorrer_bst()
        elif escolha == 4:
            break
        else:
            print("Escolha inválida. Tente novamente.")
