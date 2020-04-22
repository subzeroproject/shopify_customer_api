import json
import csv
import requests
import pandas as pd

import requests
link = requests.get("https://my-dev-shop-12.myshopify.com/admin/api/2020-04/customers.json", auth=('63250ac0afd68cccd81f5383228b83df', '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'))
r = link.json()
for element in r['customers']:
    if 'addresses' in element:
        del element['addresses']
data_file = open('customer_file.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
for item in r['customers']:
    if count == 0:
        header = item.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(item.values())
data_file.close()












