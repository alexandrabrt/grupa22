import csv

new_cars = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]
with open('data_csv.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for new_car in new_cars:
        csv_writer.writerow(new_car)


def csv_reader():
    with open('data_csv.csv', 'r') as csv_file1:
        rows = csv.reader(csv_file1, delimiter=',')
        for row in rows:
            print(row)


csv_reader()
