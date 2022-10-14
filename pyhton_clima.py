import csv
from turtle import clear
import requests
import gzip
import pymysql

bdsql = pymysql.connect(user='crawler', password='sptech', host='localhost', database='webcrawler')
cursor = bdsql.cursor()

CSV_URL="https://storage.googleapis.com/basedosdados-public/one-click-download/br_inmet_bdmep/estacao/data000000000000.csv.gz"

with requests.Session() as s:
    download = s.get(CSV_URL)
    with open('data000000000000.csv.gz', 'wb') as f:
        f.write(download.content)

f = gzip.open('data000000000000.csv.gz', 'rt')
file_content=f.read()

cr = csv.reader(file_content.splitlines(), delimiter=',')
my_list = list(cr)
my_list.remove(my_list[0])

for row in my_list:
    print(row)
    comando = f'INSERT INTO clima (id_municipio, id_estacao, estacao, data_fundacao, latitude, longitude, altitude) VALUES ({row[0]}, "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}");'

    cursor.execute(comando)
    bdsql.commit()