#Task 6

import random
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6,  'E': 4,  'F': 11,
    'G': 0
}

def a_star_dynamic(start, goal):

    open_list = [(heuristic[start], start)]
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {}

    while open_list:
        open_list.sort(key=lambda x: x[0])
        f, current = open_list.pop(0)

        if current == goal:
            return reconstruct_path(parent, start, goal), g_cost[goal]

        for neighbor in graph[current]:

            tentative_g = g_cost[current] + graph[current][neighbor]

            if tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                parent[neighbor] = current
                open_list.append((f_cost, neighbor))

        dynamic_edge_update()

    return None, None

def reconstruct_path(parent, start, goal):
    path = [goal]
    while goal != start:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path


def dynamic_edge_update():
    node = random.choice(list(graph.keys()))
    if graph[node]:
        neighbor = random.choice(list(graph[node].keys()))
        new_cost = random.randint(1, 15)

        print(f"\nEdge cost updated: {node} → {neighbor} = {new_cost}")
        graph[node][neighbor] = new_cost



start_node = 'A'
goal_node = 'G'

path, cost = a_star_dynamic(start_node, goal_node)

print("\nFinal Optimal Path:", path)
print("Total Cost:", cost)
