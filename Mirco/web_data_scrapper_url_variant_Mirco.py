# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Initialize Selenium WebDriver for Safari
service = Service("/usr/bin/safaridriver")
driver = webdriver.Safari(service=service)

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# List to store all seasons' data
all_data = []

# Loop over the past 20 seasons (2003-04 to 2023-24)
for year in range(2003, 2024):
    season_str = f"{year}-{str(year + 1)[-2:]}"
    print(f"Scraping data for the {season_str} season...")

    # URL for the NBA team stats for a given season (Regular Season)
    url = f'https://www.nba.com/stats/teams/traditional/?sort=W&dir=-1&Season={season_str}&SeasonType=Regular%20Season'

    # Open the webpage
    driver.get(url)

    try:
        # Wait for the table to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti'))
        )

        # Get the page source after loading all teams
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the correct table inside the div with class 'Crom_container__C45Ti'
        table = soup.find('div', class_='Crom_container__C45Ti').find('table')

        # Extract table headers (column names)
        headers = [th.text.strip() for th in table.find_all('th')]
        headers = headers[:28]  # Trim headers to match the actual number of columns

        # Extract rows from the table
        rows = []
        for row in table.find_all('tr')[1:]:  # Skipping the header row
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            rows.append(cols)

        # Add the season information to each row
        for row in rows:
            row.append(season_str)

        # Append data for this season to the all_data list
        all_data.extend(rows)

        print(f"Successfully scraped data for the {season_str} season")

        # Save data for each season to the 'data' folder
        team_data = pd.DataFrame(rows, columns=headers + ['Season'])
        team_data.to_csv(f'data/nba_team_stats_{season_str}.csv', index=False)

    except Exception as e:
        print(f"Error scraping {season_str}: {e}")

    # Wait a little between requests to avoid overloading the server
    time.sleep(3)

# After the loop, combine all data into one DataFrame and save it to a single CSV file
all_headers = headers + ['Season']
all_seasons_data = pd.DataFrame(all_data, columns=all_headers)
all_seasons_data.to_csv('data/nba_team_stats_2003_2024.csv', index=False)

# Close the browser
driver.quit()

print("Scraping complete.")
