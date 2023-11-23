from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/to_learn_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words_dict = data.to_dict(orient="records")

card = {}


def know():
    choose_random()
    words_dict.remove(card)
    datas = pandas.DataFrame(words_dict)
    datas.to_csv("data/to_learn_words.csv", index= False)


def choose_random():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(words_dict)
    french_word = card["French"]
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(title, text="French", fill="black")
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, flip)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 270, image=front)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
word = canvas.create_text(400, 263, font=("Arial", 40, "bold"), text="word")
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=choose_random)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=know)
right.grid(row=1, column=1)

choose_random()
window.mainloop()
