import csv
from random import randint
file = open('C:/Users/Dell/Dropbox/PC/Desktop/COLLEGE/chatbot/venv/dataset.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)

for qno in range(0,5):
    index = randint(0,29)
    print(rows[index][0])
    rows.pop(index)


file.close()