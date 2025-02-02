# Variables are containers for storing data values.
x = 5
y = "John"

print("x" ,x)
print("y" ,y)

# Variables can change its type.
z = 5       # z is of type int
z = "John"   # z is of type string

print("z" ,z)


#data type of a variable, this can be done with casting.
x = int(5)       #var int casting
y = float(4)    #var float casting
z = str(2)      #var string casting i.e '2'

print("int" ,x)
print("float" ,y)
print("str" ,z)


# data type of a variable with the type() function.

print("z type" ,type(z))
print("y type" ,type(y))

# variable names are case-sensitive.
a = 4
A = "John"

print("a" ,a)
print("A" ,A)

# variable name must start with a letter or the underscore character, can't start with number 
var_test = 4
_var_test = 4
_2var_test = 4
var2 = 4

'''
below throw error on variable names

2myvar = "John"
my-var = "John"
my var = "John"
'''

# Many Values to Multiple Variables
x, y, z = 4,3,5
print("assign multiple variables")
print("x",x)
print("y",y)
print("z",z)

# One Value to Multiple Variables
x = y = z = "apples"
print("assign one to multiple variables -> x = y = z = \"apples\"")
print("x",x)
print("y",y)
print("z",z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apples", "banana", "kiwi"]
x,y,z = fruits #unpacking
print("unpacking - extract and assign to variables")
print("x",x)
print("y",y)
print("z",z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# + operator to output multiple variables. note the space 'Python ' 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# best way to separate multiple variables print is by ,
x = 5
y = "John"
print(x, y)

#Global Variables - created outside of function and used it every ware
x = "awesome"

def func():
    print("python is", x)

func()

#Global Variables - created outside of function and override inside function
x = "awesome"

def func():
    x = "fantastic"
    print("python is", x) #local variable scope

func()
print("python is", x) #global variable scope

# global keyword
def func():
    global x
    x = "globally awesome"
func()
print("python is", x)  

# global keyword
x = "awesome"
def func():
    global x
    x = "globally fantastic" #global variable scope

func()
print("python is", x) 