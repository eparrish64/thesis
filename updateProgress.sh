#!/bin/sh
export PATH=/usr/local/bin:/Library/TeX/texbin/:$PATH
#export PATH=/usr/local/bin:$PATH
echo "Updating dissertation progress"
DOCUMENT='/Users/eparrish/Work/thesis/thesisParrish.pdf'
TEX_DOC='/Users/eparrish/Work/thesis/thesisParrish.tex'
PROGRESSFILE='/Users/eparrish/Work/thesis/progressTracking/progress.csv'
cd /Users/eparrish/Work/thesis/
WORDCOUNT=`texcount -sum -total -merge {$TEX_DOC} | grep "Sum count:" | tr -d "Sum count: "`
# Use this line in OSX
PAGECOUNT=`mdls -name kMDItemNumberOfPages -raw ${DOCUMENT}`
# Use this line in Linux
# PAGECOUNT=`pdfinfo mythesis.pdf | grep Pages | sed 's/[^0-9]*//'`
echo `date '+%Y-%m-%d %H:%M:%S'`,$WORDCOUNT,$PAGECOUNT >> $PROGRESSFILE
echo "Done! Page count ${PAGECOUNT}, word count ${WORDCOUNT}"

python /Users/eparrish/Work/thesis/progressTracking/plotProgress.py
