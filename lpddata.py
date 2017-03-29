import requests, sqlite3
from subprocess import call
url = "https://opendata.arcgis.com/datasets/b7d2a21a15f8427db62cfd09f821856a_0.csv"
r = requests.get(url)
data = r.text
with open('incidents_download.csv', 'w+') as f:
    f.write(data)
    f.close()
conn = sqlite3.connect('LPDIncidents.sqlite')
c = conn.cursor()
c.executescript("DROP TABLE IF EXISTS incidents")
c.close()
conn.close()
call(["csvsql", "-d", ",", "--db", "sqlite:///LPDIncidents.sqlite", "--table", "incidents", "--insert", "incidents_download.csv"])
