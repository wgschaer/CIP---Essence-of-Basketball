# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time


# Set up the Selenium WebDriverdriver_path = "C:/Users/School/Downloads/Compressed/chromedriver-win64/chromedriver.exe"# change path as needed
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service) (replace 'path/to/chromedriver' with your actual path)
driver_path = "C:/Users/School/Downloads/Compressed/chromedriver-win64/chromedriver.exe"# change path as needed
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


# Step 2: Open the page using Selenium
url = 'https://www.basketball-reference.com/awards/awards_2024.html'
driver.get(url)

# Step 3: Wait for the page to fully load
time.sleep(3)

# Step 4: Get the page source and close the browser
html = driver.page_source
driver.quit()

# Step 5: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 6: Find the MVP table
mvp_table = soup.find('table', {'id': 'mvp'})

# Step 7: Extract headers (Skipping irrelevant headers)
headers_row = mvp_table.find_all('tr')[1]  # Skipping higher-level headers
headers = [th.getText() for th in headers_row.find_all('th')]


#Remove the 'Rank' header to match the data columns
headers = headers[1:]

# Step 8: Extract the data rows (Skipping the 'Rank' column in the data)
rows = mvp_table.find_all('tr')[2:]  # Skip the first two rows

mvp_data = []
for row in rows:
    columns = row.find_all('td')
    if columns:  # Only extract rows that have actual data
        mvp_data.append([column.getText() for column in columns])

# Step 9: Create a DataFrame with the correct number of columns (19 columns)
mvp_df = pd.DataFrame(mvp_data, columns=headers)

# Step 10: Display the first few rows to verify the data
print(mvp_df.head())

# Step 11: Save the DataFrame to a CSV file
mvp_df.to_csv('nba_mvp_2024_data.csv', index=False)

print("Data saved to nba_mvp_2024_data.csv")



