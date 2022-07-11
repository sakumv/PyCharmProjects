import turtle
import pandas

screen = turtle.Screen()
screen.title("US States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#screen.exitonclick()
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")

is_game_on = True
my_score = 0
t = turtle.Turtle()
t.penup()
t.hideturtle()
guessed_state = []
missed_state = []

while is_game_on:
    answer = screen.textinput(title=f"Guess state : {my_score}/50", prompt="Enter a state name")
    answer = answer.title()

    #Convert the guess to title case
    if answer == "Exit":
        # for stat in data.state:
        #     if stat not in guessed_state:
        #         missed_state.append(stat)
        missed_state = [stat for stat in data.state if (stat not in guessed_state)]

        data_frame = pandas.DataFrame(missed_state)
        data_frame.to_csv("missed_state.csv")

        break

    #Check if guess is among 50 states
    if len(data[data.state==answer]) > 0:
    #write correct guess on to the map
        #get the x and y coor
        state = data[data.state == answer]
        xcor = int(state.x)
        ycor = int(state.y)
        t.goto(xcor,ycor)
        t.write(answer)
        guessed_state.append(answer)
    #use a loop to guess the map
        my_score += 1
    #record the correct guesses
        if my_score == 50:
            is_game_on = False
    #keep track of the score




turtle.mainloop()