# importing csv module
import csv
from datetime import datetime

# csv file name
filename = 'testfile.csv'

# initializing the titles and rows list
fields = []
rows = []


# read data from input csv
with open(filename, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    """for row in csvreader:
        print(', '.join(row))"""

    # extracting field names through first row
    fields = csvreader.__next__()

    # extracting each data row one by one
    for row in csvreader:
        # tmp = row;
        rows.append([datetime.strptime(row[0],'%d/%m/%Y').strftime('%d-%m-%Y'),'0',row[7],row[1],"",row[3],row[2]])
    pass