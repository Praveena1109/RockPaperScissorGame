import tkinter
import random

window = tkinter.Tk()


def compute(user_input):
    computer_input = randomChoice()
    if user_input == 'R':
        if computer_input == 'ROCK':
            result.configure(text=" TIE")
        elif computer_input == 'PAPER':
            result.configure(text="YOU LOSE")
        else:
            result.configure(text="YOU WON")
        choice.configure(text="Computer chose : " + computer_input)

    elif user_input == 'P':
        if computer_input == 'ROCK':
            result.configure(text="YOU WON")
        elif computer_input == 'PAPER':
            result.configure(text=" TIE")
        else:
            result.configure(text="YOU LOSE")
        choice.configure(text="Computer chose : " + computer_input)

    else:
        if computer_input == 'ROCK':
            result.configure(text="YOU LOSE")
        elif computer_input == 'PAPER':
            result.configure(text="YOU WON")
        else:
            result.configure(text=" TIE")
        choice.configure(text="Computer chose : " + computer_input)


def randomChoice():
    lst = ['ROCK', 'PAPER', 'SCISSOR']
    x = random.choice(lst)
    return x


MyTitle = tkinter.Label(window, text="ROCK PAPER SCISSOR", font="Helvetica 10 ")
MyTitle.pack()

MyButton = tkinter.Button(window, text="Rock", command=lambda: compute('R'))
MyButton.pack()

Button2 = tkinter.Button(window, text="Paper", command=lambda: compute('P'))
Button2.pack()

Button3 = tkinter.Button(window, text="Scissor", command=lambda: compute('S'))
Button3.pack()

choice = tkinter.Label(window, font="Helvetica 10")
choice.pack()

result = tkinter.Label(window, font="Helvetica 16 bold")
result.pack()

window.mainloop()
