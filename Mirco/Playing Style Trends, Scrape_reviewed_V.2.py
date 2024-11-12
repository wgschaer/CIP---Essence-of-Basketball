from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os

# Initialize Selenium WebDriver (Chrome) with your custom filepath
driver_path = "/Users/mircoschar/Desktop/chromedriver-mac-arm64/chromedriver"  # Your custom ChromeDriver path
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Create the 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# List of seasons to scrape
seasons = [f"{year}-{str(year + 1)[-2:]}" for year in range(2004, 2024)]
# List of positions to scrape
positions = ["G", "F", "C"]  # Guards, Forwards, Centers

# Loop through each season and position to scrape data
for season in seasons:
    for position in positions:
        try:
            # Open the NBA stats page for the current season and position
            url = f"https://www.nba.com/stats/players/traditional?Season={season}&PlayerPosition={position}"
            driver.get(url)

            # Wait for the drop-down elements to load
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "DropDown_select__4pIg9")))

            # Locate the Page drop-down elements
            dropdowns = driver.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")
            select_page = Select(dropdowns[-1])

            # Attempt to select the "All" option
            try:
                select_page.select_by_visible_text("All")
                print(f"'All' option successfully selected for the {season} season and {position} position.")
            except Exception as e:
                print(f"Failed to select 'All' option for the {season} season and {position} position: {e}")
                # Implement pagination logic if "All" is not available
                try:
                    # Loop through pages if pagination is required
                    page_number = 1
                    while True:
                        print(f"Scraping page {page_number} for the {season} season and {position} position.")
                        # Wait for the table to load on each page
                        WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti')))

                        # Parse and extract data
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        table = soup.find('div', class_='Crom_container__C45Ti').find('table')
                        headers = [th.text.strip() for th in table.find_all('th')]
                        rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]]

                        # Save data from each page
                        if rows:
                            if len(rows[0]) != len(headers):
                                headers = headers[:len(rows[0])]  # Adjust headers to match row data
                            season_data = pd.DataFrame(rows, columns=headers)
                            season_data.to_csv(f"data/nba_player_stats_{season}_{position}_page_{page_number}.csv",
                                               index=False, mode='a', header=not os.path.exists(
                                    f"data/nba_player_stats_{season}_{position}.csv"))

                        # Check if there is a next page button and click it
                        next_buttons = driver.find_elements(By.CLASS_NAME,
                                                            'pagination__next')  # Update with the correct class name for the next button
                        if next_buttons and next_buttons[0].is_displayed():
                            next_buttons[0].click()
                            page_number += 1
                        else:
                            break
                except Exception as pagination_error:
                    print(f"Pagination failed for the {season} season and {position} position: {pagination_error}")
                continue

            # Wait for the table to load
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti')))

            # Parse the page content
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('div', class_='Crom_container__C45Ti').find('table')

            # Extract headers and rows
            headers = [th.text.strip() for th in table.find_all('th')]
            rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]]

            # Check if headers and row lengths match
            if rows and len(rows[0]) != len(headers):
                print(
                    f"Column mismatch for the {season} season and {position} position. Adjusting headers to match rows.")
                headers = headers[:len(rows[0])]  # Adjust headers to match the number of columns in rows

            # Convert to DataFrame and save to a CSV file for the current season and position
            season_data = pd.DataFrame(rows, columns=headers)
            season_file_path = f"data/nba_player_stats_{season}_{position}.csv"
            season_data.to_csv(season_file_path, index=False)
            print(f"Scraped and saved data for the {season} season and {position} position to {season_file_path}.")

        except Exception as e:
            print(f"Failed to scrape data for the {season} season and {position} position: {e}")

# Combine all CSV files into one
all_data = pd.DataFrame()
for season in seasons:
    for position in positions:
        season_file_path = f"data/nba_player_stats_{season}_{position}.csv"
        if os.path.exists(season_file_path):
            season_data = pd.read_csv(season_file_path)
            all_data = pd.concat([all_data, season_data], ignore_index=True)

# Save the combined data to a single CSV file
combined_file_path = 'data/nba_player_stats_combined_2004_2024.csv'
all_data.to_csv(combined_file_path, index=False)
print(f"All data combined and saved to {combined_file_path}.")

# Close the browser
driver.quit()
