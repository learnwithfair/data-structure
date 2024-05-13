# Python program for implementation of Selection
import sys

data =[int(x) for x in input("Enter Array: ").split()]
print("Array is :",data)

# Traverse through all array elements
for i in range(len(data)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j

    # Swap the found minimum element with
    data[i], data[min_idx] = data[min_idx], data[i]

print("Sorted Array is :",data)