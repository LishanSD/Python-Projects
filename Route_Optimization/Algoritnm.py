import random

def rand(map, trucks):
    """Generate a random initial solution (list of routes per truck)."""
    cities = list(range(1, len(map)))  # exclude depot (0)
    solution = []

    for _, capacity in trucks:
        pre_city = 0
        sub_list = []
        while len(sub_list) < capacity and cities:
            randomCity = random.choice(cities)  # ✅ simpler
            if map[pre_city][randomCity] != 'N':
                sub_list.append(randomCity)
                cities.remove(randomCity)
                pre_city = randomCity
        solution.append(sub_list)
    return solution


def r_len(map, solution):
    """Calculate total route length of all trucks."""
    total_len = 0
    for route in solution:
        if not route:
            continue
        length = map[0][route[0]]  # ✅ depot → first city
        for j in range(1, len(route)):
            length += map[route[j-1]][route[j]]
        total_len += length + map[route[-1]][0]  # ✅ return to depot
    return total_len


def swap_neighbour(solution):
    """Generate a neighbour by swapping two cities in a random route."""
    neighbour = [route[:] for route in solution]  # deep copy
    route_idx = random.randint(0, len(neighbour)-1)
    route = neighbour[route_idx]
    if len(route) > 1:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return neighbour


def neigh(solution, k=10):
    """Generate k neighbours using swap move."""
    return [swap_neighbour(solution) for _ in range(k)]


def best(map, neighbours):
    """Return best neighbour and its length."""
    best_len = float('inf')
    best_neighbour = None
    for sol in neighbours:
        length = r_len(map, sol)
        if length < best_len:
            best_len = length
            best_neighbour = sol
    return best_neighbour, best_len


def hill(map, trucks, max_iter=1000):
    """Hill climbing with swap-based neighbours."""
    curr = rand(map, trucks)
    curr_len = r_len(map, curr)

    for _ in range(max_iter):
        neighbours = neigh(curr)
        bestNeighbour, best_len = best(map, neighbours)
        if best_len < curr_len:
            curr, curr_len = bestNeighbour, best_len
        else:
            break  # no better neighbour found
    return curr, curr_len


def to_int(line):
    return [int(x) if x != 'N' else 'N' for x in line]


def letter(lst):
    """Convert list of indices → letters (0→a, 1→b, etc.)."""
    return ','.join(chr(i+97) for i in lst)


# ---------------- Main ----------------
with open('input.txt','r') as input_file, open('output.txt','w') as output_file:
    line_1 = input_file.readline().strip()
    map = [to_int(line_1.split(','))]

    for _ in range(len(map[0]) - 1):
        line = input_file.readline().strip()
        map.append(to_int(line.split(',')))

    trucks = []
    for line in input_file:
        if not line.strip():
            continue
        name, cap = line.strip().split('#')
        trucks.append((name, int(cap)))

    sol, length = hill(map, trucks)

    for i, (truck_name, _) in enumerate(trucks):
        output_file.write(f"{truck_name}#{letter(sol[i])}\n")

    output_file.write(str(length))
