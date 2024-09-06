import heapq
import math
from collections import deque
import time

def medir_tempo_execucao(funcao, *args):
    inicio = time.perf_counter() 
    resultado = funcao(*args)
    fim = time.perf_counter()
    tempo_decorrido = (fim - inicio) * 1000  
    return resultado, tempo_decorrido

hDLR = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Timisoara': 329, 'Sibiu': 253,
    'Fagaras': 176, 'Rimnicu Vilcea': 193, 'Pitesti': 100, 'Bucharest': 0,
    'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199,
    'Iasi': 226, 'Neamt': 234
}

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

def heuristica_hDLR(cidade_atual, destino, _=None):
    return hDLR.get(cidade_atual, float('inf'))

def heuristica_euclidiana(cidade_atual, destino, coordenadas):
    x1, y1 = coordenadas[cidade_atual]
    x2, y2 = coordenadas[destino]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def heuristica_manhattan(cidade_atual, destino, coordenadas):
    x1, y1 = coordenadas[cidade_atual]
    x2, y2 = coordenadas[destino]
    return abs(x2 - x1) + abs(y2 - y1)

def a_estrela(grafo, inicio, destino, heuristica, coordenadas=None):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))
    custos = {inicio: 0}
    caminhos = {inicio: None}
    nos_explorados = 0  # Contador de nós explorados
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)
        nos_explorados += 1  # Incrementa quando um nó é explorado

        if no_atual == destino:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = caminhos[no_atual]
            return caminho[::-1], custo_atual, nos_explorados  # Retorna também o número de nós

        for vizinho, distancia in grafo[no_atual].items():
            novo_custo = custos[no_atual] + distancia
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, destino, coordenadas)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminhos[vizinho] = no_atual
                
    return None, float('inf'), nos_explorados

def bfs(grafo, inicio, destino):
    fila = deque([[inicio]])
    visitados = set()
    nos_explorados = 0  # Contador de nós explorados

    while fila:
        caminho = fila.popleft()
        no_atual = caminho[-1]
        nos_explorados += 1  # Incrementa quando um nó é explorado

        if no_atual == destino:
            return caminho, nos_explorados  # Retorna o número de nós

        if no_atual not in visitados:
            visitados.add(no_atual)
            for vizinho in grafo[no_atual]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return None, nos_explorados

def dfs(grafo, inicio, destino, visitados=None, nos_explorados=0):
    if visitados is None:
        visitados = set()

    visitados.add(inicio)
    nos_explorados += 1  # Incrementa quando um nó é explorado

    if inicio == destino:
        return [inicio], nos_explorados  # Retorna o número de nós

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            caminho, nos_explorados = dfs(grafo, vizinho, destino, visitados, nos_explorados)
            if caminho:
                return [inicio] + caminho, nos_explorados

    return None, nos_explorados
