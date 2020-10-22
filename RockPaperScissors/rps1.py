import random
import sys

while True:
    print("Rock, Paper, Scissors?") 
    r = input()
    r = r.lower()
    a=random.randint(1, 3)
#    print(a)
    if r == "rock" and a == 1:
        print("Rock vs Rock! It's a DRAW!")
    if r == "rock" and a == 2:
        print("Rock vs Paper! YOU LOSE!! ")
    if r == "rock" and a == 3:
        print("Rock vs Scissors! YOU WIN!!!")
    if r == "paper" and a == 1:
        print("Paper vs Rock! YOU WIN!!!")
    if r == "paper" and a == 2:
        print("Paper vs Paper! It's a DRAW!")
    if r == "paper" and a == 3:
        print("Paper vs Scissors! YOU LOSE!!")
    if r == "scissors" and a == 1:
        print("Scissors vs Rock! YOU LOSE!!")
    if r == "scissors" and a == 2:
        print("Scissors vs Paper! YOU WIN!!!")
    if r == "scissors" and a == 3:
        print("Scissors vs Scissors! It's a DRAW!")
    print("Type withdraw to exit.")
    if r == "withdraw":
        print("Goodbye")
        sys.exit(0)
