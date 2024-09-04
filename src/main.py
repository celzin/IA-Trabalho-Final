from grafo import criar_grafo_romenia
from algoritmos import a_estrela, bfs, dfs, heuristica_euclidiana, heuristica_manhattan
from visualizacao import visualizar_grafo

def main():
    # Criar o grafo da Romênia
    grafo = criar_grafo_romenia()

    # Coordenadas aproximadas das cidades (para uso nas heurísticas)
    coordenadas = {
        'Arad': (46.18, 21.32),
        'Zerind': (46.62, 21.51),
        'Oradea': (47.07, 21.92),
        'Timisoara': (45.76, 21.23),
        'Sibiu': (45.79, 24.15),
        'Fagaras': (45.84, 24.97),
        'Rimnicu Vilcea': (45.10, 24.37),
        'Pitesti': (44.85, 24.87),
        'Bucharest': (44.43, 26.10),
        'Giurgiu': (43.90, 25.97),
        'Urziceni': (44.71, 26.64),
        'Hirsova': (44.69, 27.95),
        'Eforie': (44.07, 28.63),
        'Vaslui': (46.63, 27.73),
        'Iasi': (47.16, 27.58),
        'Neamt': (46.98, 26.38)
    }

    # Executar A* com diferentes heurísticas
    print("A* com heurística Euclidiana:")
    caminho, distancia = a_estrela(grafo.nos, 'Arad', 'Bucharest', heuristica_euclidiana, coordenadas)
    print(f"Caminho: {caminho}, Distância: {distancia}")
    visualizar_grafo(grafo.nos, caminho)

    print("\nA* com heurística Manhattan:")
    caminho, distancia = a_estrela(grafo.nos, 'Arad', 'Bucharest', heuristica_manhattan, coordenadas)
    print(f"Caminho: {caminho}, Distância: {distancia}")
    visualizar_grafo(grafo.nos, caminho)

    # Executar BFS
    print("\nBusca em Largura (BFS):")
    caminho = bfs(grafo.nos, 'Arad', 'Bucharest')
    print(f"Caminho: {caminho}")
    visualizar_grafo(grafo.nos, caminho)

    # Executar DFS
    print("\nBusca em Profundidade (DFS):")
    caminho = dfs(grafo.nos, 'Arad', 'Bucharest')
    print(f"Caminho: {caminho}")
    visualizar_grafo(grafo.nos, caminho)

if __name__ == "__main__":
    main()
