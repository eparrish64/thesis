#!/bin/sh
export PATH=/usr/local/bin:$PATH
echo "Updating dissertation progress"
DOCUMENT='/Users/tburch/Documents/gitDevelopment/thesis/mythesis.pdf'
PROGRESSFILE='/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/progress.csv'
WORDCOUNT=`ps2ascii ${DOCUMENT} | wc -w`
# Use this line in OSX
PAGECOUNT=`mdls -name kMDItemNumberOfPages -raw ${DOCUMENT}`
# Use this line in Linux
# PAGECOUNT=`pdfinfo mythesis.pdf | grep Pages | sed 's/[^0-9]*//'`
echo `date '+%Y-%m-%d %H:%M:%S'`,$WORDCOUNT,$PAGECOUNT >> $PROGRESSFILE
echo "Done! Page count ${PAGECOUNT}, word count ${WORDCOUNT}"
