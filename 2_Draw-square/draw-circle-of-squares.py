import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    draw_circle_of_squares()
    draw_circles()
    
    window.exitonclick()

def draw_circle_of_squares(): 
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(20)

    for num in range(36): 
        for num in range(4): 
            brad.forward(100)
            brad.right(90)
        brad.right(10)

def draw_circles():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")

    for num in range(4): 
        angie.circle(50)
        angie.right(90)

draw_shapes()
