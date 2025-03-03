

txt = "The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#A placeholder can also include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type

price = 59.7838476
txt = f"The price is {price:.2f} dollars"
print(txt)

# operations inside formatter strings

price = 9
txt = f"The price is {price * 3} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#if...else statements inside the placeholders:

price = 49
txt = f"It is very {'Expensive' if price>50  else 'Cheap'}"

print(txt)

# comma as a thousand separator:
price = 1000000
txt = f'The price is {price:,} dollars'
print(txt)

#function that converts feet into meters:
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#multiple values 
quantity = 3
item = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, item, price))
#with index
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, item, price))

#same value more than once
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))