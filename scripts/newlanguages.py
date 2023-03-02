import sys

verss = '2.11 2.10 2.9 2.8 2.7 2.6 2.5 2.4 2.3 2.2 2.1 2.0 1.4 1.3 1.2 1.1 1.0'.split(' ')
verss.reverse()
#print(verss)

vers = {}

for line in sys.stdin:
	if not line:
		continue
	ver, lang = line.strip().split('\t')
	
	if ver not in vers:
		vers[ver] = set()

	vers[ver].add(lang)

seen = set()
for ver in verss:
	remainder = vers[ver] - seen
	seen = seen.union(vers[ver])

	print('%s\t%d\t%s' % (ver, len(remainder), ' '.join(list(remainder))))
