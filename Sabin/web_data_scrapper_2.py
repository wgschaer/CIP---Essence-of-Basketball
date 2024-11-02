import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the MVP page
url = 'https://www.basketball-reference.com/awards/awards_2024.html'

# Send a request to the website
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the MVP table
mvp_table = soup.find('table', {'id': 'mvp'})

# Extract the headers
headers = [th.getText() for th in mvp_table.find_all('th')]

# Extract the data rows
rows = mvp_table.find_all('tr')
mvp_data = []

for row in rows:
    columns = row.find_all('td')
    if columns:
        mvp_data.append([column.getText() for column in columns])

# Convert to a DataFrame
mvp_df = pd.DataFrame(mvp_data, columns=headers[1:])

# Display the first few rows
print(mvp_df.head())

# Save the data to a CSV file
mvp_df.to_csv('nba_mvp_2024_data.csv', index=False)

print("Data saved successfully!")

