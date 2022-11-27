import csv

def zaladuj(file_name):
    zaladuj.rows = []
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        zaladuj.header = next(csvreader)
        for row in csvreader:
            zaladuj.rows.append(row)

    kol = []
    for i in range(len(zaladuj.header) - 1):
        k = []
        for j in range(len(zaladuj.rows)):
            k.append(float(zaladuj.rows[j][i]))
        kol.append(k)
    return kol


