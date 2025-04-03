### Creating Variables 
x = 6
y = "Eylul"
print(x)
print(y)

x = 6        # x is of type int
x = "Irmak"  # x is now of type str
print(x)

### Casting 
x = str(5)    # x will be '5'
y = int(5)    # y will be 5
z = float(5)  # z will be 5.0

### Get The Type
x = 6
y = "Irmak"
print(type(x))
print(type(y))

### Single or Double Quotes?
x = "Eylul"
# is the same as
x = 'Eylul'

### Case-Sensitive
a = 4
A = "Irmak"
#A will not overwrite a

### Legal Variables Names
myvar = "Eylul"
my_var = "Eylul"
_my_var = "Eylul"
myVar = "Eylul"
MYVAR = "Eylul"
myvar2 = "Eylul"

### Illegal Variable Names 
#2myvar = "Eylul"
#my-var = "Eylul"
#my var = "Eylul"

### Multi Words Variable Names

## Camel Case (Each word, except the first, starts with a capital letter)
myVariableName = "Eylul"

## Pascal Case (Each word starts with a capital letter)
MyVariableName = "Eylul"

## Snake Case (Each word is separated by an underscore character)
my_variable_name = "Eylul"

### One Value to Multiple Variables 
x = y = z = "Red"
print(x)
print(y)
print(z)

### Unpack a Collection
fruits = ["watermelon", "kiwi", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

