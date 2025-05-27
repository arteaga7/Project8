'''This script gets data from a web page and converts it into a pandas DataFrame.'''

# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')
tag = 'table'
id_tag = "weather_records"
table = soup.find(tag, attrs={"id": id_tag})

# Getting column names from table
col_names = []
for row in table.find_all('th'):
    col_names.append(row.text)

# Getting content from table
content = []
for row in table.find_all('tr'):
    if not row.find_all('th'):  # Excluing headers
        content.append([i.text for i in row.find_all('td')])

weather_records = pd.DataFrame(data=content, columns=col_names)
print(weather_records)
