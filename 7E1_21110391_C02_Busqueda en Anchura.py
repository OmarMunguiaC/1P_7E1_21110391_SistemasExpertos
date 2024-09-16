import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Definir el grafo que representa las estaciones de tren
city_train_network = {
    'Estación A': ['Estación B', 'Estación D'],
    'Estación B': ['Estación A', 'Estación C', 'Estación E'],
    'Estación C': ['Estación B', 'Estación F'],
    'Estación D': ['Estación A', 'Estación E'],
    'Estación E': ['Estación B', 'Estación D', 'Estación F'],
    'Estación F': ['Estación C', 'Estación E']
}

# Algoritmo de Búsqueda en Anchura (BFS)
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return None

# Visualización del grafo de la red de trenes
def draw_graph(graph, path=None):
    G = nx.Graph()
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=12, font_color='black', font_weight='bold', edge_color='gray')
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

    plt.show()

# Ejemplo de uso
start_station = 'Estación A'
end_station = 'Estación E'
path = bfs(city_train_network, start_station, end_station)

print(f"Camino más corto desde {start_station} hasta {end_station}: {path}")

# Visualización del recorrido
draw_graph(city_train_network, path)
