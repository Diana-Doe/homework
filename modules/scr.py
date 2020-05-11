"""
Example of scraping information from a website by using requests
and BeautifulSoup libraries.
Copyright (c) 2020 Diana Hromyak
"""
import requests
import re
import json
from bs4 import BeautifulSoup
from datetime import date

# Set base url of site and url of the first page.
base_url =  "https://www.smarthomedb.com"
URL = "https://www.smarthomedb.com/?page=1"

# Create or take from file(if it already exists) a dictionary with one key 
# 'data' which contains a dictionary with dates as keys and lists which 
# contains dictionaries for each product as values. Each of dictionaries 
# has a name of the product, its category and number of its buyers.
today = date.today()
today = today.strftime(str(today))
try:
    with open('data.json', 'r', encoding='utf-8') as ff:
        main_content = json.load(ff)
except:
    main_content = dict()
    main_content['data'] = dict()
finally:
    main_content['data'][today] = []

def parse(soup):
    '''
    bs4.BeautifulSoup -> None
    Parse page by using BeautifulSoup library. 
    Take items` names, number of customers, prices, categories, rates.
    Append them to main content.
    '''
    # Find names of product
    names = soup.find_all('div', attrs={'class': 'item-name'})
    names = [row.get_text() for row in names]

    # Find customers of product
    customers = soup.find_all('div', attrs={'class': 'item-user-own'})
    cust = [row.get_text().replace('\n','') for row in customers]

    # Find price of product
    price = soup.find_all('div', attrs={'class': 'price-box'})
    price = [row.get_text().replace('\n', '').replace('$', '').split('dif')[0] for row in price]

    # Find categories of product
    # It needs extra work because of some unnecessary information
    category_pattern = re.compile('[A-Z].*[^\s\s\s]')
    patt = re.compile('[A-Z].*[a-z](?=[A-Z])|[A-Z].*[A-Z][A-Z][\d]?(?=[A-Z])')
    categories = soup.find_all('div', attrs={'class': 'item-category'})
    # Extract only text
    cat = [row.get_text() for row in categories]
    category = []
    for categ in cat:
        # Get rid off information about ecosystem
        categ = categ.replace("Gateway / Hub: Open Ecosystem", ',').replace(
            "Gateway / Hub: Closed Ecosystem", ',').replace('...', '')
        temp = patt.findall(categ)
        categ = patt.sub('', categ)
        t = temp
        if len(temp) != 0:
            temp = temp[0]
            t = []
            while patt.sub('', temp) != temp:
                t.append(patt.sub('', temp))
                temp = patt.findall(temp)[0]
            t.append(temp)
        categ = categ.split(',')
        for i in categ:
            for j in category_pattern.findall(i):
                t.append(j)
        # Finale extract the desired information and add it to list
        category.append(t)

    # Find rate of product
    # It needs extra work because it is saved as style
    rates = []
    rate_pattern = re.compile('(?<=width:).*(?=%)')
    rate = soup.find_all('div', attrs={'class': 'fill'})[1:]
    for rat in rate:
        rates.append(rate_pattern.findall(str(rat))[0])

    global main_content
    global today
    for num, name in enumerate(names, start=0):
        content = {}
        content = {
            'name' : name,
            'category' : category[num],
            'price' : price[num],
            'customers' : cust[num],
            'rate': rates[num]
        }
        main_content['data'][today].append(content)

def page_parse(URL):
    '''
    str -> None
    Get data from the page by using library requests and parse it using BeautifulSoup.
    '''
    global base_url
    # Get content from the page and parse it by using
    # BeautifulSoup library
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    parse(soup)
    
    # find out if button "next" is on the page. 
    # If there is then change URL to URL of next page.
    next_page_text = soup.find('ul', attrs={'class': 'pagination'}).findAll('li')[-1].text
    if next_page_text == 'Next':
        next_page = soup.find('ul', attrs={'class': 'pagination'}).findAll('li')[-1].find('a')['href']
        next_page_url = base_url + next_page
        page_parse(next_page_url)

page_parse(URL)
# Create a JSON file and write extracted data into it.
with open('data.json', 'w', encoding='utf-8') as ff:
    json.dump(main_content, ff, ensure_ascii=False, indent=4)
