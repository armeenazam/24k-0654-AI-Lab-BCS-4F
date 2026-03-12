# task 3

import random

POP_SIZE = 6
GENS = 15
MUT_RATE = 0.1

def fitness(x):
    return x**2 + 2*x

def random_chromosome():
    return format(random.randint(0,31), '05b')

def decode(ch):
    return int(ch,2)

def selection(pop):
    pop.sort(key=lambda x: fitness(decode(x)), reverse=True)
    return pop[:2]

def crossover(p1,p2):
    point = random.randint(1,4)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1,c2

def mutation(ch):
    ch = list(ch)
    for i in range(len(ch)):
        if random.random() < MUT_RATE:
            ch[i] = '1' if ch[i]=='0' else '0'
    return "".join(ch)

population = [random_chromosome() for _ in range(POP_SIZE)]

for gen in range(GENS):

    print("\nGeneration", gen)

    for ch in population:
        x = decode(ch)
        print(ch, "x =", x, "fitness =", fitness(x))

    parents = selection(population)

    new_pop = parents.copy()

    while len(new_pop) < POP_SIZE:
        c1,c2 = crossover(parents[0],parents[1])
        c1 = mutation(c1)
        c2 = mutation(c2)
        new_pop.extend([c1,c2])

    population = new_pop[:POP_SIZE]

best = max(population, key=lambda x: fitness(decode(x)))

print("\nBest Chromosome:", best)
print("Best x:", decode(best))
print("Best Fitness:", fitness(decode(best)))
