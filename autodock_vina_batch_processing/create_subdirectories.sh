#!/bin/bash
dir_size=3000
dir_name="dir"
count=$((`find . -maxdepth 1 -type f | wc -l`/$dir_size+1))
for i in `seq 1 $count`;
do
    mkdir -p "$dir_name$i";
    find . -maxdepth 1 -type f | head -n $dir_size | xargs -i mv "{}" "$dir_name$i"
done
