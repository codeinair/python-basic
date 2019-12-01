# element in a list
listA = [1,2,3]
1 in listA

# search for a element - Gives error if now in list
listA.index(2)

# concat a list
ListA = [1,2,3]
ListB = [4,5,6]
ListC = ListA + ListB
print(ListC)

# repeating operation - Repeats the list for n number of times
print(ListA * 3)

# Delete element in a list by position
l = [1,2,3,4]
l[1:2] = [] # as 1:2 refers to a sub list the elements in that range will be deleted
print(l)

del(l[2])
print(l)

# delete a vlaue in a list 
l.remove(1) # if not present then gives a error
print(l)

# sort a list - only same data type 
l=[2,7,5,4]
l.sort()
print(l)

# reverse the list
l=[2,7,5,4,"one","abc"]
l.reverse()
print(l)

# extend list 
l=[1,2,3]
l.extend([4,5,6])
print(l)

# slicing a list
listA= [1,2,3,4]
subList = listA[0:2]
subListSkip2 = listA[0:2:2] # start, stop and step 
subListSkipReverse2 = listA[2:0: -2] # start, stop and step - right to left 

# append a List
listA.append(subList)

# comparing list
ListA = [1,2,3,4]
ListB = [1,2,3,4]
print(ListA>ListB)
print(ListA<ListB)
print(ListA==ListB)