# This file was used to determine that the median frequency words had a frequency of 4 and less then 7.

import csv
import statistics

file = open("CleanedIsizuluCorpus.csv")
reader = csv.reader(file)
header = next(reader)

rows = []
for row in reader:
    rows.append(row)
file.close()

words = []
frequency = []

for i in range(len(rows)):
    temp = rows[i]
    words.append(temp[0])
    frequency.append(int(temp[1]))

words = words[:253902]
frequency = frequency[:253902]

print(statistics.median(frequency))
