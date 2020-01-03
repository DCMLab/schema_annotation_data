#!/bin/sh

indir=$1
outdir=$2
convert="musicxml2json" # might need to be adapted for different systems
opts="-up" # unfold and pretty-print

# go through all files in $INDIR
for file in "$indir"/*.xml
do
    base=`basename -s .xml "$file"`
    out="$outdir/$base.json"        # compute the output filename
    "$convert" "$file" "$out" $opts # convert mscx to musicxml
    echo "wrote $out"
done
