import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

#O(n) solution
# names_cache = {}

# for n in names_1:
#     names_cache[n] = 1

# for n in names_2:
#     if n in names_cache:
#         duplicates.append(n)

#Limited memory solution, only store in arrays
#Sort first array, binary search each name in second array
#Slower than my first solution, but still pretty dang fast
#O( n log n )
names_1.sort()
for n in names_2:
    first = 0
    last = len(names_2) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last)//2
        if names_1[mid] == n:
            duplicates.append(n)
            found = True
        else:
            if n < names_1[mid]:
                last = mid - 1
            else:
                first = mid + 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

