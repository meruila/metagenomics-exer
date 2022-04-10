# Running a bioinformatic program

From: https://metag-crash-course.readthedocs.io/en/latest/blast/index.html  

`best-hit.py`, `count-up.py`, and `import-ann.py` were slightly changed to accommodate Python3.  

### For loop exercise - best hits
Command used was:  
```for x in metags/*fa.x.nifh.blastnout.tsv; do python3 ../scripts/best-hit.py $x > $x.best; done```