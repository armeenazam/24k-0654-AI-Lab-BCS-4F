# Task 2
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def depth_limited_search(graph, current, goal, depth, path, visited_nodes):

    visited_nodes.append(current)
    path.append(current)

    if current == goal:
        return True

    if depth == 0:
        path.pop()
        return False

    for neighbor in graph[current]:
        if depth_limited_search(graph, neighbor, goal, depth - 1, path, visited_nodes):
            return True

    path.pop()
    return False


def run_dls(graph, start, goal, depth_limit):

    visited_nodes = []
    path = []

    print("\nRunning DLS with depth limit =", depth_limit)

    found = depth_limited_search(graph, start, goal, depth_limit, path, visited_nodes)

    print("Visited Nodes:", visited_nodes)

    if found:
        print("Goal Found!")
        print("Path:", path)
    else:
        print("Goal NOT found within depth limit.")

start_node = 'A'
goal_node = 'H'

run_dls(graph, start_node, goal_node, 2)
run_dls(graph, start_node, goal_node, 3)
