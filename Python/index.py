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
#Strig Method
"""
text = "Hello, World"

upper_case = text.upper()
print(upper_case)

lower_case = text.lower()
print(lower_case)

capitalize_first = text.capitalize()
print(capitalize_first)

extra_text = "my name is huxn"
title_phrase = extra_text.title()
print(title_phrase)

space_in_text = "           Python is fun!      "
striped_text = space_in_text.strip()
left_striped_text = space_in_text.lstrip()
right_striped_text = space_in_text.rstrip()
print(striped_text)
print(left_striped_text)
print(right_striped_text)
"""

#str.startwith(prefix) and str.endwith(suffix)
"""
filename = "example.text"
start_with = filename.startswith("example");
start_with2 = filename.startswith("nexample")
print(start_with) #true
print(start_with2) #false

#str.replace(old, new)

sentence = "I like programming in Java"
replaced_sentence = sentence.replace("java", "python")
print(replaced_sentence)
"""
#str.find() and str.index()
"""
phrase = "Python is powerful and Python is easy to learn"
find_python = phrase.find("Python") 
find_python1 = phrase.find("python")
print(find_python) #o
print(find_python1) #-1
find_python2 = phrase.index("and")
print(find_python2) #19
"""

#str.split(separator)
"""
sentence = "This is an example text"
splited_text = sentence.split(" ")
print(splited_text) #['This', 'is', 'an', 'example', 'text']
"""

#str.count(substring)
"""
sentence = "Python is easy, we should learn python and use python"
count_python = sentence.count("python")
print(count_python) #2 because case sensetive
"""
#Comparison Operators
"""
a = 5
b = 10
d = 5

c = a == b
c1 = a == d
c2 = a != b
c3 = a != d
c4 = a < b
c5 = a > b
c6 = a >= b
c7 = a <= b
print(c)#false
print(c1)#true
print(c2)#true
print(c3)#false
print(c4)#true
print(c5)#false
print(c6)#false
print(c7)#true
"""