w = int(input("Board width: "))
if w < 5:
    print("Let's make things less complicated and up that to 5, shall we?")
    w = 5

h = int(input("Board height: "))
if h < 5:
    print("Let's make things less complicated and up that to 5, shall we?")
    h = 5

x = int(input("starting column (0 is starting index): "))
y = int(input("starting row (0 is starting index): "))

#I'm intentionally leaving out smaller boards because that's not the objective
#of this program. It's about Warndorf's rule.

matrix = [[0 for x in range(w)] for y in range(h)]
matrix[x][y] = 1

def check_done(matrix):
    for s in matrix:
        for t in s:
            if t == 0:
                return False
            
def get_next_possible_fields(matrix, x, y, depth):
    field = []
    set_x = [-2,-1,1,2,-2,-1,1,2]
    set_y = [1,2,2,1,-1,-2,-2,-1]
    possibilities = 0
    for i in range(len(set_x)):
        if x + set_x[i] >= 0 and x + set_x[i] < len(matrix[0]):
            if y + set_y[i] >= 0 and y + set_y[i] < len(matrix):
                if matrix[x + set_x[i]][y + set_y[i]] == 0:
                    if depth > 0:
                        field.append(tuple([get_next_possible_fields(matrix, x + set_x[i], y + set_y[i], depth - 1), x + set_x[i], y + set_y[i]]))
                    else:
                        possibilities += 1
    if depth == 0:
        return possibilities
    else:
        return field

while check_done(matrix) == False:
    print("X:", x, "Y:", y)
    next_moves = get_next_possible_fields(matrix, x, y, 1)
    if next_moves == []:
        print("Something went wrong, no possible moves left!")
        quit
    next_moves.sort()
    x = next_moves[0][1]
    y = next_moves[0][2]
    matrix[x][y] = 1
