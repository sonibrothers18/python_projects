import random

yourChoice = input("Enter your choice: ")
compChoice = random.choice([-1, 0, 1])

gameRule = {
    "s" : -1,
    "w" : 0,
    "g" : 1
}

compRule = {
    -1 : "s",
    0 : "w",
    1 : "g"
}

print(f"Your choice is {yourChoice}, computer choice is {compRule[compChoice]}")
choice_to_number = gameRule[yourChoice]

if(compChoice == choice_to_number):
    print("Its a draw")

else:
    if(compChoice ==- 1 and choice_to_number == 1):
        print("You win!")

    elif(compChoice ==- 1 and choice_to_number == 0):
        print("You Lose!")

    elif(compChoice == 1 and choice_to_number ==- 1):
        print("You lose!")

    elif(compChoice == 1 and choice_to_number == 0):
        print("You Win!")

    elif(compChoice == 0 and choice_to_number ==- 1):
        print("You Win!")

    elif(compChoice == 0 and choice_to_number == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")