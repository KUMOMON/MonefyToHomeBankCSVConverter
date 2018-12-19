# importing csv module
import csv
from datetime import datetime

# csv file name
inputFileName = 'testfile.csv'
outputFileName = 'outfile.csv'
# initializing the titles and rows list
# fields = []
# read data from input csv

with open(inputFileName, mode='r', encoding='utf8') as csvfile:
    with open(outputFileName, mode='w',encoding='utf8', newline='') as f:
        csvreader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')


        # writer.writerow(["date", "paymode", "info", "payee", "description", "amount", "category"])

        # extracting field names through first row
        csvreader.__next__()
        # extracting each data row one by one
        for row in csvreader:
            writer.writerow([datetime.strptime(row[0],'%d/%m/%Y').strftime('%d-%m-%Y'),'0',row[7],row[1],"",row[3],row[2],""])
