import turtle

def draw_triangle(tim, points):
    tim.up() #Nothing is drawn when changing locations
    tim.goto(points[0][0],points[0][1]) #Go to bottom left of triangle
    tim.down()
    tim.goto(points[1][0],points[1][1]) #Draw to top of triangle
    tim.goto(points[2][0],points[2][1]) #Draw to bottom right of triangle
    tim.goto(points[0][0],points[0][1]) #Close the triangle

def calc_mid(p1, p2): #Calculate midpoint for subtriangles
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def triangle_recursion(tim, points, depth):
    draw_triangle(tim, points) #Base case
    if (depth > 0):
        #Bottom left subtriangle
        triangle_recursion(tim, [points[0], calc_mid(points[0], points[1]), calc_mid(points[0], points[2])], depth-1)
        #Top subtriangle
        triangle_recursion(tim, [calc_mid(points[0], points[1]), points[1], calc_mid(points[1], points[2])], depth-1)
        #Bottom right subtriangle
        triangle_recursion(tim, [calc_mid(points[0], points[2]), calc_mid(points[1], points[2]), points[2]], depth-1)
        
def main():
    tim = turtle.Turtle()
    tim.speed(10)
    tim.color("red")
    wn = turtle.Screen()
    wn.bgcolor("black")
    length = 400
    depth = 4
    points = [[-length,-length/2],[0,length],[length,-length/2]] #[Bottom left, Top, Bottom right]
    triangle_recursion(tim, points, depth) #Function for drawing triangle fractal
    wn.exitonclick()

main()
