import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

# Set up the Firefox WebDriver
geckodriver_path = "/Users/mircoschar/Desktop/geckodriver"  # Change this to the path where your geckodriver is located
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

try:
    # Open the NBA stats page
    driver.get("https://www.nba.com/stats/players/traditional")

    # Wait for the "Position" dropdown to be present in the DOM
    wait = WebDriverWait(driver, 15)
    position_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Position']")))

    # Select "Forward" from the "Position" dropdown
    select_position = Select(position_dropdown)
    select_position.select_by_visible_text("Forward")

    # Wait for the "Team" dropdown to be present
    team_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Team']")))
    select_team = Select(team_dropdown)
    select_team.select_by_visible_text("All Teams")

    # Wait for the table to be loaded
    time.sleep(5)

    # Scrape the data from the table
    table = driver.find_element(By.XPATH, "//table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Prepare data for CSV output
    data_list = []

    # Loop through rows and extract data
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        data = [cell.text for cell in cells]
        if data:  # Only include rows with data
            data_list.append(data)

    # Define the CSV file path (including the file name)
    csv_file_path = "/Users/mircoschar/Library/CloudStorage/OneDrive-HochschuleLuzern/CIP - Essence-of-Basketball/CIP---Essence-of-Basketball/Mirco/data/"

    # Write the data to a CSV file
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write the header (you can customize it if needed)
        header = ["Rank", "Player", "Team", "GP", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "TOV", "STL", "BLK", "PF", "PLUS_MINUS"]
        writer.writerow(header)
        # Write the data rows
        writer.writerows(data_list)

    print(f"Data has been successfully saved to {csv_file_path}")

except TimeoutException as e:
    print("TimeoutException: The element was not found within the given time.")
    print(driver.page_source)  # Print the page source for debugging

finally:
    # Close the browser
    driver.quit()

