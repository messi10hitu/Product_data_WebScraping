import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = "https://www.westwingnow.de/moebel/"

# STEP 1. get the HTML.
r = requests.get(url, headers=headers)
html_content = r.content
# print(html_content)

# STEP 2. Parse the HTML.
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
# div = soup.select('div', class_="blockProductGrid__item qaBlockProductGrid__item")[0].get_text().strip()
# div = soup.select('div', attrs={"class": "blockProductGrid__item qaBlockProductGrid__item"})[0].get_text().strip()

price = []
for div in soup.find_all('div', attrs={"class": "blockProductGrid__item qaBlockProductGrid__item"}):
    details = div.div.article.a.p.text.strip()
    price.append(details)
print(price)

name = []
for p in soup.find_all('p', attrs={"class": "blockProduct__name qaBlockProduct__name"}):
    p = p.text.strip()
    name.append(p)
print(name)

brand = []
for p in soup.find_all('p', attrs={"class": "blockProduct__brand qaProductBrand qaBlockProduct__brand"}):
    p = p.text.strip()
    brand.append(p)
print(brand)

df1 = pd.DataFrame(price, columns=["PRICE"])  # dataframe is an excel sheet which we can use in the python
df1['NAME'] = pd.DataFrame(name)  # dataframe is an excel sheet which we can use in the python
df1['BRAND'] = pd.DataFrame(brand)  # dataframe is an excel sheet which we can use in the python
print(df1)
df1.to_csv("Products.csv")


# Make the dataframe and create the csv file
# df_bs = pd.DataFrame(brand,columns=['brand'])
# df_bs.set_index('brand',inplace=True)
# df_bs.to_csv('beautifulsoup4.csv')

# import glob
#
# path = r'C:\\Users\\hitesh\\PycharmProjects\\WebScrapping'  # use your path
#
# all_files = glob.glob(path + "/*.csv")
#
# li = []
#
# for filename in all_files:
#     df = pd.read_csv(filename, index_col=None, header=0)
#     li.append(df)
# print(li)
# frame = pd.concat(li, axis=1, ignore_index=False)
# frame.to_csv("output.csv", index=True)

