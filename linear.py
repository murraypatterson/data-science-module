
# usage: python3 linear.py mouse_data.csv

import sys
from csv import DictReader
import numpy as np
from sklearn.linear_model import LinearRegression
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

# compute linear regression between weight (x) and size (y)
x = np.array(weights).reshape((-1,1)) # transpose vector
y = np.array(sizes)

lin = LinearRegression()
lin.fit(x, y)

r2 = lin.score(x, y) # residuals
print()
print('sum of squared residuals r^2 = {:.2f}'.format(r2))

a, *_ = lin.coef_
b = lin.intercept_
print('linear equation is y = {:.2f}*x + {:.2f}'.format(a,b))
linfn = np.poly1d([a,b])

# make some predictions based on this
x1, x2 = [10, 20]
y1, y2 = lin.predict(np.array([x1, x2]).reshape((-1,1)))
print()
print('a mouse of weight {} would have size roughly {}'.format(x1, y1))
print('a mouse of weight {} would have size roughly {}'.format(x2, y2))
print()

# scatter plot with linear equation overlayed
plt.plot(x,y, 'bo', x, linfn(x), 'r')
plt.show()
