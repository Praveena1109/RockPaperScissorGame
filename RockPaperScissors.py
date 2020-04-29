import random


def play(computer_input, user_input, computer_score, user_score):
    if user_input == 'R':
        if computer_input == 'RO':
            print("The computer chose Rock : TIE ")
        elif computer_input == 'PA':
            print("The computer chose Paper : YOU LOSE ")
            computer_score += 1
        else:
            print("The computer chose Scissors : YOU WON ")
            user_score += 1
    elif user_input == 'P':
        if computer_input == 'RO':
            print("The computer chose Rock : YOU WON ")
            user_score += 1
        elif computer_input == 'PA':
            print("The computer chose Paper : TIE ")
        else:
            print("The computer chose Scissors : YOU LOSE ")
            computer_score += 1
    elif user_input == 'S':
        if computer_input == 'RO':
            print("The computer chose Rock : YOU LOSE ")
            computer_score += 1
        elif computer_input == 'PA':
            print("The computer chose Paper : YOU WON  ")
            user_score += 1
        else:
            print("The computer chose Scissors : TIE")
    elif user_input == 'E':
        print("EXITING...THANK YOU FOR PLAYING")
    else:
        print("Enter a valid option")
    return computer_score, user_score


y = None
i = 0
j = 0
while y != 'E':
    lst = ['RO', 'PA', 'SI']
    x = random.choice(lst)
    print("WHAT DO U CHOOSE?")
    print("FOR ROCK : PRESS R")
    print("FOR PAPER : PRESS P")
    print("FOR SCISSORS : PRESS S")
    print("FOR EXIT : PRESS E ")
    y = input()
    y = y.upper()
    i, j = play(x, y, i, j)
print("FINAL SCORES")
print("COMPUTER SCORE: ", i)
print("YOUR SCORE: ", j)

