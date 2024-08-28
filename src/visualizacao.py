# visualizacao.py

import networkx as nx
import matplotlib.pyplot as plt

def plotar_grafo(grafo, caminho=None):
    G = nx.Graph()
    for no in grafo.nos:
        G.add_node(no)
    for no, vizinhos in grafo.nos.items():
        for vizinho, peso in vizinhos.items():
            G.add_edge(no, vizinho, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if caminho:
        caminho_edges = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='r', width=2)
    
    plt.show()
