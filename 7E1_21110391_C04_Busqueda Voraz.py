"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 7E1
"""

import matplotlib.pyplot as plt
import networkx as nx
import heapq

# Definir el grafo que representa la red de almacenes (las distancias no importan para la búsqueda voraz)
warehouse_network = {
    'Almacén A': ['Almacén B', 'Almacén C'],
    'Almacén B': ['Almacén A', 'Almacén D', 'Almacén E'],
    'Almacén C': ['Almacén A', 'Almacén F'],
    'Almacén D': ['Almacén B', 'Almacén G'],
    'Almacén E': ['Almacén B', 'Almacén H'],
    'Almacén F': ['Almacén C', 'Almacén I'],
    'Almacén G': ['Almacén D', 'Almacén H'],
    'Almacén H': ['Almacén E', 'Almacén G', 'Almacén J'],
    'Almacén I': ['Almacén F', 'Almacén J'],
    'Almacén J': ['Almacén H', 'Almacén I']
}

# Función heurística (distancia aproximada en línea recta al destino)
heuristic = {
    'Almacén A': 10,
    'Almacén B': 8,
    'Almacén C': 9,
    'Almacén D': 7,
    'Almacén E': 6,
    'Almacén F': 5,
    'Almacén G': 4,
    'Almacén H': 3,
    'Almacén I': 2,
    'Almacén J': 0,  # El objetivo tiene heurística cero
}

# Algoritmo de Búsqueda Voraz
def greedy_best_first_search(graph, start, goal):
    # Usamos una cola de prioridad para almacenar nodos según la heurística
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], [start]))
    visited = set()

    while priority_queue:
        # Obtener el nodo con la menor heurística
        _, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        # Si hemos llegado al objetivo
        if node == goal:
            return path

        # Agregar vecinos a la cola con prioridad basada en la heurística
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (heuristic[neighbor], new_path))

    return None

# Visualización del grafo de la red de almacenes
def draw_graph(graph, path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2500, font_size=12, font_color='black', font_weight='bold', edge_color='gray')

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

    plt.show()

# Ejemplo de uso
start_warehouse = 'Almacén A'
goal_warehouse = 'Almacén J'
path = greedy_best_first_search(warehouse_network, start_warehouse, goal_warehouse)

print(f"Camino encontrado desde {start_warehouse} hasta {goal_warehouse}: {path}")

# Visualización del recorrido
draw_graph(warehouse_network, path)
