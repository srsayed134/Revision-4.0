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