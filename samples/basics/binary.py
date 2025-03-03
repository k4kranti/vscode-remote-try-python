"""
Binary numbers, represented using the base-2 numeral system, 
are a fundamental concept in digital systems and computer science. 
The base-2 numeral system uses only two digits to represent any number which is 0 and 1.

In contrast, the decimal numeral system, which we are most familiar with is a base-10 system
 that uses ten digits (0-9).

"""

# Decimal to Binary Conversion
decimal_number = 10; 
print("decimal to binary :" , bin(decimal_number)) # 1010 i.e 1 * (2*3) + 0 * (2 *2 ) + 1 * (2 *1) + 0 * (2*0)

# Binary To Decimal Conversion
binary_number = '1010'
#Base 2 corresponds to the binary numbers. 
#Other bases are also present like 10 for decimal and 16 for hexadecimal
print('binary to decimal', int(binary_number,2))


# Binary addition
binary_num1 = '1010'
binary_num2 = '1101'
result = bin(int(binary_num1, 2) + int(binary_num2, 2))
print(result)