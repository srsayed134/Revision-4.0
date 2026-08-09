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
"""
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

"""
#List unpacking
"""
my_list = [1,2,3,4,5]
a, b, c, d, e = my_list
print(a)
print(b)
print(c)
print(d)
print(e)
my_list2 = [1,2,3,4,5,6]
a, b, *rest = my_list2
print(a)
print(b)
print(rest)
"""

#Tuple data structure :- it is immutable ordered, you cannot modify it after created but list is mutable and unordered
 
my_tuple = (1,2,3,"Huxn", 3.5)
"""
print(my_tuple)
print(my_tuple[3])
print(type(my_tuple))

# my_tuple[2] = 7 #error because immutable ÷
# print(my_tuple) #error

#you can create tuple with modified content 
new_tuple = my_tuple + (5, "Jhon")
print(new_tuple)

new_tuple2 = 2,3,4,5,6
print(type(new_tuple2)) #Class tuple 
not_tuple = 2
print(type(not_tuple))#not tuple 
not_tuple = (2)
print(type(not_tuple))#int
new_tuple3 = (2,)
print(type(new_tuple3))#tuple

friends_tuple = ("Alex", "Jordan", "Simran")

for friend in friends_tuple:
    print(friend)
"""

#Dictionary
"""
emthy_dict = {}
print(type(emthy_dict))#class dict

student_info = {"name": "Niom", "age": 20, "grade" : "A+"}
print(student_info)
print(type(student_info))
print(student_info["name"]) #Niom
print(student_info["age"]) #20
print(student_info["grade"]) #A+

person = dict(name= "Bob", age=25, city= "London")
print(person)
print(person["name"])

student_info2 = {"name": "Michel", "age" : 20, "is_student" : True, "Grade" : [56,76,23]}
print(student_info2["is_student"]) #True
print(student_info2["Grade"][2]) #23

person_info = {
    "person1" : {"name": "Bob", "Age" : 22, "Country": "France"},
    "person2" : {"name": "Alex", "Age" : 32, "Country": "Jordan"},
    "person3" : {"name": "Simon", "Age" : 45, "Country": "England"},
}

print(person_info["person1"]["name"]) #Bob
print(person_info["person2"]["Age"]) #32
"""

#Using list of tuples
"""
tuple_list = [("name", "Eva"), ("age", 22), ("City", "Berlin")]
from_tuple_to_dict = dict(tuple_list)
print(from_tuple_to_dict)
"""

#Accessing dictionary
"""
my_dict = {"name": "Jhon Doe", "age" :20, "Origin": "Spanish"}
print(my_dict["name"])#Jhon Doe

print(my_dict.get("age"))#20
print(my_dict.get("grade"))#None
"""
#Iterating dictionary
"""
my_dict = {"name": "Alex", "Age": 24, "Social": "Reddit"}

for key in my_dict:
    print(f"{key}: {my_dict[key]}")

for key,value in my_dict.items():
    print(f"{key}: {value}")
""" 

#Updating specific dictionary
"""
my_dict = {"Name": "Huxn", "Age": 23}
my_dict["Country"] = "USA"

print(my_dict)
my_dict["Age"] = 24
print(my_dict)
"""
#Uodate dictionary by method
"""
my_dict2 = {"FirstName": "Jhon", "Age": 20}
new_dict = {"LastName": "Dow", "Country": "Uk"}

my_dict2.update(new_dict)
print(my_dict2)
"""
#Update with keyword arguments
"""
my_dict3 = {"Name": "Lilian", "Age": 8}
my_dict3.update(country= "USA", State= "New York")
print(my_dict3)
"""
#Using setDefault() to add default value
"""
my_dict4 = {"Name": "Jhon", "Status": "Single"}
my_dict4.setdefault("City", "New York")
print(my_dict4)
"""
#Delete in dictionary
"""
my_dict = {"Name": "PK", "Release": 2009, "Genre": "Comedy"}
# del my_dict[" Release"]
print(my_dict)

# my_dict.pop("Genre")
print(my_dict)

my_dict.popitem()#It removes the last item of dictionary
print(my_dict)
my_dict.clear()#It removes the the whool dictionary key and item
print(my_dict)
"""

#Sets are unorder that is why you can not access like list, tuples, dictionary and also unique do not suppert duplicate item and order value by self

"""
my_set = set({1,2,3,4,5})
print(my_set)
print(type(my_set))

my_new_set = {1,2,3,4,5}
print(type(my_new_set))

my_new_set1 = {1,2,3,4,4,5,6,5,6}
print(my_new_set1) #{1, 2, 3, 4, 5, 6}

my_new_set2 = {2,4,3,8,7}
print(my_new_set2)

my_new_set3 = {"Alex", "Jhon", "Simon", "Nikkel", "Jhon"}
print(my_new_set3) #Result going to be random and change over time each output

games = {"GTA 5", "The withcer", "Call of duty", "DOTA2"}
games.add("Clash of Clan")
print(games)

games.update(["Prince of persia", "Assasin credd"])
print(games)

games.update(["Mobile Legend"])
print(games)

movies = {"PK", "Titanic", "Troy"}
movies.remove("Troy")
print(movies)
movies.clear()
print(movies)
"""
"""
games = {"GTA 5", "The withcer", "Call of duty", "DOTA2"}
for game in games:
    print(game)
"""

