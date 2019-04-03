import pandas as pd

import csv


data = pd.read_csv('proxy.txt')
proxies=[]
for i in data['proxy']:
    proxies.append('http://'+i)

print(len(proxies))

proxies = list(set(proxies))
for pro in proxies:
    # print(pro)
    with open('list.txt','a',newline='') as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow([pro])



print(len(proxies))