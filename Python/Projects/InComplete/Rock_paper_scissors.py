import random

getting_permission = input("Do you want to play rock, paper ans scissor: ")
if getting_permission.lower() == "yes":
    print("Okay lets play")

human_answer = input("1.Rock 2.Paper 3.Scissors: ")
human_guess = "Rock"
if human_answer == 1:
    human_guess = "Rock"
elif human_guess == 2:
    human_guess = "Paper"
elif human_guess == 3:
    human_guess = "Scissors"


random_number = random.randint(1,3)
computer_guess = "Rock"
if random_number == 1:
    computer_guess = "Rock"
elif random_number == 2:
    computer_guess = "Paper"
elif random_number == 3:
    computer_guess = "Scissors"


#Not complete or uodated