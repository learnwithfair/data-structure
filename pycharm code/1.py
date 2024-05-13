data =[int(x) for x in input("Enter Array: ").split()]
print("Array is :",data)
pos=int(input("Enter Position for insert element : "))
pos=pos-1
num=int(input("Enter insert Number : "))
data.insert(pos,num)
print("After inserted element in Array is :",data)
dltnum=int(input("Enter delete number : "))
data.remove(dltnum)
print("The Final Array is :",data)
