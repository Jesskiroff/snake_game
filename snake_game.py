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
    segment.penup()
    segment.goto(position)
    segments.append(segment)


screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
        
        





screen.exitonclick()