#Greetings
print("Welcome to my computer quixz")

#Asking about playing interest
playing = input("Do you want to play? ")

#lower() will replace every YES,yEs,Yes,yeS to lowercase "yes "
if playing.lower() != "yes":
    quit()

print("Okay! Let's play")

#Player scroe
correct = 0
incorrect = 0


#Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    correct += 1
    
else:
    print("Incorrenct")
    incorrect += 1

#Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Corrent")
    correct += 1

else: 
    print('Incorrect')
    incorrect += 1
    

#Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Corrent")
    correct += 1
    
else: 
    print('Incorrect')
    incorrect += 1
    

#Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Corrent")
    correct += 1
    
else: 
    print('Incorrect')
    incorrect += 1

#Result summey 
print ("You got " + str(correct)+ " correct" +" answer")
print ("You got " + str(incorrect)+" incorrect" +" answer")
print ("You got" + str((correct / 4) * 100) + "%")