import turtle 

def spiral(size, iterator): # размер, количество увеличиваний
    turtle.color("red")
    turtle.Screen().bgcolor('black')
    turtle.pensize(3)
    turtle.hideturtle()
    turtle.speed(66)
    for i in range(gens):
        turtle.forward(size) 
        turtle.left(90)
        turtle.right(10)
        size += iterator


length = 8
iterator = 5
gens = 50

spiral(length, iterator)

turtle.Screen().exitonclick()