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
url = 'https://www.basketball-reference.com/playoffs/'
driver.get(url)

# Wait for the page to fully load
time.sleep(3)

# Get the page source and close the browser
html = driver.page_source
driver.quit()

# In[37]:


# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# In[38]
# Locate the specific table by its ID
table = soup.find("table", {"id": "champions_index"}) # Adjust the ID based on the table you inspected
print(table)


# In[38]
# Locate tbody containing the rows
table_body = table.find("tbody")

# Step 3: Extract all rows with the `data-row` attribute
rows = table_body.find_all("tr", {"data-row": True})

print("Total rows found:", len(rows))
if len(rows) > 0:
    print("Sample row structure:", rows[0])  # Print the first row as a sample
else:
    print("No rows found.")


# In[39]

# Initialize a list to store row data
playoff_data = []

# Loop through each row to extract data
for row in rows:
    # Check if the required elements are present in the row
    year_tag = row.find("th", {"data-stat": "year_id"})
    league_tag = row.find("td", {"data-stat": "lg_id"})
    champion_tag = row.find("td", {"data-stat": "champion"})
    runnerup_tag = row.find("td", {"data-stat": "runnerup"})
    finals_mvp_tag = row.find("td", {"data-stat": "mvp_finals"})
    points_leader_tag = row.find("td", {"data-stat": "pts_leader_name"})
    rebounds_leader_tag = row.find("td", {"data-stat": "trb_leader_name"})
    assists_leader_tag = row.find("td", {"data-stat": "ast_leader_name"})
    win_shares_leader_tag = row.find("td", {"data-stat": "ws_leader_name"})

    # Only proceed if all tags are found
    if year_tag and league_tag and champion_tag and runnerup_tag and finals_mvp_tag and points_leader_tag and rebounds_leader_tag and assists_leader_tag and win_shares_leader_tag:
        year = year_tag.get_text()
        league = league_tag.get_text()
        champion = champion_tag.get_text()
        runnerup = runnerup_tag.get_text()
        finals_mvp = finals_mvp_tag.get_text()
        points_leader = points_leader_tag.get_text()
        rebounds_leader = rebounds_leader_tag.get_text()
        assists_leader = assists_leader_tag.get_text()
        win_shares_leader = win_shares_leader_tag.get_text()

        # Append row data to list
        playoff_data.append({
            "Year": year,
            "League": league,
            "Champion": champion,
            "Runner-Up": runnerup,
            "Finals MVP": finals_mvp,
            "Points Leader": points_leader,
            "Rebounds Leader": rebounds_leader,
            "Assists Leader": assists_leader,
            "Win Shares Leader": win_shares_leader
        })

# Convert to DataFrame to check results
import pandas as pd

playoff_df = pd.DataFrame(playoff_data)

# Display the first few rows
print(playoff_df.head())


# Filter the data from 1999 to 2024
filtered_playoff_data = [row for row in playoff_data if 1999 <= int(row["Year"]) <= 2024]

# Convert the filtered data to a DataFrame
filtered_playoff_df = pd.DataFrame(filtered_playoff_data)

# Save the DataFrame to a CSV file
filtered_playoff_df.to_csv("nba_champions_1999_2024.csv", index=False)

print("Data saved to nba_champions_1999_2024.csv")
