import tkinter
import pandas
import random




BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
words = {"French": [w["French"] for w in to_learn], "English": [w["English"] for w in to_learn]}

random_index = 0

def next_word():
    global flip_timer
    global random_index
    window.after_cancel(flip_timer)
    random_index = random.randint(0, len(words["French"]) - 1)
    current_card = words["French"][random_index]
    canvas.itemconfig(card_word, text = current_card, fill = "black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text= words["English"][random_index], fill = "white")
    canvas.itemconfig(card_image, image = card_back)

def is_known():
    global random_index
    words["French"].pop(random_index)
    words["English"].pop(random_index)
    print(len(words["French"]))
    next_word()

#Window Creation
window = tkinter.Tk()
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashcards")
flip_timer = window.after(3000, func = flip_card)





#Flashcard Creation

canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_word = canvas.create_text(400, 263, text ="Word" , font=("Arial", 60, "bold"))
card_title = canvas.create_text(400, 150, text = "Title", font=("Arial", 40, "italic"))
canvas.grid(row = 0, column = 0, columnspan= 2)

#Button Creation

wrong = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image = wrong, background=BACKGROUND_COLOR, highlightthickness=0, command = next_word)
wrong_button.grid(row = 1, column = 0)


correct = tkinter.PhotoImage(file="images/right.png")
correct_button = tkinter.Button(image = correct, background=BACKGROUND_COLOR, highlightthickness=0, command = is_known)
correct_button.grid(row = 1, column = 1)










window.mainloop()



