from tkinter import *
import random
import tkinter.messagebox

window = Tk()
window.configure(bg="white")
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
frame.configure(bg="white")
frame.pack()

logo = PhotoImage(file="heading.png")
MyTitle = Label(frame, image=logo, font="Times 30 bold ", bg="white")
MyTitle.grid(columnspan=6, padx=10, pady=10, sticky=N)

photo1 = PhotoImage(file="rock.png")
photo2 = PhotoImage(file="paper.png")
photo3 = PhotoImage(file="scissor.png")

MyButton = Button(frame, image=photo1, command=lambda: compute('R'), bg="white")
MyButton.grid(row=1, column=0, padx=20, pady=10)

Button2 = Button(frame, image=photo2, command=lambda: compute('P'), bg="white")
Button2.grid(row=1, column=2, padx=20, pady=10)

Button3 = Button(frame, image=photo3, command=lambda: compute('S'), bg="white")
Button3.grid(row=1, column=4, padx=20, pady=10)

choice = Label(frame, font="Helvetica 18", bg="white")
choice.grid(columnspan=6, padx=15, pady=15)

result = Label(frame, font="Helvetica 20 bold", bg="white")
result.grid(columnspan=6, padx=15, pady=15)

user_score = Label(frame, font="Helvetica 18", bg="white")
user_score.grid(columnspan=6, padx=15, pady=15)

computer_score = Label(frame, font="Helvetica 18", bg="white")
computer_score.grid(columnspan=6, padx=15, pady=15)

quit_button = Button(frame, text="EXIT", font="16", bg="white", command=frame.quit)
quit_button.grid(columnspan=6, padx=15, pady=15)

tkinter.messagebox.showinfo('How to play', 'Click on the image to choose your move')

window.mainloop()
