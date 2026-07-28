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

#Logical operator (and, or , not)
""" 
print(True and True) #True
print(True & False) #False
print(True | False) #True
print(False or False) #False
rint(not True)#False
print(not False)#True
print(False)#True
""" 
#conditional statement
"""
x = 3
if x > 5:
    print("x is postive")
elif x < 0:
    print("X is negative")
else:
    print("There have no number allwed from 1 to 5")
"""
#Loops 
#For loops
"""
for i in range(10):
    print("My name is huxn")
"""
#Range(start, end)
#range(star, stop, step)
"""
for i in range(2, 22):
    print("The number start from ", i )

for i in range(3, 15, 3):
    print("This is another step exmaple", i)

words = "Python"

for char in words:
    print(char)
    print(char.split( )
"""
#While loops
"""
password = ""

while len(password) < 8:
    password = input("Enter a password al least 8 charecter: ")
    print("Password need to be at least 8 charecter")

print("Password set sucsesfully")
""" 

choice = None
"""
while choice != "q":
    print("Option 1")
    print("Option 2")
    print("Option 3")
    choice = input("Enter your choice. Or type q exit: ")
    print("We exit")
"""

#Lists
#Lists number
"""
numbers = [1,2,3,4,5,6]
numbers2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numbers)
print(len(numbers))
#Access list
second_item = numbers[2]
print(second_item) #3
sliced_numbers = numbers2[2:10:2]
print(sliced_numbers)
"""
#List String
"""
fruits = ["Mango", "Pineapple", "Orange", "Watermelon", "Guaba", "Banana"]
# print(len(fruits))
#Access list
second_fruit = fruits[1] 
# print(second_fruit)
sliced_fuite_item = fruits[2:4]
# print(sliced_fuite_item)
#Update list 
fruits[2] = "Lemon"
print(fruits) #['Mango', 'Pineapple', 'Lemon', 'Watermelon', 'Guaba', 'Banana']
"""
#Mixed lists
"""
allOfThat = ["Huxn", 1, True, 3.1416]
# print(allOfThat)
# print(len(allOfThat))
"""

#Rmoving/deleting items
"""
numbers3 = [1,2,4,6,7,87,8,42,34,63]
print(numbers3)
del numbers3[3]
print(numbers3)
numbers3.remove(4)
print(numbers3)
"""
#1D, 2D, 3D lists
"""
#1D
numbers1d = [1,2,3,4,5,6]
#2D
numbers2d= [
    [1,2,3,4,5],
    [1,2,3,4,5,6], 
]
numbers3d = [
    1,[2,3,4,5,[6,7,8,9]]
]
#3D 
print(numbers2d)
print(numbers3d)

#Access code
print(numbers2d[1][2])
print(numbers3d[1][4][2])
"""

#Built in method
"""
my_lists = [1,2,3,4]
my_lists.append(5)
print(my_lists)
my_lists2 = [1,2,3,4]
my_lists2.extend([5,6,7])
print(my_lists2)
my_lists3 = [1,2,3,4]
my_lists3.insert(2, 4)
print(my_lists3)
my_lists4 = [1,2,3,4,5]
my_lists4.remove(4) #delete before index 
print(my_lists4)
my_lists5 = [1,2,3]
my_lists5.pop(1)
print(my_lists5)
my_lists6 = [1,2,3,4,5]
my_lists6.pop()
print(my_lists6)
my_lists7 = [4,3,6,8,2,8,9,10]
my_lists7.sort()
print(my_lists7)
my_lists8 = [4,5,9]
copied_list = my_lists8.copy()
print(copied_list)

#loop in list
for number in my_lists7:
    print(number)
#while loop in list

my_list9 = [1,2,3,4,5]
i = 1

while i < len(my_list9):
    print(i)
    i += 1
"""

#In operator

#String
text = "This is example"
check = "x" in text
print(check) #true

#List
my_List = [1,2,4,5,6]
check1 = 3 in my_List
check2 = 4 in my_List
print(check1) #false
print(check2) #true

#substring
my_sentence = "Python is powerful"
check3 = "Python" in my_sentence
check4 = "python" in my_sentence
print(check3) #True 
print(check4) #False #Because it is case-sensetive

#Loop

for i in range(10):
    print(i)