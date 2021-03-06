#!/usr/bin/python3

from urllib.request import urlopen
import os
import sys
import time

if len(sys.argv) != 3:
    print("USAGE: fetch_genome.py <genome_id_list> <out_dir>")
    sys.exit(1)

url_template = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"

os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".fa")
    if os.path.exists(gbk_out_file):
        print("already fetched")
    url = urlopen(url_template % id).read()
    # print(url)
    open(gbk_out_file, "wb").write(url)
    print("Done")
    time.sleep(1.0/3)