from bs4 import BeautifulSoup
import requests

url =" https://www.basketball-reference.com/awards/mvp.html"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

print(soup)

#soup.find("div")

soup.find_all("div")


