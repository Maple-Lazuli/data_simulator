#!/bin/bash

while getopts i:o: flag
do
    case "${flag}" in
        i) infile=${OPTARG};;
        o) outfile=${OPTARG};;
        *) ;;
    esac
done

if test -f "$infile"; then
  echo "Found: $infile"
else
  echo "Could not find $infile"
  echo "Exiting..."
  exit 1
fi

ksc -t graphviz "$infile"
dot -Tsvg gif.dot -o "$outfile"
rm gif.dot

if test -f "$outfile"; then
  echo "Created: $outfile"
else
  echo "Could not find $outfile"
  echo "Something went wrong."
  exit 1
fi
