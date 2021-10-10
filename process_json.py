
# usage: python3 process_json.py electronics_data.json | dot -T png -o tree.png

import sys
import json

path = sys.argv[1] # first argument is file path

data = json.load(open(path,'r'))

# print out JSON format to stderr
print(json.dumps(data, indent = 4), file = sys.stderr)

# get edges of JSON "tree"
edges = []
def get_edges(tree, parent = None) :

    category = tree['category']

    if parent is not None :
        edges.append((parent, category))

    for child in tree['subcategories'] :

        if isinstance(child, dict) :
            get_edges(child, parent = category) # recursive call
        else :
            edges.append((category, child))

get_edges(data)

# dump edge list in Graphvis DOT format
print('strict digraph tree {')
for edge in edges :
    print('  {0} -> {1};'.format(*edge))

print('}')

# NOTE: adapted from
# https://stackoverflow.com/questions/40118113/how-to-convert-json-data-into-a-tree-image
