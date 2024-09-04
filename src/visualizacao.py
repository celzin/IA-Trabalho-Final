import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo, caminho=None):
    G = nx.Graph()

    for cidade in grafo:
        for vizinho, distancia in grafo[cidade].items():
            G.add_edge(cidade, vizinho, weight=distancia)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if caminho:
        caminho_edges = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='r', width=2)

    plt.show()
