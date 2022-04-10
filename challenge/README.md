# A challenge exercise
This section contains output from the challenge exercise from the Fetching Data with the NCBI API tutorial.

> You've downloaded all the fasta files from a list. Modify the script to now download genbank files for a list of genomes of interest (not nifH -- genomes!, you can pick a phyla and download say 100 genomes IDs). Using shell commands you have learned in the past, can you count the number of 16S rRNA genes that are present in the file? Can you print out a list of all genes contained within the genomes? Note that you'll have to understand what genbank information is contained in a file.

###
Genome of interest: Lactobacillus amylovorus

### Command used to cut Lactobacillus amylovorus sequences to 100
```head -100 Lactobacillus-amylovorus_sequence.gi > 100-Lacto_amylo_seq.txt```

### Command used to concatenate all files to one
```cat Lactobacillus-amylovorus_genbank_seqs/* > all-Lacto-amylo.fa```

### 16S rRNA genes present in all-Lacto-amylo.fa
There are **21** 16S rRNA genes. This was counted using this command:
```grep "product=\"16S ribosomal RNA\"" all-Lacto-amylo.fa | wc```