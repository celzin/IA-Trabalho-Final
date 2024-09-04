import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo, caminho=None):
    G = nx.Graph()

    # Adiciona todas as arestas ao grafo
    for cidade in grafo:
        for vizinho, distancia in grafo[cidade].items():
            G.add_edge(cidade, vizinho, weight=distancia)

    # Layout dos nós (posicionamento)
    pos = nx.spring_layout(G)
    
    # Paleta de cores distinta para os nós
    cmap = plt.get_cmap('tab20')  # Paleta com 20 cores bem distintas
    cores_nos = {
        cidade: cmap(i % 20)  # Atribui cores distintas usando uma paleta maior
        for i, cidade in enumerate(grafo)
    }

    # Desenhar nós com cores únicas
    nx.draw_networkx_nodes(
        G, pos, node_size=700, node_color=[cores_nos[cidade] for cidade in G.nodes()]
    )
    
    # Desenhar as arestas normais (não percorridas)
    nx.draw_networkx_edges(G, pos, width=2)

    # Adicionar rótulos aos nós (nomes das cidades)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

    # Adicionar rótulos de peso (distância) nas arestas normais
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Se houver um caminho a ser visualizado, destacamos as arestas percorridas
    if caminho:
        caminho_edges = list(zip(caminho, caminho[1:]))  # Cria pares de nós para formar as arestas do caminho

        # Desenhar as arestas percorridas em vermelho
        nx.draw_networkx_edges(
            G, pos, edgelist=caminho_edges, edge_color='r', width=4  # Destaque em vermelho
        )

        # Corrigir os rótulos de todas as arestas do caminho percorrido
        caminho_labels = {}
        for edge in caminho_edges:
            if edge in labels:
                caminho_labels[edge] = labels[edge]
            elif (edge[1], edge[0]) in labels:  # Verifica a direção inversa da aresta
                caminho_labels[edge] = labels[(edge[1], edge[0])]

        # Adicionar rótulos de peso (distância) nas arestas percorridas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=caminho_labels, font_color='red')  # Rótulos em vermelho

    plt.title("Visualização do Grafo e Caminho Percorrido")
    plt.show()
