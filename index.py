import requests
from bs4 import BeautifulSoup

URL_PRODUCT_OWNER_PARIS_ENGLISH_WELCOME_TO_JUNGLE = "https://www.welcometothejungle.com/fr/jobs?groupBy=job&sortBy=mostRecent&query=product%20owner&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Blanguage%5D%5B%5D=en&aroundQuery=Paris%2C%20France&aroundLatLng=48.85718%2C2.34141&aroundRadius=20000"
page = requests.get(URL_PRODUCT_OWNER_PARIS_ENGLISH_WELCOME_TO_JUNGLE)

soup = BeautifulSoup(page.content, "html.parser")
job_counts  = soup.find("div", role_="listitem")

print(soup.text)

   