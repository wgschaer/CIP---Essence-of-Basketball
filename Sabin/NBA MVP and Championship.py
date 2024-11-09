#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Step 1: Set up Selenium WebDriver (replace with your ChromeDriver path)
# Selenium is used to control the browser for interacting with dynamic content
driver_path = "C:/Users/School/Downloads/Compressed/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# Create the 'data' folder if it doesn't exist
# This is where the CSV files will be saved
if not os.path.exists('data'):
    os.makedirs('data')

# Function to wait for an element to appear using Selenium
def wait_for_element(by, value, timeout=10):
    """
    Wait for an element to appear on the page.
    Used for handling dynamic content with Selenium.
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# Function to extract NBA MVP data
def extract_mvp_data():
    print("Extracting MVP data...")

    # Use Selenium to open the main Basketball Reference website
    driver.get("https://www.basketball-reference.com/")

    # Use Selenium to interact with the search bar and search for "NBA MVP"
    search_input = wait_for_element(By.CSS_SELECTOR, "input[name='search']")
    search_input.clear()  # Clear any pre-filled text
    search_input.send_keys("NBA MVP")
    search_input.send_keys(Keys.RETURN)  # Simulate pressing Enter

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Use BeautifulSoup to parse the HTML content after page is fully loaded
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Locate the MVP table using BeautifulSoup
    mvp_table = soup.find('table', {'id': 'mvp_NBA'})
    headers = ['Season', 'Lg', 'Player', 'Voting', 'Age', 'Tm', 'G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS', 'WS/48']
    rows = mvp_table.find('tbody').find_all('tr')

    # Extract data from the MVP table rows
    mvp_data = []
    for row in rows:
        columns = row.find_all(['th', 'td'])
        if len(columns) == len(headers):
            mvp_data.append([col.getText() for col in columns])

    # Filter the data for the years between 1999 and 2024
    filtered_mvp_data = [row for row in mvp_data if '1999' <= row[0] <= '2024']
    mvp_df = pd.DataFrame(filtered_mvp_data, columns=headers)

    # Save the extracted data to a CSV file
    mvp_df.to_csv('data/nba_mvp_data_1999_2024.csv', index=False)
    print("MVP data saved to 'data/nba_mvp_data_1999_2024.csv'")
    print(mvp_df.head())


# Function to extract NBA Playoffs data
def extract_playoffs_data():
    print()
    print("Extracting Playoffs data...")

    # Use Selenium to open the main Basketball Reference website
    driver.get("https://www.basketball-reference.com/")

    # Use Selenium to interact with the search bar and search for "NBA Playoffs"
    search_input = wait_for_element(By.CSS_SELECTOR, "input[name='search']")
    search_input.clear()
    search_input.send_keys("NBA Playoffs")
    search_input.send_keys(Keys.RETURN)

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Use BeautifulSoup to parse the HTML content after page is fully loaded
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Locate the Playoffs table using BeautifulSoup
    table = soup.find("table", {"id": "champions_index"})
    table_body = table.find("tbody")
    rows = table_body.find_all("tr", {"data-row": True})

    # Extract data from the Playoffs table rows
    playoff_data = []
    for row in rows:
        year_tag = row.find("th", {"data-stat": "year_id"})
        league_tag = row.find("td", {"data-stat": "lg_id"})
        champion_tag = row.find("td", {"data-stat": "champion"})
        runnerup_tag = row.find("td", {"data-stat": "runnerup"})
        finals_mvp_tag = row.find("td", {"data-stat": "mvp_finals"})
        points_leader_tag = row.find("td", {"data-stat": "pts_leader_name"})
        rebounds_leader_tag = row.find("td", {"data-stat": "trb_leader_name"})
        assists_leader_tag = row.find("td", {"data-stat": "ast_leader_name"})
        win_shares_leader_tag = row.find("td", {"data-stat": "ws_leader_name"})

        if year_tag and league_tag and champion_tag:
            playoff_data.append({
                "Year": year_tag.get_text(),
                "League": league_tag.get_text(),
                "Champion": champion_tag.get_text(),
                "Runner-Up": runnerup_tag.get_text() if runnerup_tag else "",
                "Finals MVP": finals_mvp_tag.get_text() if finals_mvp_tag else "",
                "Points Leader": points_leader_tag.get_text() if points_leader_tag else "",
                "Rebounds Leader": rebounds_leader_tag.get_text() if rebounds_leader_tag else "",
                "Assists Leader": assists_leader_tag.get_text() if assists_leader_tag else "",
                "Win Shares Leader": win_shares_leader_tag.get_text() if win_shares_leader_tag else ""
            })

    # Filter the data for the years between 1999 and 2024
    filtered_playoff_data = [row for row in playoff_data if '1999' <= row["Year"] <= '2024']
    playoff_df = pd.DataFrame(filtered_playoff_data)

    # Save the extracted data to a CSV file
    playoff_df.to_csv('data/nba_champions_1999_2024.csv', index=False)
    print("Playoffs data saved to 'data/nba_champions_1999_2024.csv'")
    print(playoff_df.head())


# Main script to run both extraction functions
try:
    extract_mvp_data()  # Extract NBA MVP data using Selenium and BeautifulSoup
    extract_playoffs_data()  # Extract NBA Playoffs data using Selenium and BeautifulSoup
finally:
    driver.quit()  # Close the browser when done
    print("Browser closed")
