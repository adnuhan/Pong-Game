from turtle import Screen, Turtle
import singleplayer
import multiplayer

window = Screen()
window.setup(width=800, height=600)
window.title("Pong Game")
window.bgcolor("Black")
window.tracer(0)

turtle = Turtle()
turtle.color("white")
turtle.speed(0)
turtle.hideturtle()

# Solo Button
turtle.penup()
turtle.goto(-41, 50)
turtle.write("Solo", move=False, font=("Courier", 24, "bold"))
turtle.goto(-46, 50)
turtle.pendown()
for a in range(2):
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(38)
    turtle.left(90)

# Multi Button
turtle.penup()
turtle.goto(-50, -50)
turtle.write("Multi", move=False, font=("Courier", 24, "bold"))
turtle.goto(-55, -50)
turtle.pendown()
for b in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(38)
    turtle.left(90)


def style(x, y):
    """Allows you to choose between Single-Player and Multiplayer"""
    if -46 < x < 40 and 50 < y < 88:
        window.clear()
        singleplayer.SinglePlayer()
    elif -55 < x < 45 and -50 < y < -12:
        window.clear()
        multiplayer.Multiplayer()


window.listen()
window.onscreenclick(style)
window.update()
window.mainloop()
