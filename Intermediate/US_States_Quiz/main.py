import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgcolor("white")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()




while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Guess an empty state (Say Exit to leave): ")
    if answer_state != None:
        answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coords = data[data["state"] == answer_state]
        t.goto(state_coords["x"].item(), state_coords["y"].item())
        t.write(answer_state)
        guessed_states.append(answer_state)



screen.exitonclick()

