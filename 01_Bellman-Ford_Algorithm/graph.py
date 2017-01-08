graph = {'A': [['B', 10], ['C', 20]],
         'B': [['E', 10], ['D', 50]],
         'C': [['E', 33], ['D', 20]],
         'D': [['E', -20], ['F', -2]],
         'E': [['F', 1]],
         'F': [[]]}

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

for key, value in cost.items():
    print("Point", key, "has the cost of", value)
