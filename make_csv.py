import json
import csv

with open('customer.json') as json_file:
    data = json.load(json_file)
customer_data = data['customers']

for element in customer_data:
    if 'addresses' in element:
        del element['addresses']

with open('customer_new.json', 'w') as json_file:
    data = json.dump(data, json_file)

data_file = open('customer_file.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for item in customer_data:
    if count == 0:
        header = item.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(item.values())
data_file.close()


