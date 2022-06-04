from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

dataDic = data.to_dict(orient="records")
current_card = {}


def is_learn():
    dataDic.remove(current_card)
    df = pd.DataFrame(dataDic)
    df.to_csv("data/words_to_learn")
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_card_bg, image=card_back_img)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(dataDic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_card_bg, image=card_front_img)
    timer = window.after(3000, func=flip_card)


# ----------------------- CONFIG GUI -------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_card_bg = canvas.create_image(400, 260, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 260, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_learn)
right_button.grid(row=1, column=1)

timer = window.after(3000, func=flip_card)
next_card()
window.mainloop()
