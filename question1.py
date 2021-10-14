import random

winning_number = str(random.randrange(1, 11))
print("Enter a number between 1 - 10: ")
players_guess = input()

while players_guess != winning_number:
    print("wrong number, please try again:")
    players_guess = input()
    if(players_guess == winning_number):
        break
print("congrats! YOU WON!")