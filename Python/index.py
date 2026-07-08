# 01. Variables

"""
age = 40
age = 10
user_password = 20
print(user_password) > 20
# print(age) > 10
"""

# 02. Arithmetic Operation

# Addition
"""
sum_result = 5 + 3
print(sum_result)
"""
#Subtraction
"""
sub_result = 29-9
print(sub_result)
"""
# Multiplyin
# Divition
"""
div_result = 10/2
print(div_result)  #5.0
div_result2 = 10//2
print(div_result2)  #5
"""
#Exponentiation
"""
power_result = 2**3
print(power_result) #8

twototwntyseven = 2 ** 27 -1
print(twototwntyseven)
"""
#Modulo
"""
mod = 38%10
print(mod) #8
"""

# 03. Getting input 
"""
input_name = input("Input your name: ")
print("Your name is", input_name)
"""
# 04. Assignment Operators
"""
x = 10
x += 5
print(x) 

y = 20
y -= 12 # y = y - 12
print(y)

z = 4
z *= 10
print(z) #40

z1 = 9
z1 /= 2
print(z1) #z1 //= 4 this // will round it

z2 = 5
z2 **= 2
print(z2) #25
"""

# 05: Strings in python 
"""
name = "Sayedur Rahamn"
print(name)
""" 
# Multiline string 
"""
multiline_string = '''This is 

multiline string '''

print(multiline_string) 
"""
#String concatenation
"""
first_name = "Huxn"
last_name = " Webdeb"

full_name = first_name + last_name
print(full_name)
"""
#String length
"""
name = "Huxn_webdev"
name_len = len(name)
print(name_len) #11
print(len("Python")) #6
"""

#String indexing and slicing
"""
text = "Python"
first_char = text[2]
substring = text[1:4] #from 1 to 4 not include 4
print(first_char)
print(substring)
"""

#String Formatting
"""
name = "Huxn"
age = 23

formated_string = f"My name is {name} and i am {age} years old"
print(formated_string)
"""
#Escape Characters
"""
escaped_string = "This is a line. \n This is new line" #its add extra new line 
escaped_string2 = "This is a line. \t This is new line" #its add tab
print(escaped_string)
print(escaped_string2)
"""
#Booleans
"""
x = True
y = False
name = "Huxn"
my_num = 19
my_num2 = 20.24
print(x)
print(type(x))
print(type(name))
print(type(my_num))
print(type(my_num2))
"""
#Type casting

"""
#float to int
float_num = 3.1416
print(type(float_num))
print(float_num)

int_num = int(float_num)
print(int_num)
print(type(int_num))

#int to float
int_num = 10
float_num = float(int_num)
print(type(float_num))
print(float_num)

#int to string

int_num = 15.10
str_num = str(int_num)
print(str_num)
print(type(str_num))
"""