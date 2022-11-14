# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.redfin.ca/on/kitchener/filter/max-price=800k,viewport=43.62128:43.23932:-80.03155:-80.82325,walk-score=70'
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

import re
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = r'C:\Better_Home\Python/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.redfin.ca/on/guelph/filter/max-price=800k,mr=33:2996+33:3316+33:3472,walk-score=70')

text_only = driver.find_element(By.TAG_NAME, "body").text
# re.findall(pattern, text_only)

src1 = driver.page_source

prices = re.findall(r'\\\"price\\\":{\\\"value\\\":(\d*)', src1)
#prices = np.array(prices).astype(int)

addresses = re.findall(r'\\\"streetLine\\\":{\\\"value\\\":\\\"(.*?)\\\",', src1)
#addresses = np.array(addresses).astype(str)

property_types = re.findall(r'\\\"propertyType\\\":(\d*?)', src1) # Use dict to convert to sensible categories
#property_types = np.array(property_types).astype(int)

square_footage = re.findall(r'\\\"sqFt\\\":{\\\"value\\\":(\d+),', src1)
#square_footage = np.array(square_footage).astype(int)

price_per_sqft = re.findall(r'\\\"pricePerSqFt\\\":{\\\"value\\\":(\d*?),', src1)
#price_per_sqft = np.array(price_per_sqft).astype(int)

n_beds = re.findall(r'\\\"beds\\\":(\d*?),', src1)
#n_beds = np.array(n_beds).astype(int)

n_baths = re.findall(r'\\\"baths\\\":(\d+.\d*),', src1)
#n_baths = np.array(n_baths).astype(int)

city = re.findall(r'\\\"city\\\":\\\"(\D*?)\\\"', src1)
#city = np.array(city).astype(str)

zip_code = re.findall(r'\\\"zip\\\":\\\"(\w\w\w \w\w\w)\\\"', src1)
#zip_code = np.array(zip_code).astype(str)





print(src1)
# print(prices)
print()
print()
#print(f'Average price of all houses is {np.sum(prices) / np.size(prices)}')
print(len(prices))
print(len(addresses))
print(len(property_types))
print(len(square_footage))
print(len(price_per_sqft))
print(len(n_beds))
print(len(n_baths))
print(len(city))
print(len(zip_code))

print(n_baths)


# print(text_only)

# driver.quit()
# \"listingId\":123456789
# \"propertyId\":123456789
# \"propertyType\":123456789
# \"price\":123456789
# \"city\":123456789
# \"sqFt\":123456789
# \"streetLine\":123456789
