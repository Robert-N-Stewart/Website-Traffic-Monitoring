set datafile separator ","
set terminal png size 1800,800
set title "http://localhost.com Web Traffic"
set ylabel "Requests per second"
set xlabel "Time"
set xdata time
set timefmt "%s"
set key right top
set grid
plot "plotdata.csv" using 1:2 with lines lw 2 lt 3 title '200s', \
     "plotdata.csv" using 1:3 with lines lw 2 lt 1 title '404s', \
     "plotdata.csv" using 1:4 with lines lw 2 lt 2 title '500s'
