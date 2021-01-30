import turtle 

turtle.speed(34)

def rectangle(length: int):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

length = 32
gens = 48

for i in range(gens):
    rectangle(length)
    length += 7
    turtle.right(10)


turtle.Screen().exitonclick()