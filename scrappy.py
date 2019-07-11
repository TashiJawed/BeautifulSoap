from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/Iris_flower_data_set').text

soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

table = soup.find('tbody')
# print(table.prettify())

headers = []

for head in table.find_all('th'):
	headers.append(head.text.encode("ascii"))

headers.pop()
headers.append('Species')

import csv

with open("irisdataset.csv", "w") as f:
	handler = csv.writer(f, delimiter = ",")
	handler.writerow(headers)


def insertRow(list):
	with open("irisdataset.csv", "a") as f:
		handler = csv.writer(f, delimiter = ",")
		handler.writerow(list)

print(headers)
table_data = []
for data in table.find_all('tr'):
	table_data = []
	for row in data.find_all('td'):
		rowData = row.text
		# print(row.text)
		table_data.append(rowData.encode("latin-1"))
	print(table_data)
	insertRow(table_data)
	



