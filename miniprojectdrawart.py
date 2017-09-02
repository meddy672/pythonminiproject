import turtle

def flower_head(some_turtle):
    
    some_turtle.forward(50)
    some_turtle.right(-45)
    some_turtle.forward(50)
    some_turtle.right(45)
    some_turtle.backward(50)
    some_turtle.left(45)
    some_turtle.backward(50)
    
def draw_flower_stem(some_turtle):
    print(some_turtle.pos())
    some_turtle.setpos(0,-270)
    
       
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(3)
    practice(brad)
    for i in range(1, 37):
        practice(brad)
        brad.right(10)
    draw_stem(brad)


    window.exitonclick()

draw_art()
        