#Function
"""
#only funtion
def greet():
    print("This is an example")

greet()
#function with argument

def greet1(name):
    print(f"Hello this is {name}")

greet1("Alex")

def greet2(x,y):
    result= x + y
    print(result)

greet2(3,4)

#Default parameter

def greet3(x,y = 7):
    result= x * y
    print(result)

greet3(8,9)#72
greet3(8)#56

def greet4(message, num_exclamation_marks = 3):
    print(message + "!" * num_exclamation_marks)

greet4("Hello")#Hello!!!

#Named peremeter
def Details(name, age, country):
    print("Name", name)
    print("Age", age)
    print("Country", country)

Details(name="HuXn", age=23, country="UK")

#Retun 

def Two_sum(x, y):
    result = x + y
    return result

result = Two_sum(50, 33)
print(result)
#Multiple return

def Square_Cube(x):
    square = x ** 2
    cube = x ** 3
    return square,cube

square, cube = Square_Cube(5)
print(square)
print(cube)

#Nested funtion

def Outer_funtion(x):
    def Inner_funtion(y):
        return x + y

    result = Inner_funtion(5)
    return result

Result = Outer_funtion(5)
print(Result)
"""

#Lamda function
"""
add = lambda x,y : x + y
result = add(6,6)
print(result)

def apply_def(a,b, operation):
    return operation(a,  b)

result2 = apply_def(5,6, lambda a,b: a+b)
print(result2)
""" 

############## End intermadiate part or bigenner ##############

#Modeule
#Import full file
"""
import example_module_1

print(example_module_1.my_fav_num)#76
print(example_module_1.add_num(3,4))#7
print(example_module_1.multi_num(4,6))#24
print(example_module_1.test())
"""
#Import full file and give a alias name
"""
import example_module_1 as test
print(test.add_num(3,5))
"""
#Import specific function
"""
from example_module_1 import test
test()

from example_module_1 import add_num
print(add_num(2,3))

#Import multiple one is create alias
from example_module_1 import (my_fav_num as fav_num, multi_num, division_num)
print(fav_num)
print(multi_num(5,6)) 
print(division_num(10,2))#5.0
print(int(division_num(10,2)))#5
"""

#Import all module #For access any funtion or variable there is no need to typw example_module_1.add_num() insteade add_num(2,3 )
"""
from example_module_1 import *
print(add_num(4,5))#9
test()#This is practice
print(multi_num(3,5))#15
print(int(division_num(20,5)))#4 
"""

#Import date and time
"""
from datetime import datetime

date = datetime(year=2023, month=3, day=23, hour=3, minute=20, second=34)
print(date)
date2shothand = datetime(2022,3,4,19,20,54)
print(date2shothand)

print(f"Year: {date.year}")
print(f"Year: {date2shothand.year}")
print(f"Month: {date.month }")
print(f"Hour :{date.hour}")

print(date.now())
print(date.now().time())
print(date.now().hour)
print(date.now().minute)
"""

#Class
"""
class Person:
    def talk(self):
        print("My name in huxn")

#This is a instance for Person and it it an object 
Huxn = Person()
Huxn.talk()
"""
#__init__ is a  Constructor which allow us to create variable in class
#This is an example of one person 
"""
class Person:
    def __init__(self):
        self.name = "Huxn"
        self.age = 20
        self.location = "USA"

    def talk(self):
        #If we don't use self if there is name in global the variable will be use in this class module. SO we should use self keyword for safety
        print(f"The name is {self.name} and his age is {self.age}. He is from {self.location}")

Person1 = Person()
#Access method
Person1.talk()

#Access variable
Person1_name = Person1.name
print(Person1_name)#Huxn
"""

#This is an example of multiple person 
"""
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def details(self):
        print(f"I am {self.name}. I am {self.age} years old. My birth place is {self.location}")

Jordan = Person("Jordan", 20, "USA")
Jhon = Person("Jhon", 23, "Uk")
Rakesh = Person("Rakesh", 19, "India")
Hammam = Person("Hammam", 24, "UAE")
Dimitri = Person("Dimitri", 22, "Russia")
Nimiko = Person("Nimiko", 18, "Japan")

#Access all of them details
Nimiko.details()
Jhon.details()
Rakesh.details()

#Access all birthplace
Nimiko_location = Nimiko.location
Jordan_location = Jordan.location
print(Nimiko_location)#Japan
print(Jordan_location)#USA
"""
#Static variable in class
"""
class Car:
    car_number = 0 

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_number += 1

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
car2 = Car("Jeep", "Rubicon")
car2 = Car("Toyota", "Fielder")

print(Car.car_number)
"""

#OOP (Object oriented programming)
#Inheritance
"""
#Super/Parents/ Base class 
class Animal:
    #Variable by constructor
    def __init__(self, animal_name):
        self.animal_name = animal_name

    #Method
    def animal_info(self):
        print(f"This is a {self.animal_name}")

#Instance from parent element
Dog = Animal("Dog")
Dog.animal_info()

#Child/derived/sub class
class Dog1(Animal):
   def bark(self):
      print("Woof Woof")

#Instance from child animal
Dog1 = Dog1("Cat")
Dog1.bark()
Dog1.animal_info()
"""
#Variable borrow from parent class

class Animal:
    def __init__(self, breed, color, speed):
        self.breed = breed
        self.color = color
        self.speed = speed

    def details(self):
        print(f"This is an {self.breed} and color is {self.color} but speed is {self.speed}")

class Dog(Animal):
    def __init__(self,animal_name, breed, color, speed):
        super().__init__(breed, color, speed)

        self.animal_name = animal_name

    def bark(self):
        print(f"The {self.animal_name} is a pet. It is a {self.breed} breed")

#Instance of Animal(Parent element)
Animal_Obj = Animal("German", "Brown", "Fast")
Animal_Obj.details()

#Instance of Dog Element(Child element)
Dog_Obj = Dog("Dimitri", "Persian", "White", "Slow")
Dog_Obj.bark()
Dog_Name = Dog_Obj.animal_name
print(Dog_Name)