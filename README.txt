Files: 

collector.sh- logs total current requests to server in the statsdata.tsv file. Must use --interval flag to specify intervals of collection. Interval must be a positive, in seconds, and an integer below 60

statsdata.tsv- stores server request info with attributes time of collection, total 200 requests, total 404 requests, and total 500 requests

trafficgen.py- generates requests to the server. Arguments must be url, rps, and jitter. Verifies that rps is between 1-500 and jitter is between 0-1

timeserver- server

plot.sh- is executed to produce plot of rps from collected data in statsdata.tsv

plotHelper.py- is a helper to plot.sh for making rps calculations

sitePloter.gnuplot- gnu commands for plotting data from temp csv after calculations are made


