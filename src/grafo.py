# grafo.py

class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, nome):
        self.nos[nome] = {}
    
    def adicionar_aresta(self, origem, destino, custo):
        self.nos[origem][destino] = custo
        self.nos[destino][origem] = custo  # Para grafos não direcionados

def criar_grafo_romenia():
    grafo = Grafo()

    # Adicionando nós conforme o mapa da Romênia
    cidades = [
        'Arad', 'Zerind', 'Oradea', 'Sibiu', 'Fagaras', 'Rimnicu Vilcea',
        'Pitesti', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova',
        'Bucareste', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui',
        'Iasi', 'Neamt'
    ]
    
    for cidade in cidades:
        grafo.adicionar_no(cidade)
    
    # Adicionando arestas com base nas distâncias fornecidas
    grafo.adicionar_aresta('Arad', 'Zerind', 75)
    grafo.adicionar_aresta('Arad', 'Timisoara', 118)
    grafo.adicionar_aresta('Arad', 'Sibiu', 140)
    grafo.adicionar_aresta('Zerind', 'Oradea', 71)
    grafo.adicionar_aresta('Oradea', 'Sibiu', 151)
    grafo.adicionar_aresta('Timisoara', 'Lugoj', 111)
    grafo.adicionar_aresta('Lugoj', 'Mehadia', 70)
    grafo.adicionar_aresta('Mehadia', 'Drobeta', 75)
    grafo.adicionar_aresta('Drobeta', 'Craiova', 120)
    grafo.adicionar_aresta('Sibiu', 'Fagaras', 99)
    grafo.adicionar_aresta('Sibiu', 'Rimnicu Vilcea', 80)
    grafo.adicionar_aresta('Fagaras', 'Bucareste', 211)
    grafo.adicionar_aresta('Rimnicu Vilcea', 'Pitesti', 97)
    grafo.adicionar_aresta('Rimnicu Vilcea', 'Craiova', 146)
    grafo.adicionar_aresta('Pitesti', 'Craiova', 138)
    grafo.adicionar_aresta('Pitesti', 'Bucareste', 101)
    grafo.adicionar_aresta('Bucareste', 'Giurgiu', 90)
    grafo.adicionar_aresta('Bucareste', 'Urziceni', 85)
    grafo.adicionar_aresta('Urziceni', 'Hirsova', 98)
    grafo.adicionar_aresta('Hirsova', 'Eforie', 86)
    grafo.adicionar_aresta('Urziceni', 'Vaslui', 142)
    grafo.adicionar_aresta('Vaslui', 'Iasi', 92)
    grafo.adicionar_aresta('Iasi', 'Neamt', 87)

    return grafo
