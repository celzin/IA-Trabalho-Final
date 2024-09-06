from grafo import criar_grafo_romenia
from algoritmos import *
from visualizacao import visualizar_grafo

def main():
    grafo = criar_grafo_romenia()

    print("\nA* com heurística hDLR:")
    caminho, distancia = a_estrela(grafo.nos, 'Arad', 'Bucharest', heuristica_hDLR)
    print(f"Caminho: {caminho}, Distância: {distancia}")
    visualizar_grafo(grafo.nos, caminho)

    print("A* com heurística Euclidiana:")
    caminho, distancia = a_estrela(grafo.nos, 'Arad', 'Bucharest', heuristica_euclidiana, coordenadas)
    print(f"Caminho: {caminho}, Distância: {distancia}")
    visualizar_grafo(grafo.nos, caminho)

    # print("\nA* com heurística Manhattan:")
    # caminho, distancia = a_estrela(grafo.nos, 'Arad', 'Bucharest', heuristica_manhattan, coordenadas)
    # print(f"Caminho: {caminho}, Distância: {distancia}")
    # visualizar_grafo(grafo.nos, caminho)

    # print("\nBusca em Largura (BFS):")
    # caminho = bfs(grafo.nos, 'Arad', 'Bucharest')
    # print(f"Caminho: {caminho}")
    # visualizar_grafo(grafo.nos, caminho)

    # print("\nBusca em Profundidade (DFS):")
    # caminho = dfs(grafo.nos, 'Arad', 'Bucharest')
    # print(f"Caminho: {caminho}")
    # visualizar_grafo(grafo.nos, caminho)

if __name__ == "__main__":
    main()
