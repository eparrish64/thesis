#!/bin/sh
export PATH=/usr/local/bin:/Library/TeX/texbin/:$PATH
#export PATH=/usr/local/bin:$PATH
echo "Updating dissertation progress"
DOCUMENT='/Users/tburch/Documents/gitDevelopment/thesis/thesisBurch.pdf'
TEX_DOC='/Users/tburch/Documents/gitDevelopment/thesis/thesisBurch.tex'
PROGRESSFILE='/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/progress.csv'
cd /Users/tburch/Documents/gitDevelopment/thesis/
WORDCOUNT=`texcount -sum -total -merge {$TEX_DOC} | grep "Sum count:" | tr -d "Sum count: "`
# Use this line in OSX
PAGECOUNT=`mdls -name kMDItemNumberOfPages -raw ${DOCUMENT}`
# Use this line in Linux
# PAGECOUNT=`pdfinfo mythesis.pdf | grep Pages | sed 's/[^0-9]*//'`
echo `date '+%Y-%m-%d %H:%M:%S'`,$WORDCOUNT,$PAGECOUNT >> $PROGRESSFILE
echo "Done! Page count ${PAGECOUNT}, word count ${WORDCOUNT}"

python /Users/tburch/Documents/gitDevelopment/thesis/progressTracking/plotProgress.py
