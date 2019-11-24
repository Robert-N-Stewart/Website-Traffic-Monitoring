#!/bin/bash

#gets the first and second time to collected to calculate interval
time1=$(sed -n 1p statsdata.tsv | sed 's/^\([[:digit:]]*\).*/\1/')
time2=$(sed -n 2p statsdata.tsv | sed 's/^\([[:digit:]]*\).*/\1/')
timeInterval=$(($time2 - $time1))

#gets collections per minute from interval
numberOfCollectionsPerMinute=$((60 / $timeInterval))

#creates temp tsv with only collections per minute
rm everyminutestatsdata.tsv 2> /dev/null
touch everyminutestatsdata.tsv
cat statsdata.tsv | head -1 > everyminutestatsdata.tsv
awk -v var="$numberOfCollectionsPerMinute" 'NR%var==0' statsdata.tsv > everyminutestatsdata.tsv

#creates calculations to get plot data with requests per minute
python plotHelper.py

#plots data
gnuplot < sitePloter.gnuplot  > rpsPlot.png

#removes temp files
rm plotdata.csv
rm everyminutestatsdata.tsv

display rpsPlot.png

