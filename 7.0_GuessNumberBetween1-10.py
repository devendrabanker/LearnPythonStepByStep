#Goal: This program is to guess a number between 1-10
#Input: Any number between 1-10
#output : if number is correct => we win else, try one more time

import random

programSelectedRandomNumber = random.randint(1,10)
#print(f"randomIndex = {randomIndex}")

while True:
    userEnteredNumber=int(input("Enter your guess number: "))
    print(f"User has guessed {userEnteredNumber}")
    if userEnteredNumber == programSelectedRandomNumber:
        print(f"You Win : correctly guessed number = {programSelectedRandomNumber}")
        break
    else:
        print(f"You Missed : Better luck next time!!")
    