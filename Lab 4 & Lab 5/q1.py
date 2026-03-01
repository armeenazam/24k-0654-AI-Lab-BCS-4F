#Task 1

building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows = len(building)
cols = len(building[0])

graph = {}

for r in range(rows):
    for c in range(cols):
        if building[r][c] == 1:
            graph[(r, c)] = []

            # Possible moves: Up, Down, Left, Right
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if building[nr][nc] == 1:
                        graph[(r, c)].append((nr, nc))


def bfs(graph, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nEmergency Exit Found!")
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


start_node = (0, 0)
goal_node = (3, 3)

print("BFS Traversal:")
bfs(graph, start_node, goal_node)
