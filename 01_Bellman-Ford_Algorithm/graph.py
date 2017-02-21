#graph = {'A': [['B', 10], ['C', 20]],
#         'B': [['E', 10], ['D', 50]],
#         'C': [['E', 33], ['D', 20]],
#         'D': [['E', -20], ['F', -2]],
#         'E': [['F', 1]],
#         'F': [[]]}

graph = {'A': [['B', 5]],
         'B': [['C', -2]],
         'C': [['D', -2]],
         'D': [['F', -2], ['E', 4]],
         'E': [[]],
         'F': [['B', 2]]}

#Doesn't check for endless negative routes.

starting_point = input("Which starting point should I use? ")
if graph.get(starting_point) == None:
    print("Not a valid starting point!")
    exit

cost = {}
for i in graph:
    if i == starting_point:
        cost[i] = 0
    else:
        cost[i] = None

for i in range(len(graph)-1):
    changed = False

    for key, values in graph.items():
        for value in values:
            if cost[key] == None:
                next
            elif value == []:
                next
            elif cost[value[0]] == None:
                cost[value[0]] = cost[key] + value[1]
                changed = True
            else:
                if (cost[key] + value[1]) < cost[value[0]]:
                    cost[value[0]] = cost[key] + value[1]
                changed = True
    
    if not changed:
        break

impossible = False
for key, values in graph.items():
    for value in values:
        if value != [] and cost[key] != None:
            if (cost[key] + value[1]) < cost[value[0]]:
                impossible = True

if impossible == False:
    for key, value in cost.items():
                    print("Point", key, "has the cost of", value)
else:
    print("This graph has an endless loop!")
