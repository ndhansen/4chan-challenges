graph = {'A': {'B': 10, 'C': 20},
         'B': {'A': 10, 'E': 10, 'D': 50},
         'C': {'A': 20, 'E': 33, 'D': 20},
         'D': {'E': 10, 'F': 2, 'B': 50, 'C': 20},
         'E': {'F': 1, 'B': 10, 'C': 33},
         'F': {'E': 1}}

def get_next_values(start, graph, cost):
    for key, value in graph[start].items():
        if (cost[graph[start][key][0]] == None) or (cost[start] + value < cost[graph[start][key][0]]):
            cost[graph[start][key][0]] = cost[start] + value
        del graph[key][start]
        del graph[start][key]
    next_node = graph[start][i][0]
    
         
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

out = False
while out != True:
    

for key, value in cost.items():
    print("Point", key, "has the cost of", value)
