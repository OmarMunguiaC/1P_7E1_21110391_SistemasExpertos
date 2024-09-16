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

# Definir el grafo que representa las intersecciones de la ciudad con las distancias de las calles
city_map = {
    'Hospital': {'A': 4, 'B': 2, 'F': 1},
    'A': {'Hospital': 4, 'C': 5, 'D': 10},
    'B': {'Hospital': 2, 'D': 7, 'E': 3},
    'C': {'A': 5, 'Accidente': 12},
    'D': {'A': 10, 'B': 7, 'F': 6},
    'E': {'B': 3, 'F': 2, 'Accidente': 5},
    'F': {'D': 6, 'E': 2, 'Accidente': 8, 'Hospital': 1},
    'Accidente': {'C': 12, 'E': 5, 'F': 8}
}

# Función heurística (distancia aproximada en línea recta desde cada intersección hasta el lugar del accidente)
heuristic = {
    'Hospital': 14,
    'A': 12,
    'B': 10,
    'C': 8,
    'D': 7,
    'E': 4,
    'F': 6,
    'Accidente': 0  # El objetivo tiene heurística cero
}

# Algoritmo A* (A-star)
def a_star_search(graph, start, goal):
    # Usamos una cola de prioridad para almacenar nodos según f(n) = g(n) + h(n)
    priority_queue = []
    heapq.heappush(priority_queue, (0 + heuristic[start], [start], 0))  # f(n), camino, g(n)
    visited = set()

    while priority_queue:
        # Obtener el nodo con el menor f(n)
        f_value, path, g_cost = heapq.heappop(priority_queue)
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        # Si hemos llegado al objetivo
        if node == goal:
            return path, g_cost

        # Agregar vecinos a la cola con prioridad basada en f(n)
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                new_g_cost = g_cost + cost  # g(n) actual + costo de la arista
                f_value = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (f_value, new_path, new_g_cost))

    return None, float('inf')

# Visualización del mapa de la ciudad
def draw_graph(graph, path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2500, font_size=12, font_color='black', font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

    plt.show()

# Ejemplo de uso
start_location = 'Hospital'
goal_location = 'Accidente'
path, cost = a_star_search(city_map, start_location, goal_location)

print(f"Camino encontrado desde {start_location} hasta {goal_location}: {path} con un coste de {cost}")

# Visualización del recorrido
draw_graph(city_map, path)
