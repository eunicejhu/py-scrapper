import requests
from bs4 import BeautifulSoup
import sys
import os

URL = "https://fr.le360.ma/"

# find all the links

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# output into a file
if os.path.exists("360_result.md"):
    os.remove("360_result.md")

f = open("360_result.md", "x")

nav_links = soup.find(id="header").find_all("a")
f.write("# nav links \n")
for a in nav_links:
    f.write("- "+ a.text)
    f.write(" url: " + a.get("href") + "\n")

footer_links = soup.find(id="footer").find_all("a")
f.write("# footer links \n")
for a in footer_links:
    f.write("- "+ a.text)
    f.write(" url: " + a.get("href") + "\n")

f.close()