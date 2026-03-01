# TASK 4

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}


def uniform_cost_search(graph, start, goal):

    frontier = [(0, start, [start])]

    visited_cost = {}

    while frontier:

        frontier.sort(key=lambda x: x[0])

        cost, current, path = frontier.pop(0)

        if current in visited_cost and visited_cost[current] <= cost:
            continue

        visited_cost[current] = cost

        if current == goal:
            print("Least Cost Path:", path)
            print("Total Cost:", cost)
            return

        for neighbor in graph[current]:
            edge_cost = graph[current][neighbor]
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            frontier.append((new_cost, neighbor, new_path))

    print("Goal not reachable.")


start_node = 'S'
goal_node = 'G'

uniform_cost_search(graph, start_node, goal_node)
