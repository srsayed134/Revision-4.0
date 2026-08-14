"""
import random

#Getting random number's limit form player
input_limit_number= input("Input a limit number: ")

#Check inputed number validity
if input_limit_number.isdigit():
    input_limit_number = int(input_limit_number)

#Create random number according to palyer limit
random_number = random.randint(0, input_limit_number)

#Store how many times player guess
guess = 0
print(f"Guess any number in between from 0 to {input_limit_number} number: ")
#Run loop to find match
while True:
    guess += 1
    guess_number = input("Your guess: ")
    #Check input validity
    if guess_number.isdigit():
        guessed_number = int(guess_number)
        #Increment guess number
    else:
        print("Input valid number next time")
        #Looping the input for wrong guess
        continue

    if guessed_number == random_number:
        print("Congrets you have matched")
        #Stop while loop when matched
        break
    elif guessed_number > random_number:
        print("You are above the random number")
    else:
        print ("You are below the random number")


print(f"You have gueesed {str(guess)} times")
"""
Day:1

import random

inputed_number = input("Type a valid number: ")
if inputed_number.isdigit():
    inputed_number = int(inputed_number)

input_random_number = random.randint(0, inputed_number)
guess = 0

while True:
    guess += 1
    getting_random_number = input(f"Give a number in between of {inputed_number}: " )
    if getting_random_number.isdigit(): 
        getting_random_number = int(getting_random_number)
    else:
        print("Write a valid number in next time")
        continue

    if getting_random_number == input_random_number:
        print("Congrets your guessed number is correct")
        break
    elif getting_random_number > input_random_number:
        print("You are above of random number")
    else:
        print("You are below of random nuber")
print(f"You have guess {guess} times")
        