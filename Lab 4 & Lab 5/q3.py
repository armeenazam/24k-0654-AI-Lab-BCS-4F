# Task 3
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

def depth_limited_search(graph, current, goal, depth, path):

    path.append(current)

    if current == goal:
        return True

    if depth == 0:
        path.pop()
        return False

    for neighbor in graph[current]:
        if depth_limited_search(graph, neighbor, goal, depth - 1, path):
            return True

    path.pop()
    return False

def iterative_deepening_search(graph, start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("\nSearching with depth limit =", depth)

        path = []

        found = depth_limited_search(graph, start, goal, depth, path)

        if found:
            print("Goal Found!")
            print("Final Path:", path)
            return

        else:
            print("Goal not found at depth", depth)

    print("Goal not found within max depth.")


start_node = 'A'
goal_node = 'G'

iterative_deepening_search(graph, start_node, goal_node, 5)
