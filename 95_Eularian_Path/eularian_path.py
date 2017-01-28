import copy

circuit = {'A': ['B', 'C', 'E'],
         'B': ['D', 'D', 'C', 'A'],
         'C': ['A', 'B', 'D', 'F'],
         'D': ['B', 'B', 'C', 'F'],
         'E': ['A', 'F'],
         'F': ['C', 'D', 'E']}

def no_sides_remaining(circuit):
    for vertex, side in circuit.items():
        if side != []:
            return False
    return True

def check_connectivity(circuit, dots, pos):
    #if pos not in dots:
    dots.append(pos)
    connections = circuit[pos].copy()
    for dot in dots:
        if dot in connections[:]:
            connections.remove(dot)
    if connections == []:
        return
    else:
        for next_connection in connections:
            check_connectivity(circuit, dots, next_connection)
    return dots

def will_burn_bridge(circuit, pos, target):
    if len(circuit[target]) == 1 and len(circuit[pos]) == 1:
        circuit[position].remove(target)
        circuit[target].remove(position)
        if no_sides_remaining(circuit):
            return False
        else:
            return True
    circuit[position].remove(target)
    circuit[target].remove(position)
    search_start = target
    dots = []
    dots = check_connectivity(circuit, dots, search_start)
    unique_dots = []
    for dot in dots:
        if dot not in unique_dots:
            unique_dots.append(dot)
    dots_remaining = 0
    for i in circuit:
        if circuit[i] != []:
            dots_remaining += 1
    if len(unique_dots) != dots_remaining:
        return True
    return False

odds = 0
for vertex, side in circuit.items():
    if len(side) % 2 != 0:
        odds += 1

if odds != 2 and odds != 0:
    print("Wrong number of odd vertecies, found", odds, "expected 0 or 2")
    quit

if odds != 0:
    for vertex, side in circuit.items():
        if len(side) % 2 != 0:
            start = vertex
            break

else:
    start = list(circuit.keys())[0]

position = start
i = 0
while no_sides_remaining(circuit) == False:
    try:
        target = circuit[position][i]
    except IndexError:
        print("Something went wrong. Either there's no solution, or I made a mistake.")
        print("Please consult Nicholas")
        quit
    circuit_cpy = copy.deepcopy(circuit)
    if will_burn_bridge(circuit_cpy, position, target) == False:
        print(position, target)
        circuit[position].remove(target)
        circuit[target].remove(position)
        position = target
        i = 0
    else:
        i += 1

print("It should be solved now!")
