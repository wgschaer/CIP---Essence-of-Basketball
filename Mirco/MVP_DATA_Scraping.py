import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the MVP awards page on Basketball Reference
url = 'https://www.basketball-reference.com/awards/mvp.html'

# Send an HTTP request to the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the MVP table
table = soup.find('table', {'id': 'mvp'})

# Extract data from the table
mvp_data = []
for row in table.find('tbody').find_all('tr'):
    if 'class' not in row.attrs:  # Avoid header rows
        year = row.find('th').text
        player = row.find('td', {'data-stat': 'player'}).text
        position = row.find('td', {'data-stat': 'pos'}).text
        team = row.find('td', {'data-stat': 'team_id'}).text

        mvp_data.append({
            'Year': year,
            'Player': player,
            'Position': position,
            'Team': team
        })

# Convert the data into a pandas DataFrame
df_mvp = pd.DataFrame(mvp_data)

# Save to CSV
df_mvp.to_csv('mvp_data.csv', index=False)

# Display the data
print(df_mvp.head())
