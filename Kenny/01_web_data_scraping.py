# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import os

# Initialize Selenium WebDriver using context manager for better resource handling
driver_path = "C:/Tools/chromedriver-win64/chromedriver.exe"  # Update this path as needed
service = Service(executable_path=driver_path)

with webdriver.Chrome(service=service) as driver:
    # Open the base URL for NBA team stats
    url = 'https://www.nba.com/stats/teams/advanced'
    driver.get(url)

    # Create the 'data' folder if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # List to store all scraped data
    all_data = []

    # Wait for the drop-down elements to load
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "DropDown_select__4pIg9")))

    # Locate the Season and Season Type drop-down elements
    dropdowns = driver.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")
    select_season = Select(dropdowns[0])
    select_season_type = Select(dropdowns[1])

    # Define the range of seasons to scrape
    target_seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2004, 2024)]

    # Loop through each season
    for season_str in target_seasons:
        try:
            print(f"Scraping data for the {season_str} season...")

            # Select the season and "Regular Season" type
            select_season.select_by_visible_text(season_str)
            select_season_type.select_by_visible_text("Regular Season")

            # Wait for the table to load
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti')))

            # Parse the page content
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('div', class_='Crom_container__C45Ti').find('table')

            # Extract headers and rows
            headers = [th.text.strip() for th in table.find_all('th')][:21]
            rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]]

            # Append the season information
            for row in rows:
                row.append(season_str)

            # Extend the all_data list with current season data
            all_data.extend(rows)
            print(f"Successfully scraped data for the {season_str} season")

        except Exception as e:
            print(f"Error scraping data for the {season_str} season: {e}")
            continue

    # Convert to DataFrame and save to a single CSV file
    all_headers = headers + ['Season']
    combined_data = pd.DataFrame(all_data, columns=all_headers)
    combined_data.to_csv('data/nba_team_stats_2004_2024.csv', index=False)

    print("All data from 2004-05 to 2023-24 seasons has been successfully combined and saved to "
          "'data/nba_team_stats_2004_2024.csv'.")

print("Scraping complete.")
