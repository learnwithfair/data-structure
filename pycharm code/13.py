
queue = [int(x) for x in input("Enter The Elements : ").split()]
print("Queue Elements is : ",queue)
# Removing elements from the queue
print("\nDequeue Elements From Queue are : ",queue.pop(0),end=" ")
print(queue.pop(0))

print("After removing Queue elements is : ",queue)
