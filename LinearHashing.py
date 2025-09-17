import time

Students = ["Malik", "Abdel", "Josh", "Aziz", "Thomas", "Karl", "James", "Eric", "Jason", "David", "Ron", "Bob", "Charlie", "Alice", "Lily", "Mason", "Alex", 
            "Noah", "Olivia", "Emma", "Ella", "Tom", "Max"]
StudentsHash = []
HashTable = [[] for _ in range(20)]

def linear_search(name):
    found = True
    for i in range(len(Students)):
        if Students[i] == name:
            print(name, " found at position", i+1)
            found = True
            break
        else:
            found = False
    if found == False:
        print(name, "not found")

def hash_function(name):
    NameInt = 0
    for i in range(len(name)):
        NameInt = NameInt + ord(name[i])
    NameInt = NameInt % 19
    return NameInt

for name in Students:
    index = hash_function(name)
    HashTable[index].append(name)

def hash_search(name):
    if name in HashTable[hash_function(name)]:
        print("Name Found at position", hash_function(name)+1)
    else:
        print("Name not found")

name = input("input a name: ")
start = time.perf_counter()
linear_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)

times = []
start = time.perf_counter()
hash_search(name)
end = time.perf_counter()
time_difference = end - start
print(time_difference)

def bubble_sort():
    flag = True
    while flag:
        flag = False
        for i in range(len(Students)-1):
            if Students[i] > Students[i+1]:
                Students[i], Students[i+1] = Students[i+1], Students[i]
                flag = True

bubble_sort()
print(Students)

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

insertion_sort()
print(Students)