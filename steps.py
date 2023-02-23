import matplotlib.pyplot as mat
from random import choice

"""
Big Note:
Each line starts at the coordinate (10, 10)
"""

#Used to help set boundaries for the lines - want them to stay in the first quadrant
x_axis_length = 20
y_axis_length = 20

#changes in the coordinate in terms on length
x_change = 1
y_change = 1

#where all the x and y coordinates will be stoed
x = [x_axis_length//2]
y = [y_axis_length//2]

#applied to the last coordinate in the line - up, right, down, left are their directions
vectors = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#this is where all the coordinates are randomly generated
while True:
    current_vector = choice(vectors)
    next_x_coord = x[-1] + current_vector[0] * x_change

    #checks if the line would intercept with the x-axis
    if next_x_coord <= 0:
        x.append(0)
        y.append(y[-1])
        break

    #checks if the line is going beyond the x-axis
    elif next_x_coord >= x_axis_length:
        x.append(x_axis_length)
        y.append(y[-1])
        break

    else:
        next_y_coord = y[-1] + current_vector[1] * y_change
        #checks if the line would intercept with the y-axis
        if next_y_coord <= 0:
            x.append(x[-1])
            y.append(0)
            break

        #checks if the line is going beyond the y-axis
        elif next_y_coord >= y_axis_length:
            x.append(x[-1])
            y.append(y_axis_length)
            break

        else:
            #This checks if there is another coordinate - prevents the line from intersecting with itself
            repetition = False
            for i in range(len(x)):
                if x[i] == next_x_coord:
                    if y[i] == next_y_coord:
                        repetition = True
                        break

            if not repetition:
                x.append(next_x_coord)
                y.append(next_y_coord)

    #this is to make it so that line can't have more than a certain number of line segments added to it
    if len(x) > 16: break

#give integer values to the axis
mat.xticks([num for num in range(0, x_axis_length+1)])
mat.yticks([num for num in range(0, y_axis_length+1)])

mat.plot(x, y, color="#F00F0F")
mat.show()
