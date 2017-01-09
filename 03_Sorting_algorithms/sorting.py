import random
import os
import time

def show_sorting(numbers, index_1, index_2, sleeptime = 0.1):
    tmp = os.system('cls')
    for i in range(len(numbers)):
        if i == index_1 or i == index_2:
            print('+' * numbers[i])
        else:
            print('-' * numbers[i])
    time.sleep(sleeptime)

def bubblesort(numbers):
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                show_sorting(numbers, i, i+1)
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                show_sorting(numbers, i, i+1)
                sorting = True
    return None

def insertsort(numbers):
    for i in range(1, len(numbers)):
        s = i
        while numbers[s] < numbers[s - 1] and (s - 1) >= 0:
            show_sorting(numbers, s, s - 1, 0.1)
            numbers[s], numbers[s - 1] = numbers[s - 1], numbers[s]
            show_sorting(numbers, s, s - 1, 0.1)
            s -= 1
    return None

def selectsort(numbers):
    for i in range(len(numbers)):
        key = i
        for x in range(i+1, len(numbers)):
            if numbers[x] < numbers[key]:
                key = x
                show_sorting(numbers, i, key, 0.25)
        numbers[i], numbers[key] = numbers[key], numbers[i]
        show_sorting(numbers, i, key, 0.25)

def mergesort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = numbers[:middle]
    right = numbers[middle:]
    
    left = mergesort(left)
    right = mergesort(right)
    print("Comparing", left, "with", right)
    time.sleep(0.25)
    return merge(left, right)

def merge(left, right):
    result = []
    while left != [] and right != []:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left != []:
        result.append(left.pop(0))
    while right != []:
        result.append(right.pop(0))
    return result

def quicksort(numbers,start, end):
    if start < end:
        part = partition(numbers, start, end)
        quicksort(numbers, start, part - 1)
        quicksort(numbers, part + 1, end)

def partition(numbers, start, end):
    i = start - 1
    pivot = numbers[end]

    for j in range(start, end):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[end] = numbers[end], numbers[i + 1]
    return (i + 1)

numbers = []
for i in range(12):
    numbers.append(random.randint(1, 10))

print("First, Bubblesort!")
time.sleep(1)
bubblesort(numbers[:])

tmp = os.system('cls')
print("Next, Intert sort!")
time.sleep(1)
insertsort(numbers[:])

tmp = os.system('cls')
print("Next, Select sort!")
time.sleep(1)
selectsort(numbers[:])

tmp = os.system('cls')
print("Next, Merge sort!")
time.sleep(1)
print("Before:", numbers)
tmp = mergesort(numbers[:])
print("After:", tmp)

tmp = os.system('cls')
print("Next, quick sort!")
time.sleep(1)
quicksort(numbers, 0, len(numbers) - 1)
print(numbers)
time.sleep(1)
input("Press enter to continue...")



