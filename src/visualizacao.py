import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo, caminho=None):
    G = nx.Graph()
    for cidade in grafo:
        for vizinho, distancia in grafo[cidade].items():
            G.add_edge(cidade, vizinho, weight=distancia)
    pos = nx.spring_layout(G)
    cmap = plt.get_cmap('tab20') 
    cores_nos = {
        cidade: cmap(i % 20) 
        for i, cidade in enumerate(grafo)
    }
    nx.draw_networkx_nodes(
        G, pos, node_size=700, node_color=[cores_nos[cidade] for cidade in G.nodes()]
    )
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    if caminho:
        caminho_edges = list(zip(caminho, caminho[1:]))  
        nx.draw_networkx_edges(
            G, pos, edgelist=caminho_edges, edge_color='r', width=4 
        )
        caminho_labels = {}
        for edge in caminho_edges:
            if edge in labels:
                caminho_labels[edge] = labels[edge]
            elif (edge[1], edge[0]) in labels: 
                caminho_labels[edge] = labels[(edge[1], edge[0])]

        nx.draw_networkx_edge_labels(G, pos, edge_labels=caminho_labels, font_color='red') 
    plt.title("Visualização do Grafo e Caminho Percorrido")
    plt.show()
