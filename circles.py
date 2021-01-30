import turtle 

size = 8

turtle.pensize(2)
turtle.color('white')
turtle.Screen().bgcolor('black')
turtle.hideturtle()
turtle.speed(52)

for i in range(30):
    turtle.circle(size)
    size += 5
    turtle.right(10)

turtle.Screen().exitonclick()