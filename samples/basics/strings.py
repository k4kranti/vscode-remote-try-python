
''''
letter = input("Type a letter to use in christmas tree: ")
print()
print('  ' + letter)
print(' ' + letter + letter + letter)
print(letter + letter + letter+ letter + letter)
print('  |  ')
'''


#string contact

name = 'Pierre'
email = 'pierre@gmail.com'
age = 50
height = 72

print('His name is ' +name)
print(name + ' can be contacted at ' + email)
#print('He is ' + age + 'years old and is ' + height + 'inches tall')  #throws Type Error - only contact str (not int)


print('His name is ' +name)
print(name + 'can be contacted at ' + email)
print('He is ' + str(age) + ' years old and is ' + str(height) + ' inches tall.')


#string subtraction won't work
'''
revenue = input('Business Revenue: ')
cost = input('Business costs: ')
profit = revenue - cost  #TypeError: unsupported operand type(s) for -: 'str' and 'str'
print('The Business profit is: ' + str(profit))
'''


#string multiplication with int only - not with float 
x= 'Z' * 10
#x = 'A' * 2.5.   # not with float 
print(x)



revenue = int(input('Business Revenue: '))
cost = int(input('Business costs: '))
profit = revenue - cost 
print('The Business profit is: ' + str(profit)) # convert str to int
#lets build bar
cost_bar = '#' * cost
profit_bar = '#' * profit
print('  cost_bar: ' + cost_bar) 
print('profit_bar: ' + profit_bar) 

# when input is larger, you will have bigger bars 
revenue = int(input('Business Revenue: '))
cost = int(input('Business costs: '))
profit = revenue - cost 
print('The Business profit is: ' + str(profit)) 
#lets build bar say max hash is 25 bars
cost_bar = '#' * int((cost / revenue) * 25)  #string multiplication with int only - cast to int
profit_bar = '#' * int((profit / revenue) * 25)
print('  cost_bar: ' + cost_bar) 
print('profit_bar: ' + profit_bar) 