#!/bin/sh
### Script to remove ATLAS labels, provide by Louis D'Earmo

if [ $# -ne 2 ]; then
OUTPUT_NAME=$1
else
OUTPUT_NAME=$2
fi

gs -q -dNOCACHE -dNOPAUSE -dBATCH -dSAFER -sDEVICE=eps2write -sOutputFile=output.eps $1.pdf
sed -i -e 's/ATLAS/ /g' output.eps
sed -i -e 's/Internal/ /g' output.eps
sed -i -e 's/Simulation/ /g' output.eps
epstopdf output.eps --outFile="${OUTPUT_NAME}-temp.pdf"
pdfcrop --margin 10 "${OUTPUT_NAME}-temp.pdf" "${OUTPUT_NAME}.pdf"
rm output.eps "${OUTPUT_NAME}-temp.pdf" output.eps-e