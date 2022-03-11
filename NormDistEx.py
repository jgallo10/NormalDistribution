from random import random
import numpy as np

#function for Normal Disrobution
def normalDist(m, sd, num):
    num = np.random.normal(m, sd, num)
    return num

#me = mean, standard Deviation = standDev, num = range number
me = 5.0
standDev = 0.1
num = 10

print(normalDist(me, standDev, num))