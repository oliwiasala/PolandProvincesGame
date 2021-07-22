import turtle
import pandas

screen = turtle.Screen()
screen.addshape("provinces_img.gif")
screen.title("Poland Provinces Game")
turtle.shape("provinces_img.gif")

data = pandas.read_csv("provinces.csv")
all_provinces = data.province.to_list()
guessed_provinces = []


def show_province():
    x_coor = int(data[data.province == answer_province].x)
    y_coor = int(data[data.province == answer_province].y)
    new_province = turtle.Turtle()
    new_province.hideturtle()
    new_province.penup()
    new_province.setposition(x_coor, y_coor)
    new_province.write(answer_province)


while len(guessed_provinces) < 16:
    answer_province = turtle.textinput(title=f"{len(guessed_provinces)}/16 guessed provinces",
                                       prompt="What's another province's name?").lower()

    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        show_province()
    elif answer_province == "exit":
        missed_provinces = [province for province in all_provinces if province not in guessed_provinces]
        missed_provinces_data = pandas.DataFrame(missed_provinces)
        missed_provinces_data.to_csv("provinces_to_learn.csv")
        break
