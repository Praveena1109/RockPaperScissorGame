from tkinter import *
import random

window = Tk()

u = 0
c = 0


def compute(user_input):
    computer_input = randomChoice()

    if user_input == 'R':
        if computer_input == 'ROCK':
            result.configure(text=" TIE")
        elif computer_input == 'PAPER':
            result.configure(text="YOU LOSE")
            globals()['c'] += 1
        else:
            result.configure(text="YOU WON")
            globals()['u'] += 1
        choice.configure(text="Computer chose : " + computer_input)
        user_score.configure(text="User's score : " + str(u))
        computer_score.configure(text="Computer's score : " + str(c))

    elif user_input == 'P':
        if computer_input == 'ROCK':
            result.configure(text="YOU WON")
            globals()['u'] += 1
        elif computer_input == 'PAPER':
            result.configure(text=" TIE")
        else:
            result.configure(text="YOU LOSE")
            globals()['c'] += 1
        choice.configure(text="Computer chose : " + computer_input)
        user_score.configure(text="User's score : " + str(u))
        computer_score.configure(text="Computer's score : " + str(c))

    else:
        if computer_input == 'ROCK':
            result.configure(text="YOU LOSE")
            globals()['c'] += 1
        elif computer_input == 'PAPER':
            result.configure(text="YOU WON")
            globals()['u'] += 1
        else:
            result.configure(text=" TIE")
        choice.configure(text="Computer chose : " + computer_input)
        user_score.configure(text="User's score : " + str(u))
        computer_score.configure(text="Computer's score : " + str(c))


def randomChoice():
    lst = ['ROCK', 'PAPER', 'SCISSOR']
    x = random.choice(lst)
    return x


frame = Frame(window)
frame.pack()

MyTitle = Label(frame, text="ROCK PAPER SCISSOR", font="Helvetica 18 ")
MyTitle.grid(columnspan=6)

MyButton = Button(frame, text="Rock", font="12", command=lambda: compute('R'))
MyButton.grid(row=1, column=0, padx=4, pady=4)

Button2 = Button(frame, text="Paper", font="12", command=lambda: compute('P'))
Button2.grid(row=1, column=2, padx=4, pady=4)

Button3 = Button(frame, text="Scissor", font="12", command=lambda: compute('S'))
Button3.grid(row=1, column=4, padx=4, pady=4)

choice = Label(frame, font="Helvetica 15")
choice.grid(columnspan=6, padx=4, pady=4)

result = Label(frame, font="Helvetica 16 bold")
result.grid(columnspan=6, padx=4, pady=4)

user_score = Label(frame, font="Helvetica 15")
user_score.grid(columnspan=6, padx=4, pady=4)

computer_score = Label(frame, font="Helvetica 15")
computer_score.grid(columnspan=6, padx=4, pady=4)

quit_button = Button(frame, text="EXIT", font="15", command=frame.quit)
quit_button.grid(columnspan=6, padx=4, pady=4)

window.mainloop()
