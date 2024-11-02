#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# In[35]:


# Step 1: Set up Selenium WebDriver (replace with your ChromeDriver path)
driver_path = "C:/Users/School/Downloads/Compressed/chromedriver-win64/chromedriver.exe"  # change path as needed
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# In[36]:


# Step 2: Open the page using Selenium
url = 'https://www.basketball-reference.com/awards/mvp.html'
driver.get(url)

# Wait for the page to fully load
time.sleep(3)

# Get the page source and close the browser
html = driver.page_source
driver.quit()

# In[37]:


# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# In[38]:

# Step 5: Find the MVP table by its ID
mvp_table = soup.find('table', {'id': 'mvp_NBA'})
print(mvp_table)

# In[39]:

# Step 6: Manually define the headers since we already know them
headers = ['Season', 'Lg', 'Player', 'Voting', 'Age', 'Tm', 'G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%',
           'FT%', 'WS', 'WS/48']

# In[40]:


# Step 7: Extract rows from the table
rows = mvp_table.find('tbody').find_all('tr')

# Print the number of rows found
print(f"Total rows found: {len(rows)}")

# Print the first row structure (if any)
if len(rows) > 0:
    print("First row structure:", rows[0])

# In[41]:


mvp_data = []
for row in rows:
    # Extract <th> and <td> elements from each row
    columns = row.find_all(['th', 'td'])

    # Only append rows that match the number of headers
    if len(columns) == len(headers):
        mvp_data.append([col.getText() for col in columns])

# In[44]:


# Step 9: Filter rows for the years between 1999 and 2023
mvp_filtered_data = [row for row in mvp_data if '1999' <= row[0] <= '2024']

# In[45]:


# Step 10: Create the DataFrame and check the first few rows
mvp_df = pd.DataFrame(mvp_filtered_data, columns=headers)
print(mvp_df.head())

# In[47]:


# Step 11: Save the DataFrame to a CSV file
mvp_df.to_csv('nba_mvp_data_1999_2023.csv', index=False)

print("Data saved to nba_mvp_data_1999_2023.csv")

# In[ ]:




