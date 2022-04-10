# Fungene is FUN!
From: https://metag-crash-course.readthedocs.io/en/latest/blast-fungene/index.html

Command for getting best hits of corn, prairie, and soybean is found below:  
```for x in metags/*fa.x.nifh.blastnout.tsv; do python3 ../scripts/best-hit.py $x > $x.best; done```