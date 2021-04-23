# The LIst Methods

# The Index() Methods
PlacesVisited = ['India', 'Nepal', 'Malaysia', 'Bhutan', 'USA']
print(PlacesVisited.index('Nepal'))


# The Append method
PlacesVisited.append('Africa')
print(PlacesVisited)


# The Insert() method
PlacesVisited.insert(2, 'UK')
print(PlacesVisited)

#The Remove Method
PlacesVisited.remove('Bhutan')
print(PlacesVisited)

# The Sort() method
### Python itself sorting -Capital letter priority then alphabate
PlacesVisited.sort()
print(PlacesVisited)

### Python force sorting 
# use key=str.lower
PlacesVisited.sort(key=str.lower)
print(PlacesVisited)

## the reverse sorting
PlacesVisited.sort(key=str.lower, reverse=True)
print(PlacesVisited)

