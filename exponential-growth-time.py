from pylab import *

a = 2.

def initialize():
    global x, result, t, timesteps ###
    x = 1.

    result = [x]
    t = 0. ###
    timesteps = [t] ###
    
def observe():
    global x, result, t, timesteps ###
    result.append(x)
    timesteps.append(t) ###

def update():
    global x, result, t, timesteps ###
    #x = x*a
    x = (-((a-1)/x)*x+a)*x
    t = t + 0.1 ###

initialize()
while t < 3.: ###
    update()
    observe()

print(result)
plot(timesteps, result) ###

show()
