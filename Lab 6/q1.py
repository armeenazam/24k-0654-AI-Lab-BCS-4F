# task1

import random

def f(x):
    return -x**2 + 6*x

min_x = 0
max_x = 6

x = random.randint(min_x, max_x)

print("Initial x:", x)
print("f(x):", f(x))

while True:
    neighbors = []

    if x - 1 >= min_x:
        neighbors.append(x - 1)
    if x + 1 <= max_x:
        neighbors.append(x + 1)

    best_neighbor = x
    best_value = f(x)

    for n in neighbors:
        value = f(n)
        print("Checking neighbor:", n, "f(x) =", value)

        if value > best_value:
            best_neighbor = n
            best_value = value

    if best_neighbor == x:
        break

    x = best_neighbor
    print("Move to:", x, "f(x) =", f(x))
    print()

print("\nFinal Optimal x:", x)
print("Maximum value:", f(x))
