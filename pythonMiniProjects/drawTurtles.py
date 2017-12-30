import turtle

def draw_square(a_turtle,size):
	for x in range(4):
		a_turtle.forward(size)
		a_turtle.right(90)

def draw_square_circles(a_turtle,size):
	for x in range (45):
		draw_square(a_turtle,size)
		a_turtle.right(8)

def draw_multiple_square_circle(a_turtle,initial_size):
	for x in range (1,6):
		draw_square_circles(a_turtle,initial_size/x)

def draw_triangle(a_turtle,size):
	for x in range(3):
		a_turtle.forward(size)
		a_turtle.right(120)

def drawr_triangle_circles(a_turtle,size):
	for x in range (45):
		draw_triangle(a_turtle,size)
		a_turtle.left(8)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(400)

	draw_multiple_square_circle(brad,200)

	brad.color("yellow")
	drawr_triangle_circles(brad,100)

	window.exitonclick()


	
	
draw_art()