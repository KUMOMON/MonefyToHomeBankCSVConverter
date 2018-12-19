# importing csv module
import csv

# csv file name
filename = 'testfile.csv'

# initializing the titles and rows list
fields = []
rows = []

with open(filename, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';' )
    """for row in csvreader:
        print(', '.join(row))"""

    # extracting field names through first row
    fields = csvreader.__next__()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    pass