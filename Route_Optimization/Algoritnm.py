import random

def generate_random_solution(map, trucks):
    """
    Generate a random solution for the given trucks and map.
    """
    cities = list(range(len(map)))
    solution = []

    for truck in trucks:
        sub_list = []
        pre_city = 0
        while len(sub_list) < truck[1]:
            random_city = random.choice([city for city in cities if map[pre_city][city] != 'N'])
            sub_list.append(random_city)
            cities.remove(random_city)
            pre_city = random_city
        solution.append(sub_list)
    return solution

def route_length(map, solution):
    total_length = 0

    for route in solution:
        route_length = 0
        for i in range(1, len(route)):
            route_length += map[route[i-1]][route[i]]
        total_length += route_length + map[0][route[0]]

    return total_length

def get_neighbours(solution, map):
    neighbours = []
    for route in solution:
        for i in range(len(route)):
            neighbour_route = route[:]
            neighbour_route[i] = random.choice([city for city in range(len(map)) if map[route[i-1]][city] != 'N'])
            neighbours.append(neighbour_route)
    return neighbours

def best(map, neighbours):
    bestNeighbour = min(neighbours, key=lambda x: r_len(map, x))
    bestRouteLength = r_len(map, bestNeighbour)
    return bestNeighbour, bestRouteLength

def hill(map):
    curr = rand(map)
    curr_len = r_len(map, curr)
    neighbours = neigh(curr, map)
    bestNeighbour, best_len = best(map, neighbours)

    while best_len < curr_len:
        curr = bestNeighbour
        curr_len = best_len
        neighbours = neigh(curr, map)
        bestNeighbour, best_len = best(map, neighbours)

    return curr, curr_len

def convert_to_int(line):
    """Convert a list of strings to a list of integers.

    Skip over 'N' values in the list.
    """
    int_list = []
    for value in line:
        if value == 'N':
            continue
        int_list.append(int(value))
    return int_list

def convert_list_to_string(lst):
    """Convert a list of integers to a string with each character separated by a comma."""
    char_list = []
    for num in lst:
        char_list.append(chr(num + 97))
    out_str = ','.join(char_list)
    return out_str

map = []
input_file = open('input.txt','r')
output_file = open('output.txt','w')

line_1 = input_file.readline()
line_1 = line_1[:-1]

line_1_list=to_int(line_1.split(','))
map.append(line_1_list)

for i in range(len(line_1_list)-1):
    line=input_file.readline()
    line = line[:-1]
    line_list=to_int(line.split(','))
    map.append(line_list)

trucks=[]
line=input_file.readline()
while True:
    if line[len(line)-1]=='\n':
       line = line[:-1]

    line_list=line.split('#')
    line_list[1]=int(line_list[1])
    trucks.append(line_list)
    line=input_file.readline()

    if line == '':
        break


sol, len = hill(map)

for i in (trucks):
    [a,b] = i[0].split("_")
    output_file.writelines(i[0]+'#'+letter(sol[int(b)-1])+'\n')

output_file.write(str(len))
input_file.close()
output_file.close()