# Lists of python
x = [3, 4, 5]
print(x)


# printing Individual Elements of a List(String side by side)
y = ["1", "2", "3", "4"]
print(end=""+y[1])
print(end=" "+y[2])


#printing Individual Elements of a List
a = [12, 13, 15]
print(a[2])



# Nested Lists- are just list within list
u = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(u[1][3])


#### Negative INDEXS
p = [1, 2, 3, 4]
print(p[-2])
print(p[-1])


#Sublist or Slicing
#q[start index:end index+1]

q = [1, 2, 3, 4, 5, 6,]
print(q[0:5])
print(q[2:4])


# Slicing using negative index
# q[start index:end index+1]

q =[1, 2, 3, 4, 5, 6]
print(q[0:-2])
print(q[1:-1])

#Another way

print(q[:4])
print(q[1:])

#whole list print
print(q[:])


# List Modify
a = [1, 2, 3, 4, 5]
b =['a', 'b', 'c']
ab = a+b
print(ab)


x = [1, 2, 3, 4]
newX = x*2
print(newX)


# List Element delesion
p = [1, 2, 3, 'a']
del p[3]
print(p)
