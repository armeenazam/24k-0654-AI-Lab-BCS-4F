#Task 5

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}


def multi_goal_best_first(graph, start, goals):

    frontier = [(0, start, [start], set())]
    visited_states = set()

    while frontier:
        frontier.sort(key=lambda x: x[0])

        cost, current, path, visited_goals = frontier.pop(0)

        if current in goals:
            visited_goals = visited_goals | {current}

        if visited_goals == set(goals):
            print("All goals visited!")
            print("Path:", path)
            print("Total Cost:", cost)
            return

        state = (current, tuple(sorted(visited_goals)))
        if state in visited_states:
            continue

        visited_states.add(state)

        for neighbor, weight in graph[current]:
            new_cost = cost + weight
            new_path = path + [neighbor]
            frontier.append((new_cost, neighbor, new_path, visited_goals))

    print("Could not reach all goals.")


# Run Example
start_node = 'S'
goal_nodes = ['J', 'K']

multi_goal_best_first(graph, start_node, goal_nodes)
