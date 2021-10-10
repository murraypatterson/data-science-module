
# usage: python3 statistics.py mouse_data.csv

import sys
from csv import DictReader
from math import sqrt
import seaborn as sns
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

# print out some descriptive statistics
print()
print('\tmean +/- SD')
print('\t'+20*'-')
print('weight\t{:.2f} +/- {:.2f}'.format(mean(weights), sd(weights)))
print('size\t{:.2f} +/- {:.2f}'.format(mean(sizes), sd(sizes)))
print()

# plot the distribution with seaborn/matplotlib
ax = sns.displot(data = weights, bins = 8)
ax.set(xlabel = 'weight in grams')
plt.show()

ax = sns.displot(data = sizes, bins = 8, color = 'g')
ax.set(xlabel = 'size in cm')
plt.show()
