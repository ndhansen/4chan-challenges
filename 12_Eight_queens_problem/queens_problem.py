n = int(input("Enter the board size: "))
if n < 8:
    print("M8 it's called the 8 queens problem not the", n, "queens problem. Changing that to 8")
    n = 8
positions = []

if n % 6 != 2 and n % 6 != 3:
    for i in range(2, n + 1, 2):
        positions.append(i)
    for i in range(1, n + 1, 2):
        positions.append(i)
else:
    even = [x for x in range(2, n+1, 2)]
    odd = [x for x in range(1, n+1, 2)]
    pos1 = odd.index(1)
    pos3 = odd.index(3)
    if n % 6 == 2:
        pos5 = odd.index(5)
        odd[pos1], odd[pos3] = odd[pos3], odd[pos1]
        odd[len(odd)-1], odd[pos5] = odd[pos5], odd[len(odd)-1]
        positions = even + odd

    elif n % 6 == 3:
        pos2 = even.index(2)
        even[len(even)-1], even[pos2] = even[pos2], even[len(even)-1]
        odd[len(odd)-2], odd[pos1] = odd[pos1], odd[len(odd)-2]
        odd[len(odd)-1], odd[pos3] = odd[pos3], odd[len(odd)-1]
        positions = even + odd

for row in range(n):
    print(((4*n)+1) * "-")
    for square in range(n):
        print("|", end="")
        if positions[row] - 1 == square:
            print(" Q ", end="")
        else:
            print("   ", end="")
            
    print("|", end="")
    print()
print(((4*n)+1) * "-")
