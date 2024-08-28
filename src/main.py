# main.py

from grafo import criar_grafo_exemplo
from algoritmos import a_estrela, bfs, dfs
from visualizacao import plotar_grafo

def main():
    grafo = criar_grafo_exemplo()
    
    print("Executando A*...")
    caminho_a_estrela = a_estrela(grafo, 'A', 'E')
    print(f"Caminho A*: {caminho_a_estrela}")
    plotar_grafo(grafo, caminho_a_estrela)
    
    print("Executando BFS...")
    caminho_bfs = bfs(grafo, 'A', 'E')
    print(f"Caminho BFS: {caminho_bfs}")
    plotar_grafo(grafo, caminho_bfs)
    
    print("Executando DFS...")
    caminho_dfs = dfs(grafo, 'A', 'E')
    print(f"Caminho DFS: {caminho_dfs}")
    plotar_grafo(grafo, caminho_dfs)

if __name__ == "__main__":
    main()
