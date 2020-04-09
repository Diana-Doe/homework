"""
!!! Requires Chrome webdriver !!!
Example of scraping information from a website by using selenium
and BeautifulSoup libraries.
Copyright (c) 2020 Diana Hromyak
 """
import re
import json
from bs4 import BeautifulSoup
from selenium import webdriver


# First of all we need to configure webdriver to use Chrome
# here you need to set your path to chromedriver
driver = webdriver.Chrome(r"\webdrivers\chromedriver")
driver.get("https://www.smarthomedb.com/")

# Get content from the page and parse it by using
# BeautifulSoup library
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()



# Find names of product
names = soup.find_all('div', attrs={'class': 'item-name'})
names = [row.get_text() for row in names]

# Find customers of product
customers = soup.find_all('div', attrs={'class': 'activatedCount withover'})
cust = [row.get_text() for row in customers]

# Find price of product
price = soup.find_all('span', attrs={'class': 'fancyButton clickOut'})
price = [row.get_text() for row in price]

# Find categories of product
# It needs extra work because of some unnecessary information
category_pattern = re.compile('[A-Z](?:\\S|\\s(?!\\s))*')
categories = soup.find_all('div', attrs={'class': 'item-category'})
# Extract only text
cat = [row.get_text() for row in categories]
category = []
for categ in cat:
    # Get rid off information about ecosystem
    categ = categ.replace("Gateway / Hub: Open Ecosystem", '   ').replace(
        "Gateway / Hub: Closed Ecosystem", '   ')

    # Finale extract the desired information and add it to list
    category.append(category_pattern.findall(categ))
<<<<<<< HEAD

# Find rate of product
# It needs extra work because it is saved as style
rates = []
rate_pattern = re.compile('(?<=width:).*(?=%)')
rate = soup.find_all('div', attrs={'class': 'fill'})[1:]
for rat in rate:
    rates.append(rate_pattern.findall(str(rat))[0])
=======
>>>>>>> 3b159eef9015d9a92ffce54a8cd8e3cecec0636c

# Create a dictionary which contains a list which contains dictionaries
# for each product. Each of dictionaries has a name of the product,
# its category and number of its buyers as keys.
main_content = dict()
main_content['data'] = []
for num, name in enumerate(names, start=0):
    content = {}
    content = {
        'name' : name,
        'category' : category[num],
        'price' : price[num],
        'customers' : cust[num],
        'rate': rates[num]
    }
    main_content['data'].append(content)

# Create a JSON file and write extracted data into it.
with open('information.json', 'w', encoding='utf-8') as ff:
    json.dump(main_content, ff, ensure_ascii=False, indent=4)
