#!/usr/bin/env python3

import matplotlib.pyplot as plt

plt.box(False)

img = plt.imread('blank-world-map.png')

width = 2048*3
height = 1024*3

fig, ax = plt.subplots(figsize=(width/1000.0,height/1000.0), frameon=False)
ax.imshow(img, extent=(0, width, 0, height))

ax.set_axis_off()
ax.set_xlim(left=0, right=width)
ax.set_ylim(bottom=0, top=height)

with open('mapdata.tsv') as fin:
    lines = [l.split('\t') for l in fin.readlines() if '.' in l and '#' not in l]

code2ver = {}
with open('versions.tsv') as fin:
    for line in fin:
        ls = line.split()
        if len(ls) > 2:
            for c in ls[2:]:
                code2ver[c] = ls[0]

ver = list(set(code2ver.values()))

print(code2ver)
print(ver)

ax.scatter(
    [width*((float(l[1]) + 180) % 360)/360 for l in lines],
    [height*((90+float(l[2])) / 180) for l in lines],
    s=2,
    c = [ver.index(code2ver[l[0]]) for l in lines]
    #c=[l[0] for l in lines]
)

plt.savefig('map.png', dpi=1000)
