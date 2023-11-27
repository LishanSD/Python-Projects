import random

def rand(map):
    cities = list(range(len(map)))
    solution = []

    for i in trucks:
        pre_city = 0
        sub_list = []
        while len(sub_list) < i[1]:   
            randomCity = cities[random.randint(1, len(cities) - 1)]
            if (map[pre_city][randomCity] != 'N'):
                sub_list.append(randomCity)
                cities.remove(randomCity)
                pre_city = randomCity
        solution.append(sub_list)
    return solution

def r_len(map, solution):
    r_len = 0
    for i in solution:
        length = 0
        for j in range(len(i)):
            if (j == 0):
                first_len = map[0][j]
            else:
                length += map[i[j-1]][i[j]]
        r_len = first_len + length
    return r_len

def neigh(solution, map):
    neighbours = []
    for i in solution:
        for j in range(len(i)):
            neighbour = rand(map)
            neighbours.append(neighbour)
    return neighbours

def best(map, neighbours):
    bestRouteLength = r_len(map, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        curr_len = r_len(map, neighbour)
        if curr_len < bestRouteLength:
            bestRouteLength = curr_len
            bestNeighbour = neighbour
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

def to_int(line):
    for i in range(len(line)):
        if line[i] == 'N':
            continue
        line[i]=int(line[i])
    return line

def letter(lst):
    char_list=[]
    for i in lst:
        char_list.append(chr(i+97))
    out_str=','.join(char_list)
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
print(sol, len)
for i in (trucks):
    [a,b] = i[0].split("_")
    output_file.writelines(i[0]+'#'+letter(sol[int(b)-1])+'\n')

output_file.write(str(len))
input_file.close()
output_file.close()