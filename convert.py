import csv

filename = 'testfile.csv'

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=" ", quotechar=';')
    for row in csvreader:
        print(', '.join(row))