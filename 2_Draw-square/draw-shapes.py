import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    draw_square()
    draw_circle()
    draw_triangle()
    
    window.exitonclick()

def draw_square(): 
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(3)
    for num in range(4): 
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(50)

def draw_triangle():
    peter = turtle.Turtle()
    peter.shape("triangle")
    peter.color("yellow")
    for num in range(3): 
        peter.forward(100)
        peter.right(120)

draw_shapes()
