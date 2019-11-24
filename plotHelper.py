#!/bin/python

import csv
import itertools

#opens temp file that contains only data every minute
f1 = open("everyminutestatsdata.tsv")
f2 = open("everyminutestatsdata.tsv")

#creates two readers for parallel line iteration
reader1 = csv.reader(f1, delimiter='\t')
reader2 = csv.reader(f2, delimiter='\t')
first_row = next(reader2)
startingTime = first_row[0]	#starts one reader one line ahead

#creates a new list containing nextLine - prevLine (for total requests per each minute)
newList = []
for row1, row2 in itertools.izip(reader1, reader2):
	row1 = map(int, row1)
	row2 = map(int, row2)
	newList.append([b - a for a, b in zip(row1, row2)])

#corrects the time and finds rps from rpm
timeOfLogFromStartingTime = 0 
for row in newList:
	row[0] = timeOfLogFromStartingTime
	timeOfLogFromStartingTime = timeOfLogFromStartingTime + 60
	row[1] = row[1] / 60
	row[2] = row[2] / 60
	row[3] = row[3] / 60

#creates temp csv for ploting
plotfile = open('plotdata.csv', 'w+')
for rowl in newList:
	recordToAdd = str(rowl[0]) + "," + str(rowl[1]) + "," + str(rowl[2]) + "," + str(rowl[3]) + "\n"
	plotfile.write(recordToAdd)










