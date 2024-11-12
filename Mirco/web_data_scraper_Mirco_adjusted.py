from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Set up the Selenium WebDriver for Safari
driver = webdriver.Safari()

# Open the NBA stats page
driver.get("https://www.nba.com/stats/players/traditional")

# # Wait for the page to load
# wait = WebDriverWait(driver, 10)
#
# # Example: Interact with the "Position" dropdown menu
# position_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Position']")))
# select_position = Select(position_dropdown)
# select_position.select_by_visible_text("Forward")  # Adjust to "Guard" or "Center" as needed
#
# # Example: Interact with the "Team" dropdown menu
# team_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Team']")))
# select_team = Select(team_dropdown)
# select_team.select_by_visible_text("All Teams")
#
# # Allow the page to update and load the filtered data
# time.sleep(5)
#
# # Scrape the data
# # Example: Find the table and extract data
# table = driver.find_element(By.XPATH, "//table")
# rows = table.find_elements(By.TAG_NAME, "tr")
#
# # Loop through rows and extract data
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     data = [cell.text for cell in cells]
#     print(data)
#
# # Close the browser
# driver.quit()
