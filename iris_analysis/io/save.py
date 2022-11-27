import csv

def save_result(results, result_file):
    with open(result_file, 'w') as file:
        writer = csv.writer(file)
        list = ['Median', 'Mean', 'Std']
        writer.writerow(list)
        writer.writerows(results)

