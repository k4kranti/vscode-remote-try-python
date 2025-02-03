#addition +
x = 5
y = 2

print(x + y)

#subtraction -
x = 5
y = 2

print(x -y)


#multiplication *
x = 5
y = 2

print(x*y)


#division /
x = 5
y = 2

print("division" ,x/y)

#Modulus %
x = 15
y = 7

print("Modulus or reminder ", x % y)


# Exponentiation **
x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2


# floor division //
x = 15
y = 2

print(x // y) #rounds the result down to the nearest whole number



x = 3
print(x)
# or use := 
print("x :=", x := 3)	




"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
print(5 + 4 - 7 + 3)



"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""
print(100 + 5 * 3)

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")


#list's last item -1 and before last -2  index

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

basket = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(basket[2:5])
print(basket[:2]) # first two
print(basket[-2:]) # last two - Minus operator specifies slicing to be done from the rear end.

test = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(test[-4:-1])
print(test[-4:])    #last four
print(test[2:5])    # ['cherry', 'orange', 'kiwi']


#change basket "banana", "cherry"
basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
basket[1:3] = ["blackcurrant", "watermelon"]
print(basket)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)