import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")


while True:
    select_state = screen.textinput(title="Please enter a state", prompt="Please guess a state: ")
    state_data = data[data["state"] == select_state]
    x_coordinate = state_data.values[0][1]
    y_coordinate = state_data.values[0][2]
    x_y_coordinate = (x_coordinate, y_coordinate)
    # print(x_y_coordinate)
    position = turtle.Turtle()
    position.penup()
    position.goto(x_y_coordinate)
    position.write(state_data.values[0][0])

screen.exitonclick()
