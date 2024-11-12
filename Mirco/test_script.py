from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Firefox WebDriver
geckodriver_path = "/Users/mircoschar/Desktop/geckodriver"  # Make sure this path is correct
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

try:
    # Open the NBA stats page
    driver.get("https://www.nba.com/stats/players/traditional")

    # Wait for the main table to load
    wait = WebDriverWait(driver, 30)  # 30-second timeout
    table = wait.until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Extract and print the table headers as a sample
    headers = table.find_elements(By.TAG_NAME, "th")
    header_texts = [header.text for header in headers]
    print("Table headers:", header_texts)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
