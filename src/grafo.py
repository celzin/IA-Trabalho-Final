class Grafo:
    def __init__(self):
        self.nos = {}

    def adicionar_aresta(self, cidade1, cidade2, distancia):
        if cidade1 not in self.nos:
            self.nos[cidade1] = {}
        if cidade2 not in self.nos:
            self.nos[cidade2] = {}
        self.nos[cidade1][cidade2] = distancia
        self.nos[cidade2][cidade1] = distancia

def criar_grafo_romenia():
    grafo = Grafo()
    grafo.adicionar_aresta('Arad', 'Zerind', 75)
    grafo.adicionar_aresta('Arad', 'Timisoara', 118)
    grafo.adicionar_aresta('Arad', 'Sibiu', 140)
    grafo.adicionar_aresta('Zerind', 'Oradea', 71)
    grafo.adicionar_aresta('Oradea', 'Sibiu', 151)
    grafo.adicionar_aresta('Sibiu', 'Fagaras', 99)
    grafo.adicionar_aresta('Sibiu', 'Rimnicu Vilcea', 80)
    grafo.adicionar_aresta('Fagaras', 'Bucharest', 211)
    grafo.adicionar_aresta('Rimnicu Vilcea', 'Pitesti', 97)
    grafo.adicionar_aresta('Pitesti', 'Bucharest', 101)
    grafo.adicionar_aresta('Bucharest', 'Giurgiu', 90)
    grafo.adicionar_aresta('Bucharest', 'Urziceni', 85)
    grafo.adicionar_aresta('Urziceni', 'Hirsova', 98)
    grafo.adicionar_aresta('Hirsova', 'Eforie', 86)
    grafo.adicionar_aresta('Urziceni', 'Vaslui', 142)
    grafo.adicionar_aresta('Vaslui', 'Iasi', 92)
    grafo.adicionar_aresta('Iasi', 'Neamt', 87)
    
    return grafo
