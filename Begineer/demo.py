from operator import truediv
import random

name= "Beau"
age = 39
# all accepted variables - name1 HEIGHT my_name _name
# not accepted variables
# 123 test! % keywords of python for eg: if="hi"
#Expression- any sort of code that returns a value for eg: 1+1
#Statement - an operation on the value

name =" Beau"# use semi colon for multiple lines
print(type(name)==str)# indentation is imp as it represents the dependency between lines
# datatypes: strings , type is used to ususally check the datatype as the above is str
print(isinstance(name, str))# another method to find the type of data
age = 2
print(isinstance(age, int))
age=float(2) # making a float
print(isinstance(age, float))
age= int("20")# converting string to an integer
print(isinstance(age, int))
number = "20"# this method is known as casting : method to extract value from an variable
age = int(number)
print(isinstance(age, int))
# operators
age = 20 # assignment op


# arithmethic operator
1+1#2
2-1 #1
2*2 #4
4/2 #2
4%3 #1
4**2 #16
4//2 #2 

print("Scamp"+"is a good dog")
age=8
age+=8 # age = age+8 similarly with other arithmetic op
print(age)
# comparison op
a=1
b=2
a==b# False
a!=b# True
a>b# False
a<=b# True
con1= True
con2= False
not con1 # False
con1 and con2 # False
con1 or con2 # True

# OR operator return the first true value or 1st value if both are true for eg:
print(0 or 1) # 1
print(False or "hey")# hey
print('hi'or 'hey')# hi
print([] or False)# False here [] is an empty value which is considered as false
print(False or [])# [] False is taken and [] is given

#AND Operator
print(0 and 1) # 0
print(False and "hey")# false
print('hi' and 'hey')# hey
print([] and False)#  [] only evaluates the second arg if 1st is true
print(False and [])# False is as first

# BITWISE OP
# & binary and
# |binary or
# ^ binary xor
# - binary not
# << shift left operation
# >> shift right operation
# is & in op
# ternery op - easier mathod than to evaluate def if else
def is_adult2(age):
    return True if age >= 18 else False # in a single line



# STRINGS
"BEAU"
('BEAU')
name= "Beau"
name+='is my name'
age= str(39)
print(age)
print(name)
#FUNCTIONS OF STRINGS
print("Beau".lower())
print("BeAu".upper())
print("beAu".title())
islower()
isaplha()
isalnum()
isdecimal()
lower()
islower()
upper()
isupper()
title()
startswith()
endswith()
replace()
split()
strip()
join()
find() 
