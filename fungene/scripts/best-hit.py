# revised d.has_key(query) and print statement to fit python3
import sys

d = {}

for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    if query in d:
        continue
    else:
        d[query] = hit
        print(line) 