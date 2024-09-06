import heapq
import math
from collections import deque

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
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)

        if no_atual == destino:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = caminhos[no_atual]
            return caminho[::-1], custo_atual

        for vizinho, distancia in grafo[no_atual].items():
            novo_custo = custos[no_atual] + distancia
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, destino, coordenadas)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminhos[vizinho] = no_atual
                
    return None, float('inf')

def bfs(grafo, inicio, destino):
    fila = deque([[inicio]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        no_atual = caminho[-1]

        if no_atual == destino:
            return caminho

        if no_atual not in visitados:
            visitados.add(no_atual)
            for vizinho in grafo[no_atual]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return None

def dfs(grafo, inicio, destino, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(inicio)

    if inicio == destino:
        return [inicio]

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            caminho = dfs(grafo, vizinho, destino, visitados)
            if caminho:
                return [inicio] + caminho

    return None
