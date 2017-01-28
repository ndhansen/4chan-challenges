num_rows = int(input("How deep should we go? "))

row = [1]

for i in range(num_rows):
    print(row)
    next_row = []
    for i in range(len(row) + 1):
        if i == 0:
            next_row.append(0 + row[i])
        elif i == (len(row)):
            next_row.append(0 + row[i-1])
        else:
            next_row.append(row[i - 1] + row[i])
    row = next_row
