import time

Students = ["Malik", "Abdel", "Josh", "Aziz", "Thomas", "Karl", "James", "Eric", "Jason", "David", "Ron", "Bob", "Charlie", "Alice", "Lily", "Mason", "Alex", 
            "Noah", "Olivia", "Emma", "Ella", "Tom", "Max"]
StudentsHash = []
HashTable = [[] for _ in range(20)]

def linear_search(name):
    count = 0
    found = True
    for i in range(len(Students)):
        count = count + 1
        if Students[i] == name:
            print(name, " found at position", i+1)
            found = True
            print(count, "Number of trials to find", name)
            break
        else:
            found = False
    if found == False:
        print(name, "not found")
        print(count, "Number of trials")

def hash_function(name):
    NameInt = 0
    for i in range(len(name)):
        NameInt = NameInt + ord(name[i])
    NameInt = NameInt % 19
    return NameInt

for names in Students:
    index = hash_function(names)
    HashTable[index].append(names)

def hash_search(name):
    count = 0
    Flag = False
    for i in range(len(HashTable[hash_function(name)])):
        count = count + 1
        if name == HashTable[hash_function(name)][i]:
            print("Name Found at position", hash_function(name)+1)
            print(count, "Number of trials to find", name)
            Flag = True
            break
    if Flag == False:
        print("Name not found")
        print(count, "Number of trials")
            

def bubble_sort():
    flag = True
    while flag:
        flag = False
        for i in range(len(Students)-1):
            if Students[i] > Students[i+1]:
                Students[i], Students[i+1] = Students[i+1], Students[i]
                flag = True

def insertion_sort():
    flag = True
    while flag:
        flag = False
        for i in range(len(Students)-1):
            for j in range(len(Students)-i):
                if Students[i] > Students[i+j]:
                    Students[i], Students[i+j] = Students[i+j], Students[i]
                    flag = True
                    break

def binary_search(name):
    count = 0
    lower_bound = 0
    upper_bound = len(Students)-1
    middle = (upper_bound-lower_bound)//2
    found = True
    while found:
        count = count + 1
        if lower_bound > upper_bound:
            print(name, "not found")
            print(count, "Number of trials")
            found = False
        elif Students[middle] == name:
            print(name, "found at position", middle + 1)
            print(count, "Number of trials to find", name)
            found = False
        elif Students[middle] < name:
            lower_bound = middle+1
            middle = lower_bound + (upper_bound-lower_bound)//2
        else:
            upper_bound = middle-1
            middle = upper_bound - (upper_bound-lower_bound)//2

name = input("input a name: ")

start = time.perf_counter()
linear_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)

start = time.perf_counter()
hash_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)

bubble_sort()
start = time.perf_counter()
binary_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)