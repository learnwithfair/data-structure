# Linear Search in Python
def linearSearch(array, element):
    n = len(array)
    find = False
    pos = []
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == element):
            pos.append(i + 1)
            find = True
    if (find == True):
        return pos
    else:
        return -1


data = [int(x) for x in input("Enter Array: ").split()]
print("Array is :", data)
element = int(input("Enter your searching element : "))
result = linearSearch(data, element)
if (result == -1):
    print("Element not found")
else:
    print("Element found at position(s): ", result)
