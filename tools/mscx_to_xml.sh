#!/bin/sh

INDIR=$1
OUTDIR=$2
MSCORE="musescore" # might need to be adapted for different systems
PYTHON="python3"

# activate the python environment
source env/bin/activate

# go through all files in $INDIR
for file in "$INDIR"/*.mscx
do
    base=`basename -s .mscx "$file"`
    out="$OUTDIR/$base.xml"            # compute the output filename
    "$MSCORE" -o "$out" "$file"        # convert mscx to musicxml
    echo "add IDs to $out"
    "$PYTHON" add_ids.py "$out" "$out" # add note IDs
    echo "wrote $out"
done
