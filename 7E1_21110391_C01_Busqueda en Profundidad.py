import matplotlib.pyplot as plt
import networkx as nx

# Definir el grafo que representa la ciudad
city_graph = {
    'Casa': ['Parque', 'Supermercado'],
    'Parque': ['Casa', 'Museo'],
    'Supermercado': ['Casa', 'Cafeteria'],
    'Museo': ['Parque', 'Restaurante'],
    'Cafeteria': ['Restaurante', 'Supermercado'],
    'Restaurante': ['Museo', 'Cafeteria']
}

# Algoritmo de Busqueda en Profundidad (DFS)
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    if start == goal:
        return visited

    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if path:
                return path

    return None

# Visualizacion del grafo de la ciudad
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
start_point = 'Casa'
end_point = 'Restaurante'
path = dfs(city_graph, start_point, end_point)

print(f"Camino desde {start_point} hasta {end_point}: {path}")

# Visualizacion del recorrido
draw_graph(city_graph, path)
