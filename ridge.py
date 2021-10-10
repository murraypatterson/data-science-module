
# usage: python3 ridge.py mouse_data.csv

import sys
from csv import DictReader
from math import sqrt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

path = sys.argv[1] # first argument is file path

rows = DictReader(open(path,'r'))
_, weight, size, *_ = rows.fieldnames # we just want weight and size

# gather weights and sizes
weights = []
sizes = []
for row in rows :
    weights.append(float(row[weight]))
    sizes.append(float(row[size]))

# computing the mean
def mean(xs) :
    return sum(xs) / float(len(xs))

# computing the variance
def variance(xs) :
    m = mean(xs)
    return sum([(x - m)**2 for x in xs]) / float(len(xs))

# computing standard deviation
def sd(xs) :
    v = variance(xs)
    return sqrt(v)

# mean +/- SD before and after adding outlier
print()
print('\tmean +/- SD')
print('\t'+20*'-')
print('weight\t{:.2f} +/- {:.2f}'.format(mean(weights), sd(weights)))
print('size\t{:.2f} +/- {:.2f}'.format(mean(sizes), sd(sizes)))
print('\t'+20*'-', '(after adding outlier)')

# add an outlier
weights += [4.]
sizes += [10.]

print('weight\t{:.2f} +/- {:.2f}'.format(mean(weights), sd(weights)))
print('size\t{:.2f} +/- {:.2f}'.format(mean(sizes), sd(sizes)))

# train / test split
training = [0,1,19]

# compute linear regression on training set (x,y)
x = np.array([weights[t] for t in training]).reshape((-1,1)) # transpose vector
y = np.array([sizes[t] for t in training])

lin = LinearRegression()
lin.fit(x, y)

a, *_ = lin.coef_
b = lin.intercept_
print()
print('linear equation is y = {:.2f}*x + {:.2f}'.format(a,b))
linfn = np.poly1d([a,b])

# compute ridge regression on training set (x,y)
ridge = Ridge(alpha = 10.)
ridge.fit(x, y)

a, *_ = ridge.coef_
b = ridge.intercept_
print('ridge equation is y = {:.2f}*x + {:.2f}'.format(a,b))
print()
ridgefn = np.poly1d([a,b])

# scatter plot with training, test set, and linear and ridge equations
plt.plot(weights, sizes, 'bo') # test set
plt.draw()

d = range(2,9) # reasonable range
plt.plot(x, y, 'ro', d, linfn(d), 'r') # overlay training set / linear
plt.draw()

plt.plot(weights, ridgefn(weights), 'k') # ridge
plt.show()
