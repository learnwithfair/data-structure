def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            if array[j] > array[j + 1]:
                # swapping elements
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# Get input from user
data = [int(x) for x in input("Enter Array: ").split()]

# Calling function
bubbleSort(data)

#  Print Output
print('Sorted Array in Ascending Order:')
print(data)
