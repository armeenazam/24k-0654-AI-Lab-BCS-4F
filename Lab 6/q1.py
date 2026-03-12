#task 2
goal = 20
beam_width = 2

def heuristic(n):
    return abs(goal - n)

beam = [(1, [1])]
visited = set([1])

level = 0
found = False

while beam and not found:
    print("\nLevel", level)
    new_states = []

    for state, path in beam:
        print("Exploring:", state)

        children = [state + 2, state + 3, state * 2]

        for child in children:

            if child > goal or child in visited:
                continue

            visited.add(child)
            new_path = path + [child]

            if child == goal:
                print("\nGoal Reached!")
                print("Path:", new_path)
                found = True
                break

            new_states.append((child, new_path))

        if found:
            break

    if found:
        break

    new_states.sort(key=lambda x: heuristic(x[0]))
    beam = new_states[:beam_width]

    print("Selected states:")
    for state, _ in beam:
        print(state, "h =", heuristic(state))

    level += 1
