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

# Open the NBA stats page
url = "https://www.nba.com/stats/players/traditional?Season=2004-05&PlayerPosition=F"
driver.get(url)

# Create the 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# List to store all scraped data
all_data = []

# Wait for the drop-down elements to load
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "DropDown_select__4pIg9")))

# Locate the Page drop-down elements
dropdowns = driver.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")
select_page = Select(dropdowns[-1])

# Select the season and "Regular Season" type
select_page.select_by_visible_text("All")

# Wait for the table to load
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'Crom_container__C45Ti')))

# Parse the page content
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('div', class_='Crom_container__C45Ti').find('table')

# Extract headers and rows
headers = [th.text.strip() for th in table.find_all('th')][:30]
rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]]

# Extend the all_data list with the current season data
all_data.extend(rows)
print(f"Scraped data for the 2004-05 season.")

# Convert to DataFrame and save to a single CSV file
combined_data = pd.DataFrame(all_data, columns=headers)
combined_data.to_csv('data/nba_player_stats_2004_2024.csv', index=False)


# Close the browser
driver.quit()
