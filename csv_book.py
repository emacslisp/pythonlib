import csv

file_to_output = open('1.csv', mode='w', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

data = open('1.csv', encoding="utf-8")

csv_data = csv.reader(data)
data_lines = list(csv_data)
print(len(data_lines))

for line in data_lines[:5]:
    print(line)