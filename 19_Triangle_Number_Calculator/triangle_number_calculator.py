size = int(input("Please enter the size of the triangle: "))

def triangle(size):
    if size == 1:
        return 1
    else:
        return size + triangle(size - 1)

print(triangle(size))
