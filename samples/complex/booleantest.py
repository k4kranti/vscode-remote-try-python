a = 200
b = 165

if a>b:
    print('a is greater than b')
else:
    print('a is not greater than b')

# The bool() function allows you to evaluate any value, and give you True or False
print(bool(45))
print(bool("Hello"))
print(bool(4.6))
print(bool(True))
print(bool(["apples","oranges"]))
# Any number is true except 0 , {} , [], None
print(bool())
print(bool({}))
print(bool(0))
print(bool([]))
print(bool(None))


# function that returns 0 or False

class myclass():
   def __len__(self):
      return 0
   
myobj = myclass()
print("function returning 0 or False :" , bool(myobj))

# built-in functions that return a boolean value, like the isinstance() function

x = 200
print("isinstance(x, int): " , isinstance(x, int))
