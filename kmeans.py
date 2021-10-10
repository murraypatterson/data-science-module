
# usage: python3 kmeans.py mouse_data.csv

import sys
from csv import DictReader
import numpy as np
from sklearn.cluster import KMeans
from tabulate import tabulate
import matplotlib.pyplot as plt

path = sys.argv[1] # first argument is file path
k = int(sys.argv[2]) # second argument is k

rows = DictReader(open(path,'r'))
_, weight, size, *_ = rows.fieldnames # we just want weight and size

# gather weights and sizes
weights = []
sizes = []
for row in rows :
    weights.append(float(row[weight]))
    sizes.append(float(row[size]))

# compute a k-means clustering
cs = np.array([[x,y] for x,y in zip(weights, sizes)]) # preprocess

kmeans = KMeans(n_clusters = k).fit(cs)
labels = kmeans.labels_

# print cluster centers (the \mu_i)
print()
print('cluster centers:')
print()
print(tabulate(kmeans.cluster_centers_, headers = ['weight', 'size']))
print()

# move each point into its cluster
xs = [[] for i in range(k)]
ys = [[] for i in range(k)]
for i in range(len(labels)) :
    xs[labels[i]].append(weights[i])
    ys[labels[i]].append(sizes[i])

# plot each cluster with a different color
plt.plot(xs[0], ys[0], 'ro')
plt.plot(xs[1], ys[1], 'go')
plt.plot(xs[2], ys[2], 'bo')
plt.draw()
plt.show()
