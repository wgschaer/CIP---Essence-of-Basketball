import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd

# Set up the Firefox WebDriver
geckodriver_path = "/Users/mircoschar/Desktop/geckodriver"  # Update the path if needed
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

try:
    # Open the NBA stats page
    driver.get("https://www.nba.com/stats/players/traditional")

    # Save the page source to a file for analysis
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    print("Page source saved to page_source.html")

    # Increase wait time to ensure the page loads fully
    wait = WebDriverWait(driver, 60)  # 60-second timeout

    # Wait for the "Position" dropdown to be visible and interactable
    position_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Position']"))
    )
    # Select "Forward" from the "Position" dropdown
    select_position = Select(position_dropdown)
    select_position.select_by_visible_text("Forward")

    # Wait for the "Team" dropdown to be visible and interactable
    team_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Team']"))
    )
    select_team = Select(team_dropdown)
    select_team.select_by_visible_text("All Teams")

    # Wait for the table to be fully loaded
    table = wait.until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Extract rows from the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Prepare data for CSV output
    data_list = []

    # Loop through rows and extract only the relevant data
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 24:  # Ensure there are enough cells to extract
            player = cells[1].text  # Player name
            team = cells[2].text    # Team
            pts = cells[6].text     # Points (PTS)
            reb = cells[18].text    # Rebounds (REB)
            data = [player, team, pts, reb]
            data_list.append(data)

    # # Debugging Zeilen einfügen
    # print(f"Number of data rows collected: {len(data_list)}")
    # print(data_list[:5])  # Zeige die ersten 5 Datenzeilen an

    # Define the CSV file path
    csv_file_path = "data/nba_stats.csv"
    header = ["Player", "Team", "PTS", "REB"]
    df = pd.DataFrame(data_list, columns=header)

    # Save data for each season to the 'data' folder
    # team_data = pd.DataFrame(rows, columns=headers + ['Season'])
    df.to_csv(f'data/nba_stats.csv', index=False)

    # # Write the data to a CSV file
    # with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
    #     writer = csv.writer(csv_file)
    #     # Write the header for the relevant data
    #     header = ["Player", "Team", "PTS", "REB"]
    #     writer.writerow(header)
    #     # Write the data rows
    #     writer.writerows(data_list)

    print(f"Data has been successfully saved to {csv_file_path}")

except TimeoutException as e:
    print("TimeoutException: The element was not found within the given time.")
    print(driver.page_source)  # Print the page source for debugging

finally:
    # Close the browser
    driver.quit()
