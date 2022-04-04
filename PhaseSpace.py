from pylab import *

s, y = 1,1

xval, yval = meshgrid(arange(-10, 10, .1), arange(-4, 4, .1))

x_dot = xval - xval * yval
y_dot= -(s/y)*sin(xval)
streamplot(xval, yval, x_dot, y_dot)

grid()
show()