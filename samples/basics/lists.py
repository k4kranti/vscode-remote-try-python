
#List items are ordered, changeable, and allow duplicate values.

mylist = ["apple", "banana", "cherry"]
print(mylist)
print("type:", type(mylist))
print("len:" , len(mylist))

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#list constructor
list1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(list1)


list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#start to 4 items
print(list1[:4])
#start at 2 to end
print(list1[2:])

fruit_check = input("Which fruit to buy? ")
if fruit_check in list1:
  print(f"Yes, {fruit_check} is in the fruits list")
else:
  print(f"No, {fruit_check} is not in fruits list")


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
  
print("        ");
# Change the second item:
list1 = ["apple", "banana", "cherry"]
print('Before the second item: ', list1)
list1[1] = "blackcurrant" #replace index 1  
print('Change the second item: ', list1)
print("        ");
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print('Before the second item: ', list1)
list1[1:3] = ["blackcurrant", "watermelon"] #replace index [1:3]
print('After the second item : ', list1)

list1 = ["apple", "banana", "cherry"]

list1[1:3] = ["watermelon"]

print(list1)

#To add an item to the end of the list, use the append() method:

list1.append("mango")
print(list1)
