# main.py

from grafo import criar_grafo_romenia
from algoritmos import a_estrela, bfs, dfs
from visualizacao import plotar_grafo

def main():
    grafo = criar_grafo_romenia()
    
    print("Executando A* de Arad para Bucareste...")
    caminho_a_estrela = a_estrela(grafo, 'Arad', 'Bucareste')
    print(f"Caminho A*: {caminho_a_estrela}")
    plotar_grafo(grafo, caminho_a_estrela)
    
    print("Executando BFS de Arad para Bucareste...")
    caminho_bfs = bfs(grafo, 'Arad', 'Bucareste')
    print(f"Caminho BFS: {caminho_bfs}")
    plotar_grafo(grafo, caminho_bfs)
    
    print("Executando DFS de Arad para Bucareste...")
    caminho_dfs = dfs(grafo, 'Arad', 'Bucareste')
    print(f"Caminho DFS: {caminho_dfs}")
    plotar_grafo(grafo, caminho_dfs)

if __name__ == "__main__":
    main()