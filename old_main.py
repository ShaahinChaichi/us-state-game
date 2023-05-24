# # TODO: My version Finished almost finished,but need Improvement
# def start_game():
#     game_is_on = True
#     while game_is_on:
#         select_state = screen.textinput(title="Please enter a state", prompt="Please guess a state: ")
#         state_data = data[data["state"] == select_state]
#         position = turtle.Turtle()
#         if select_state in state_data.values:
#             x_y_coordinate = (state_data.values[0][1], state_data.values[0][2])
#             position.penup()
#             position.goto(x_y_coordinate)
#             position.write(state_data.values[0][0])
#             start_game()
#
#         position.penup()
#         position.goto(0, 240)
#         position.write("Wrong")
#         game_is_on = False
#
#     screen.exitonclick()
#
#
# start_game()
