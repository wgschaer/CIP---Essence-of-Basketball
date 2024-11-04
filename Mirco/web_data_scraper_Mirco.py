from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Initialize Selenium WebDriver for Safari
driver = webdriver.Safari()

# Open the base URL for NBA team stats
url = 'https://www.nba.com/stats/teams/traditional'
driver.get(url)

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# List to store all seasons' data
all_data = []

# Wait for the season drop-down to be clickable and locate the Season drop-down element by class name
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "DropDown_select__4pIg9"))
)
season_dropdown = driver.find_element(By.CLASS_NAME, "DropDown_select__4pIg9")
select_season = Select(season_dropdown)

# Wait for the season type drop-down and locate the Season Type drop-down element
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "DropDown_select__4pIg9"))
)
season_type_dropdown = driver.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")[1]  # The second drop-down is
# for Season Type
select_season_type = Select(season_type_dropdown)

# Define the range of seasons to scrape
target_seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2003, 2024)]

# Loop over each option (season) in the drop-down
for option in select_season.options:
    season_str = option.text.strip()

    # Only select seasons between 2003-04 and 2023-24
    if season_str not in target_seasons:
        continue

    print(f"Scraping data for the {season_str} season...")

    # Select the season from the drop-down
    select_season.select_by_visible_text(season_str)

    # Select "Regular Season" from the Season Type drop-down
    select_season_type.select_by_visible_text("Regular Season")

    # Wait for the table to load for the new season
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti'))
    )

    # Get the page source after loading the selected season's data
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

    # Wait a little between requests to avoid overloading the server
    time.sleep(3)

# After the loop, combine all data into one DataFrame and save it to a single CSV file
all_headers = headers + ['Season']
all_seasons_data = pd.DataFrame(all_data, columns=all_headers)
all_seasons_data.to_csv('data/nba_team_stats_2003_2024.csv', index=False)

print("All data from 2003-04 to 2023-24 seasons has been successfully combined and saved to "
      "'data/nba_team_stats_2003_2024.csv'.")

# Close the browser
driver.quit()

print("Scraping complete.")
