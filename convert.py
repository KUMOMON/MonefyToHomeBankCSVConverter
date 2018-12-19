import csv

filename = ''

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=" ", quotechar=';')
    for row in csvreader:
        print(', '.join(row))