# grafo.py

class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, nome):
        self.nos[nome] = {}
    
    def adicionar_aresta(self, origem, destino, custo):
        self.nos[origem][destino] = custo
        self.nos[destino][origem] = custo  # Para grafos não direcionados

def criar_grafo_exemplo():
    grafo = Grafo()

    # Adicionar nós
    grafo.adicionar_no('A')
    grafo.adicionar_no('B')
    grafo.adicionar_no('C')
    grafo.adicionar_no('D')
    grafo.adicionar_no('E')

    # Adicionar arestas com custos
    grafo.adicionar_aresta('A', 'B', 4)
    grafo.adicionar_aresta('A', 'C', 2)
    grafo.adicionar_aresta('B', 'C', 5)
    grafo.adicionar_aresta('B', 'D', 10)
    grafo.adicionar_aresta('C', 'D', 3)
    grafo.adicionar_aresta('D', 'E', 4)
    grafo.adicionar_aresta('C', 'E', 7)

    return grafo
