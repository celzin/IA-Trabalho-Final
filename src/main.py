from grafo import criar_grafo_romenia
from algoritmos import *
from visualizacao import visualizar_grafo_dinamico

def main():
    grafo = criar_grafo_romenia()

    # print("\nA* com heurística Euclidiana:")
    # (caminho, distancia, nos_explorados, log), tempo_execucao = medir_tempo_execucao(a_estrela, grafo.nos, 'Arad', 'Bucharest', heuristica_euclidiana, coordenadas)
    # print(f"Caminho: {caminho}, Distância: {distancia}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    # print("Sequência de nós explorados:")
    # for entry in log:
    #     print(entry)
    # visualizar_grafo(grafo.nos, caminho)

    # print("\nA* com heurística Manhattan:")
    # (caminho, distancia, nos_explorados, log), tempo_execucao = medir_tempo_execucao(a_estrela, grafo.nos, 'Arad', 'Bucharest', heuristica_manhattan, coordenadas)
    # print(f"Caminho: {caminho}, Distância: {distancia}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    # print("Sequência de nós explorados:")
    # for entry in log:
    #     print(entry)
    # visualizar_grafo(grafo.nos, caminho)

    # print("\nA* com heurística hDLR:")
    # (caminho, distancia, nos_explorados, log), tempo_execucao = medir_tempo_execucao(a_estrela, grafo.nos, 'Arad', 'Bucharest', heuristica_hDLR)
    # print(f"Caminho: {caminho}, Distância: {distancia}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    # print("Sequência de nós explorados:")
    # for entry in log:
    #     print(entry)
    # visualizar_grafo(grafo.nos, caminho)

    print("\nA* com visualização dinâmica (heurística hDLR):")
    (caminho, distancia, nos_explorados, log), tempo_execucao = medir_tempo_execucao(a_estrela_dinamico, grafo.nos, 'Arad', 'Bucharest', heuristica_hDLR)
    print(f"Caminho: {caminho}, Distância: {distancia}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    for entry in log:
        print(entry)
    visualizar_grafo_dinamico(grafo, caminho=caminho)

    # print("\nBusca em Largura (BFS):")
    # (caminho, nos_explorados, log), tempo_execucao = medir_tempo_execucao(bfs, grafo.nos, 'Arad', 'Bucharest')
    # print(f"Caminho: {caminho}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    # print("Sequência de nós explorados:")
    # for entry in log:
    #     print(entry)
    # # visualizar_grafo(grafo.nos, caminho)

    # print("\nBusca em Profundidade (DFS):")
    # (caminho, nos_explorados, log), tempo_execucao = medir_tempo_execucao(dfs, grafo.nos, 'Arad', 'Bucharest')
    # print(f"Caminho: {caminho}, Nós explorados: {nos_explorados}, Tempo de execução: {tempo_execucao:.4f} ms")
    # print("Sequência de nós explorados:")
    # for entry in log:
    #     print(entry)
    # visualizar_grafo(grafo.nos, caminho)

if __name__ == "__main__":
    main()
