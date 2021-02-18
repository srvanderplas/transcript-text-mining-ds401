#!/bin/bash

# Set up files for LAREX

LAREXDIR=/home/susan/Projects/CSAFE/2020-legal-transcript-text-mining/ #tools/LAREX
# filedir=src/main/webapp/resources/books/
filedir=data/ocr4all/

# Read in arguments from the command line
while getopts d:o:i: flag
do
  case "${flag}" in
    # dir for input
    d) DIR=${OPTARG};;
    # dir for output
  esac
done

shopt -s nullglob


## Make list of files
s1files="$DIR/*.pdf"


# Altered from https://stackoverflow.com/questions/31105241/imagemagick-parallel-conversion
convertPageToPNG(){
    ## Expecting filename as first parameter and page number as second
    # echo DEBUG: File: $1 Page: $2 Newpage: $3
    noexten=${1%%.*}

    ## Convert to four-digit integer
    arg2=$(printf '%04d' "$2")
    convert -density 300 -quality 100 "$1[$2]" "$3/$arg2.png"
}

# Export function for use later in script
export -f convertPageToPNG

for f in $s1files
do
  # Get number of pages
  npages=$(qpdf --show-npages "$f")
  ## This doesn't work with the parallel implementation,
  ## but leaving it for clarity
  #echo "Document Name: $f"
  #echo "Document is $npages pages long"

  ## Clean up names
  name=${f%.pdf}
  name=${name##*/}

  mkdir -p "$LAREXDIR/$filedir/$name";
  mkdir -p "$LAREXDIR/$filedir/$name/input";
  newpg="$LAREXDIR/$filedir/$name/input"

  ## Pass pages to parallel one at a time (outside the double loop)
  for ((i=0;i<$npages;i++)); do
    echo "$f:$i:$newpg"
  done
done | parallel --eta --colsep ':' convertPageToPNG {1} {2} {3}

echo "Conversion to images: Done!"
