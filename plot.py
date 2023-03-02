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

def lat2x(lat):
    return width*((float(lat) + 180) % 360)/360
def lon2y(lon):
    return height*((90+float(lon)) / 180)

langs = {}
with open('mapdata.tsv') as fin:
    for line in fin:
        if '.' in line and '#' not in line:
            ls = line.strip().split('\t')
            langs[ls[0]] = (ls[1], ls[2])

with open('versions.tsv') as fin:
    for line in fin:
        ls = line.split()
        color = ls[0]
        mark = ls[1]
        codes = ls[4:]
        ax.scatter([lat2x(langs[x][0]) for x in codes],
                   [lon2y(langs[x][1]) for x in codes],
                   s=2,
                   c=color,
                   marker=mark)
plt.savefig('map.png', dpi=1000)
