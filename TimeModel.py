
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#import matplotlib.animation as animation 
from matplotlib.widgets import Slider, Button, RadioButtons
# use python to select some of the data
#
# Simple python program to calculate s as a function of t. 
# Any line that begins with a '#' is a comment.
# Anything in a line after the '#' is a comment.
#


#First let's clear the plot from any previous times that we ran the code


# Here is the raw data for the position of the muffin cup as a function of time. Use the "split" function to break it into
# a list of (possibly empty) strings.
#

data = """1.000000000E-1 5.500000000E-1
1.333333333E-1 7.226620928E-1
1.666666667E-1	8.748054218E-1
2.000000000E-1	1.007612020E0
2.333333333E-1	1.122195826E0
2.666666667E-1	1.219606608E0
3.000000000E-1	1.300833660E0
3.333333333E-1	1.366809285E0
3.666666667E-1	1.418412077E0
4.000000000E-1	1.456470018E0
4.333333333E-1	1.481763393E0
4.666666667E-1	1.495027535E0
5.000000000E-1	1.496955416E0
5.333333333E-1	1.488200091E0
5.666666667E-1	1.469376989E0
6.000000000E-1	1.441066091E0
6.333333333E-1	1.403813964E0
6.666666667E-1	1.358135687E0
7.000000000E-1	1.304516672E0
7.333333333E-1	1.243414361E0
7.666666667E-1	1.175259850E0
8.000000000E-1	1.100459397E0
8.333333333E-1	1.019395857E0
8.666666667E-1	9.324300310E-1
9.000000000E-1	8.399019342E-1
9.333333333E-1	7.421319947E-1
9.666666667E-1	6.394221813E-1
1.000000000E0	5.320570676E-1
1.033333333E0	4.203048333E-1
1.066666667E0	3.044182091E-1
1.100000000E0	1.846353664E-1
1.133333333E0	6.118075646E-2
1.166666667E0	-6.573409982E-2
1.200000000E0	-1.959098666E-1
1.233333333E0	-3.291586912E-1
1.266666667E0	-4.653035428E-1
""".splitlines()  # split this string on the "newline" character.

print("We have", len(data), "data points.")

#
# Here we'll take the list of strings defined above and break it into actual numbers in reasonable units.
#

tlist = []
ylist = []
for s in data:
    t,y = s.split()     # break string in two
    t=float(t)          # convert time to float
    y=float(y)   # convert distance (in meters) to float
    tlist.append(t)
    ylist.append(y)
        
print ("tlist=",tlist)
print ("ylist=",ylist)


vlist = []  # Velocity list (computed velocities from experimental data)
tvlist = []  # time list (times for corresponding velocities)
for i in range(1,len(tlist)):
    dy=ylist[i]-ylist[i-1]
    dt=tlist[i]-tlist[i-1]
    vlist.append(dy/dt)
    tvlist.append((tlist[i]+tlist[i-1])/2.0)

    
# these are the physical parameters that you need to modify

m=0.005125  # kg
g=9.8     # m/s^2
b=0.035    # total guess, need to improve
v=0.0    # start with zero velocity

#plt.clf() 
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

b0 = b
dt = (tlist[-1]-tlist[0])/(len(tlist)-1)  # time per frame in original video
t=0.0

vclist = [v]
tclist = [t]

def deriv(v, t):
    return b*v**2/m - g

for i in range(len(tlist)):
    dv = deriv(v,t)*dt
    v += dv
    t += dt
    
    vclist.append(v)
    tclist.append(t)
    
fig, axs = plt.subplots(2)
fig.suptitle("Comparison of experimental and drag model")
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel('velocity along y (m/s)')
axs[0].set_ylabel('position along y (m)')
axs[1].plot(tvlist,vlist,'g.',tclist,vclist)
axs[0].plot(tlist,ylist,'r.')


plt.show()

# 

