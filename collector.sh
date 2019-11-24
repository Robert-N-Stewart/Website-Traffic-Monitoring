#!/bin/bash
helper="--interval to control the collection interval"

#verifies --interval flag is properly used
if [ "$#" -ne 2 ]; then
	echo $helper
	exit 1
fi

case "$1" in

	--help)
		echo $helper
		exit 1
		;;
	--interval)
		interval=$2
		;;
	*)
		echo $helper
		exit 1 
		;;
esac

#verifies that interval is an int
re='^[0-9]+$'
if ! [[ $interval =~ $re ]] ; then
   echo "interval must be an integer value" 
   exit 1
fi

#creates data collection file and collects data in format ts
rm statsdata.tsv 2> /dev/null
touch statsdata.tsv
while :
do
	responce=$(curl -s http://localhost:8080/stats)

	four04=$(echo $responce | sed 's/.*404s:\ \([[:digit:]]*\).*/\1/')
	two00=$(echo $responce | sed 's/.*200s:\ \([[:digit:]]*\).*/\1/')
	five00=$(echo $responce | sed 's/.*500s:\ \([[:digit:]]*\).*/\1/')
	timeOfCollection=$(date +%s)
	echo -e "$timeOfCollection\t$two00\t$four04\t$five00"
	echo -e "$timeOfCollection\t$two00\t$four04\t$five00" >> statsdata.tsv
	sleep $interval

done
