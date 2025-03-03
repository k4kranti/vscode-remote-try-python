''''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

Tuples are written with round brackets.

'''

mytuple = ("apple", "banana", "cherry")

print(mytuple)

#A tuple is a collection which is ordered and unchangeable.allow duplicate values.

#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)


# One item tuple, remember the comma:
tuple1 = ("apple",)
print(type(tuple1))

#NOT a tuple, this is string
tuple2 = ("apple")
print(type(tuple2))

# The search will start at index 2 (included) and end at index 5 (not included).
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# changing tuple values . Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
x = ("apple", "banana", "cherry")
# Convert the tuple to a list
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
print("Asterisk*")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # remaining assigned to asterisk

# iterate tuple using for 
thistuple1 = ("apple", "banana", "cherry")
for x in thistuple1:
  print(x)

#index through using range and len using for i in range(len(tuple))
thistuple2 = ("apple", "banana", "cherry")
for i in range(len(thistuple2)):
  print(thistuple2[i])