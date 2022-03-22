import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

data=[4,2,6,5,7,7,6,8,5,5,5,4,6,5,2,6,4,6,4,8,4,5,3,3,3]

mu, std = norm.fit(data)
plt.hist(data, bins=5,density=True,alpha=0.5,color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Coin Tossing: mu = %.2f, std = %.2f" %(mu, std)
plt.title(title)
plt.show()