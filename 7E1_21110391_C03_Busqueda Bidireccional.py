import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Definir el grafo que representa la red de carreteras entre ciudades
city_road_network = {
    'Ciudad A': ['Ciudad B', 'Ciudad C'],
    'Ciudad B': ['Ciudad A', 'Ciudad D', 'Ciudad E'],
    'Ciudad C': ['Ciudad A', 'Ciudad F'],
    'Ciudad D': ['Ciudad B', 'Ciudad G'],
    'Ciudad E': ['Ciudad B', 'Ciudad H', 'Ciudad F'],
    'Ciudad F': ['Ciudad C', 'Ciudad I', 'Ciudad E'],
    'Ciudad G': ['Ciudad D', 'Ciudad H'],
    'Ciudad H': ['Ciudad E', 'Ciudad G', 'Ciudad J'],
    'Ciudad I': ['Ciudad F', 'Ciudad J'],
    'Ciudad J': ['Ciudad H', 'Ciudad I']
}

# Algoritmo de Búsqueda Bidireccional
def bidirectional_search(graph, start, goal):
    # Usamos dos colas: una desde el inicio y otra desde el final
    if start == goal:
        return [start]

    start_queue = deque([[start]])
    goal_queue = deque([[goal]])
    start_visited = {start: [start]}
    goal_visited = {goal: [goal]}

    while start_queue and goal_queue:
        # Expandir desde el inicio
        start_path = start_queue.popleft()
        last_node_start = start_path[-1]

        if last_node_start in goal_visited:
            return start_path + goal_visited[last_node_start][::-1][1:]

        for neighbor in graph[last_node_start]:
            if neighbor not in start_visited:
                new_path = list(start_path)
                new_path.append(neighbor)
                start_queue.append(new_path)
                start_visited[neighbor] = new_path

        # Expandir desde el final
        goal_path = goal_queue.popleft()
        last_node_goal = goal_path[-1]

        if last_node_goal in start_visited:
            return start_visited[last_node_goal] + goal_path[::-1][1:]

        for neighbor in graph[last_node_goal]:
            if neighbor not in goal_visited:
                new_path = list(goal_path)
                new_path.append(neighbor)
                goal_queue.append(new_path)
                goal_visited[neighbor] = new_path

    return None

# Visualización del grafo de la red de carreteras
def draw_graph(graph, path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2500, font_size=12, font_color='black', font_weight='bold', edge_color='gray')

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

    plt.show()

# Ejemplo de uso
start_city = 'Ciudad A'
goal_city = 'Ciudad J'
path = bidirectional_search(city_road_network, start_city, goal_city)

print(f"Camino encontrado desde {start_city} hasta {goal_city}: {path}")

# Visualización del recorrido
draw_graph(city_road_network, path)
