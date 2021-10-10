
# usage: python3 process_csv.py mouse_data.csv

import sys
from csv import DictReader
from tabulate import tabulate

path = sys.argv[1] # first argument is file path

rows = DictReader(open(path,'r'))
cols = rows.fieldnames

# build dictionary indexed by first column
sample = {}
for row in rows :
    idx = int(row[cols[0]])
    sample[idx] = row

# print out in tabular form
table = tabulate(
    [[sample[idx][c] for c in cols] for idx in sample],
    headers = cols)

print()
print(table)

# a few examples
print()
print('Examples:')
print()

p = 'weight'
i = 3
print(' 1. The {} of sample {} is {} grams'.format(p, i, sample[i][p]))

p = 'lot'
i = 7
print(' 2. The {} number of sample {} is {}'.format(p, i, sample[i][p]))

p = 'size'
i = 13
print(' 3. The {} of sample {} is {} cm'.format(p, i, sample[i][p]))

print()
