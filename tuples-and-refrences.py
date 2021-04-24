## Tuple examples

tup = (1, 2, 3, 4, 'Hello', "9.98")
print(tup)
print(type(tup))
print(tup[4])
print(tup[:4])
print(tup[1:])



##### Tuple To List Conversion

newList = list(tup)
print(newList)
print(type(newList))


###### List to Tuple Conversion

t = tuple(newList)
print(t)
print(type(t))



#### Refrences Problem, ## main list not remain intact

### REfrences

def f(someList):
    someList.append("ok")

x = [1, 2, 3, 4]

f(x)

print(x)



#### for making the main list intact use copy function 

### REfrences
import copy as cp

def f(someList):
    someList.append("ok")

x = [1, 2, 3, 4]
s = cp.copy(x)

f(s)

print(x)

