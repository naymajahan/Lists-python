### 1st problem- Linear search with in a list, search for a number within the list. If it is found, then print "YES", else print "NO".

#### Solution

def linearSearch(someList,value):
    for i in range(len(someList)):
        if someList[i] == value:
            return "FOUND"

    if i == len(someList)-1:
        return "NOT FOUND"

a = [1, 2, 3, 4, 5, 6]

print(linearSearch(a, 3))
print(linearSearch(a, 33))



###2nd PROBLEM
### Binarry Search

def binarySearch(someList, value):

    if value > someList[-1]:
        return 'NOT FOUND'

    first = 0
    last = len(someList)-1

    while first <= last:
        mid = (first+last)//2

        if someList[mid] == value:
            return 'FOUND'
        elif someList[mid]>value:
            first=mid+1
        elif someList[mid]<value:
            last=mid-1

    if first > last:
        return 'NOT FOUND'


a = [1, 2, 3, 4, 5]
print(binarySearch(a,3))
print(binarySearch(a,77))



###  Given a list of numbers, print only the odd ones, forming a new list

def printOdd(someList):
    newList= []

    for i in range(len(someList)):
        if someList[i] % 2 != 0:
            newList.append(someList[i])

    return newList

a= [1, 2, 3, 4, 5]
print(printOdd(a))



#### Given a list of numbers(might be sorted or unsorted), return the centereb avg of the numbers.
## it's the average formed by excluding the largest and the smallest values all together.

def centraedAvg(someList):
    sum = 0
    count = 0
    tenpList= someList.sort()
    for i in range(1,len(someList)-1):
        sum = sum+someList[i]
        count=count+1

    return sum/count

a =[1, 2, 3, 4, 5]
print(centraedAvg(a))


