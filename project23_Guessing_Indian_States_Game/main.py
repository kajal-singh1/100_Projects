import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "100_Projects/project23/Indian_States.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("100_Projects/project23/states_coordinates.csv")
data_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct", prompt="what's the next state name").title()
    if ans_state == "Exit":
        missing_state = []
        for state in data_list:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if ans_state in data_list:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)


screen.exitonclick()