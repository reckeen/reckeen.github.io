import sys
import csv
import time

time.sleep(1)
with open(sys.argv[1],'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar = '"')

    for row in reader:
        print(','.join(row[5:8]))

