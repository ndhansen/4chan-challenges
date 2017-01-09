import re
search = input("What word do you want to search? ")
file = open('text.txt')
content = file.readlines()
counter = 0
for line in content:
    for word in line.split(' '):
        word = re.sub('\W', '', word)
        if word.lower() == search.lower():
            counter += 1
file.close()

print(counter)
