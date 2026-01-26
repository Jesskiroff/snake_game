from turtle import Screen, Turtle, time


screen = Screen()
screen.setup(width= 500, height= 500)
screen.bgcolor("black")
screen.title("The Snake Game")


starting_positions = [(0,0), (-20,0), (-40,0)]


segments = []


for position in starting_positions:
    segment= Turtle("square")
    segment.color("white")
    segment.goto(position)





screen.exitonclick()