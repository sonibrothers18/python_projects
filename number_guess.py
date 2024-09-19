import random

compNumber = random.randint(1, 100)
attempt = 0
yourNumber = 0

while(compNumber != yourNumber):
    yourNumber = int(input("Enter your number: "))

    if(yourNumber > compNumber):
        print("Guess lower number !")
        attempt += 1
    elif(yourNumber < compNumber):
        print("Guess higher number !")
        attempt += 1

print(f"You guess number {compNumber} in {attempt} attempt")