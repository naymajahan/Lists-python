## Afew programs with lists
## List of movies that i loved

favMovie = []

while True:
    print('Movie no '+ str(len(favMovie)+1) + ' or press ENTER to stop adding to the list')
    movie = input()

    if movie == '':
        break

    favMovie =favMovie + [movie]

if len(favMovie) != 0:
    print('The List is ')
    for i in range(len(favMovie)):
        print(favMovie[i])



### properties
## The 'in' and "not in" keywords

myStudy = ['highlighter', 'gliter pen', 'pencil', 'marker', 'notepad']

print('Enter a study gadgets')
name = input()
if name not in myStudy:
    print("Nope, It's not in the List")
else:
    print(name+' is my study gadgets')




### Assuming multiple values at once

chocolateMilkShake = ['chocolate', 'milk', 'ice cream', 'blender']
x, y, z, q = chocolateMilkShake

print(x,y,z,q)   



#### strings are list too

a = 'Whats a list'
print(a[8])

