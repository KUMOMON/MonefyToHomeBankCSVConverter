import csv

filename = 'testfile.csv'

with open(filename,encoding='utf8', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\n",quotechar=';')
    for row in csvreader:
        print(', '.join(row))