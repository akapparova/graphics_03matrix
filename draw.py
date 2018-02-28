from display import *
from matrix import *

def draw_lines( matrix, screen, color ):
    x = matrix[0]
    y = matrix[1]
    for i in range(len(x) - 1): 
        draw_line(x[i], y[i], x[i+1], y[i+1], screen, color)


def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y
    B = x - x1

    if (B == 0): 
        if (y < y1):
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
        elif (y > y1):
            while (y1 <= y):
                plot(screen, color, x, y)
                y -= 1

                
    elif (A == 0): 
        while (x <= x1):
            plot(screen, color, x, y)
            x += 1
    else:
        slope = A / (B * -1)



        
        if (slope >= 0 and slope <= 1):
            d = 2 * A + B
            while (x <= x1):
                plot(screen, color, x, y)
                if (d > 0):
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A



                
        elif (slope > 1):
            d = A + 2 * B
            while (y <= y1):
                plot(screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B



                
        elif (slope < 0 and slope >= -1):
            d = 2 * A - B
            while (x <= x1):
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A



                
        elif (slope < -1):
            d = A - 2 * B
            while (y >= y1):
                plot(screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B