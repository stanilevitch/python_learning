import csv
import numpy

ages = []
with open('csvfile/example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ages.append(int(row[2]))
m = numpy.median(ages)
print(m)

ages.sort()
print(ages[2])