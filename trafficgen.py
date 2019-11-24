#!/usr/bin/python

import sys
import time
import random
import urllib2
#import subprocess		#used if request should be made as subprocces with curl 

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

#validates jitter and rps arguments
if jitter > 1 or jitter < 0:
	print "jitter must be between the values of 0 and 1"
	sys.exit()

if rps > 500 or rps < 0:
	print "rps value must be between the values of 0 and 500"
	sys.exit()

#gets the average time to execute a request (based on 500 sequential requests) 
#for calculating the actual rps
startTime = time.time()
for i in xrange(500):
	try:
   		urllib2.urlopen(url)
	except urllib2.HTTPError as err:
   		if err.code == 404:
       			continue
   		elif err.code == 500:
       			continue
endTime = time.time()
averageTimeToExecuteEachRequest = (endTime - startTime) / 500

#if the maximum number of requests per second is greater than what the system can handle, exit
if (averageTimeToExecuteEachRequest * (rps * ((1.0 + jitter) ** 4))) > 1:
	print "system can not handle desired requests per second"	
	sys.exit()

#until program is terminated by user with ctl c, random amount of requests are made
#with desired rps 
while True:
 	numberOfRequestsPerSecond = random.randint(int(rps * (1.0 - jitter)), int(rps * ((1.0 + jitter) ** 4)))
 	startTime = time.time()
 	for i in xrange(numberOfRequestsPerSecond):
		try:
   			urllib2.urlopen(url)
		except urllib2.HTTPError as err:
   			if err.code == 404:
       				continue
   			elif err.code == 500:
       				continue 
	endTime = time.time()
	if endTime - startTime < 1:
		time.sleep(1 - (endTime - startTime))

