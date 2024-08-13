import csv 
with open('purchase_data_1.xlsx') as csv_file:
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        print(row)