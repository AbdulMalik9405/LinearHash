import time
import statistics

Students = ["Malik", "Abdel", "Josh", "Aziz", "Thomas", " Karl", "James", "Eric", "Jason", "David", "Ron", "Bob", "Charlie", "Alice", "Lily", "Mason", "Alex", 
            "Noah", "Olivia", "Emma", "Ella", "Tom", "Max"]

StudentsInt = []

StudentsIntHash = []

HashTable = [
    [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

times = []

name = input("Enter a name: ")
for j in range(100):
    start = time.perf_counter()

    found = True

    for i in range(len(Students)):
        if Students[i] == name:
            print(name, " found at position", i+1)
            found = True
            end = time.perf_counter()
            break
        else:
            found = False

    if found == False:
        print(name, "not found")
        end = time.perf_counter()

    time_difference = end - start
    times.append(time_difference)

print(times)
print(statistics.median(times))

for i in Students:
    NameInt = 0
    for j in range(len(i)):
        NameInt = NameInt + ord(i[j])
    StudentsInt.append(NameInt)

for i in range(len(StudentsInt)):
    StudentsIntHash.append(StudentsInt[i] % 19)

for i in range(len(Students)):
    HashTable[StudentsIntHash[i]].append(Students[i])

times = []
name = input("Enter a name: ")
for j in range(100):
    NameInt = 0
    start = time.perf_counter()
    for i in range(len(name)):
        NameInt = NameInt + ord(name[i])
    NameInt = NameInt % 19

    if name in HashTable[NameInt]:
        print("Name Found at position", NameInt+1)
        end = time.perf_counter()
    else:
        print("Name not found")
        end = time.perf_counter()

    time_difference = end - start
    times.append(time_difference)
print(times)
print(statistics.median(times))