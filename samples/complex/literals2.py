# literals are value that is directly return in source code. say like fixed values in the programing. That means thsi value is not computed or derieved from other variables or expressions. 

#numerical literals
number = 42
pi= 1.42
complex = 1 + 7j

print("number:", number)
print("pi :", pi)
print("complex :", complex)

#String literals
msg1 = "Hello, World!"   #string literal with double 
msg2 ='Python' #string literal with single q
msg3 =''' Multi-line  
Single quote Record''' # multi-line
msg4 =""" Multi-line  
double quote Record """

print("msg1:", msg1)
print("msg2:", msg2)
print("msg3:", msg3)
print("msg4:", msg4)


#Boolean Literals - represents truth value - True or False
is_student= True
print("He is adreykell student in computer class?", is_student)


#None Literal - represents the absense of the value or null value 
result = None
print("Results published?", result)

#List, Tuple, Dictionary and Sets Literals

#list literal 
numbers = [1,2,3,4,5,6,7]

print("numbers:", numbers)

#Tuple literal
tuple = (1,2,3)

print("tuple:", tuple)

#Dictionary literal
person= {'name': 'Alice' , 'age':14} 

print("person:", person)

#Set literal
unique_set = {1,2,3,4,2}

print("unique_set:", unique_set)

#Set of String Literals
fruits = {"apple", "banana" ,"grapes" ,"banana"}
print("fruits :", fruits)

#unordered, unique, mutable (add,remove,math opera like union,intersection and difference)

fruits.remove("banana")
print("fruits_removal :", fruits)

fruits.add("oranges")
fruits.add("kiwi")

print("fruits_newset :", fruits)

set1 =  {1,2,3}
set2 = {3,4,5,6}
union_set = set1 | set2 # or set1.union(set2)
print("union_set :", union_set)

intersection_set = set1 & set2 #or set1.intersection(set2)
print("intersection_set :", intersection_set)


difference_set1 = set1 - set2
print("difference_set1 :", difference_set1)

difference_set2 = set2 - set1
print("difference_set2 :", difference_set2)

#mixed Data set
mixed_set = {1,"hello",3.14,True} #True is treated as 1 , so it is not added again.
print(mixed_set)

#empty set literal
empty_set =set() #use empty set constructor
print(empty_set)

empty_dictionary = {}
print(empty_dictionary)

#Complex literal with real and imaginary parts 
z1 = 3+4j
print("Complex literal" , z1)

#Complex literal with real and  negative imaginary parts 
n1 = 2-4j
print("Complex literal" , n1)

#Complex literal only imaginary  parts 
i1 = 4j
print("Complex imaginary literal" , i1)

#Accessing complex
print("Complex literal real part",z1.real) #3.0
print("Complex literal imaginary part",z1.imag) #4.0


x = b"Hello"
y =  bytes(5)

print("binary literal" , x)
print("bytes literal" , y)