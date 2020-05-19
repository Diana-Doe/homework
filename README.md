## Project name: SmartHome analysis
### [My site](https://deersmarthome.herokuapp.com/) (Try to reload if it doesn't work)
The site from which I take data -- [SmartHome](https://www.smarthomedb.com/products).
[Video](https://drive.google.com/file/d/1h1sezj9qaymjf_Xt854Bb71HjkNWI5Jb/view?usp=sharing)
## Description
The program takes data from the [web-site](https://www.smarthomedb.com/products, 'SmartHome') by using the requests library. Then it parses it by using BeautifulSoup and re libraries. And it saves collected data as JSON file.
<br>How It saves data from the site(keys&values).
![customers](https://user-images.githubusercontent.com/54356826/82263954-a7dcbb00-996c-11ea-80b5-f1000ad859f4.png)
####
Then the program gets data from the JSON file and rewrites it as ADT.
<br>Structure of ADT:
####
![Untitled Diagram](https://user-images.githubusercontent.com/54356826/81616636-86b81f80-93ec-11ea-9175-8158f2a044f7.jpg)
####
Then it creates graphs by using Plotly and site by using dash with bootstrap components. 
####
![image](https://user-images.githubusercontent.com/54356826/82119593-8327ee00-9788-11ea-83b6-bf75ec610d3e.png)
####
![image](https://user-images.githubusercontent.com/54356826/82119626-c1bda880-9788-11ea-9d85-93b969798125.png)
Program builds 7 graphs: 
- *Date-Devices*
![image](https://user-images.githubusercontent.com/54356826/82265624-1e2eec80-9970-11ea-8a09-c022ed84508c.png)
- *Caregories*
![image](https://user-images.githubusercontent.com/54356826/82265652-2e46cc00-9970-11ea-8959-0a283e8e5a5c.png)
- *Date-Customers*
![image](https://user-images.githubusercontent.com/54356826/82265693-4585b980-9970-11ea-88b8-7848680938ae.png)
- *Rate-Price*
![image](https://user-images.githubusercontent.com/54356826/82265711-520a1200-9970-11ea-8fb9-727ce7685958.png)
- *Category-Price-Rate*
![image](https://user-images.githubusercontent.com/54356826/82265741-6c43f000-9970-11ea-9066-6136d6cde196.png)
- *Price-Customers*
![image](https://user-images.githubusercontent.com/54356826/82265782-84b40a80-9970-11ea-9411-2b840ec9d2d6.png)
- *Rate-Customers*
![image](https://user-images.githubusercontent.com/54356826/82265814-95fd1700-9970-11ea-8df9-a93a13a141a4.png)
#### Contents in Modules directory: 
- `scraping.py` - This is code for web-scraping. It collects data from site and writes it into JSON file. If there is an available JSON file in the same directory it updates it.
- `graph.py` - This is code for creating graphs and site. It contains the dash application layouts, logic for graphs. It works with ADT data.
- `dataADT.py` - This is auxiliary module, it is used in `graph.py`. It get data from JSON file and convert it into ADT.
- `LinkedList.py` - This is code which contains classes for the implementation of data structures (LinkedList, LinkedDict). It is used in `dataADT.py`.
<br>In examples directory you can test certain parts of the code. You do not need it for main program. Also, module `scraping.py` in examples directory requires Chrome webdriver.
## Table of Contents
> ### [Homework №0](https://github.com/Diana-Doe/homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-0)
> ### [Homework №1](https://github.com/Diana-Doe/homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-1)
> ### [Homework №2](https://github.com/Diana-Doe/homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-2)
> ### [Homework №3](https://github.com/Diana-Doe/homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-3)
> ### [Homework №4](https://github.com/Diana-Doe/homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-4)
## Installation
- Clone repo.
- Install all required libraries.
```python
pip install beautifulsoup4
pip install plotly
pip install dash
pip install dash-bootstrap-components 
```
- Run `scraping.py` from module directory to build database.
- Run `graph.py` from module directory to buid graphs and site.
## Usage
This program can be used for analysing information about smart homes, like price, amount of customers, rating, categories, number of devices, etc. So you will know how fast the number of devices on the market is increasing. Also, you will be aware of what devices are best and from which category they are. As a result, you definitely won't buy a raw device with a low rating. Moreover, you will be better in stock understanding.
<br>Also, it may be used for site analyze to know customers preferences and improve the site by adding more devices that customers prefer.
## Credits
Hromyak Diana, UCU
## License
[MIT License](https://github.com/Diana-Doe/homework/blob/master/LICENSE.md)
