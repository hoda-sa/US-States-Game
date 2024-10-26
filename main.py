import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_correct = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States", prompt="What's another state name?").title()
    if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states] #using list comprehension
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.up()
        t.hideturtle()
        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data.state == answer_state].y.item()
        t.goto(x_cor,y_cor)
        t.write(answer_state)
        guessed_states.append(answer_state)
        states_correct += 1



