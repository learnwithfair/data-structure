# Binary Search in python
def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [int(x) for x in input("Enter Array: ").split()]
data.sort()
print("Array is :", data)
element = int(input("Enter your searching element : "))
result = binarySearch(data, element, 0, len(data) - 1)
if result == -1:
    print("Element not found")
else:
    print("Element is present at position ", result + 1)
