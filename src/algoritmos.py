# algoritmos.py

import heapq
from collections import deque

def heuristica(no_atual, no_destino):
    # Exemplo de heurística simplificada (número de letras de diferença)
    return abs(ord(no_destino) - ord(no_atual))

def a_estrela(grafo, inicio, fim):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))
    custos = {inicio: 0}
    caminhos = {inicio: None}
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if no_atual == fim:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = caminhos[no_atual]
            return caminho[::-1]
        
        for vizinho, custo in grafo.nos[no_atual].items():
            novo_custo = custos[no_atual] + custo
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, fim)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminhos[vizinho] = no_atual
    
    return None

def bfs(grafo, inicio, fim):
    fila = deque([inicio])
    caminhos = {inicio: None}
    
    while fila:
        no_atual = fila.popleft()
        
        if no_atual == fim:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = caminhos[no_atual]
            return caminho[::-1]
        
        for vizinho in grafo.nos[no_atual]:
            if vizinho not in caminhos:
                caminhos[vizinho] = no_atual
                fila.append(vizinho)
    
    return None

def dfs(grafo, inicio, fim, caminho=None, visitados=None):
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()
    
    caminho.append(inicio)
    visitados.add(inicio)
    
    if inicio == fim:
        return caminho
    
    for vizinho in grafo.nos[inicio]:
        if vizinho not in visitados:
            resultado = dfs(grafo, vizinho, fim, caminho, visitados)
            if resultado:
                return resultado
    
    caminho.pop()
    return None
