import turtle 

def triangle(length):
    turtle.hideturtle()
    turtle.color('green')
    turtle.pensize(5)
    turtle.speed(52)
    turtle.Screen().bgcolor("black")
    for i in range(3):
        for j in range(10):
            turtle.forward(length)
            length += 13
            turtle.left(120)

length = 32
gens = 10

triangle(length)
turtle.Screen().exitonclick()
