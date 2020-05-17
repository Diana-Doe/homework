## Project name: SmartHome analysis
[My site](https://deersmarthome.herokuapp.com/)
The site from which I take data -- [SmartHome](https://www.smarthomedb.com/products).
## Description
The program takes data from the [web-site](https://www.smarthomedb.com/products, 'SmartHome'), stores them in ADT and builds graphs.
<br>Site is built with dash with bootstrap components.
<br>
![image](https://user-images.githubusercontent.com/54356826/82119593-8327ee00-9788-11ea-83b6-bf75ec610d3e.png)
<br>
![image](https://user-images.githubusercontent.com/54356826/82119626-c1bda880-9788-11ea-9d85-93b969798125.png)
<br>
<br>Since the site from which I take information is not large I do not use a web spider.
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
- For scraping and storing data you do not need any additional libraries. But you need to install three libraries for visualisation.
```python
pip install plotly
pip install dash
pip install dash-bootstrap-components 
```
- Run `scraping.py` from module directory to build database.
- Run `graph.py` from module directory to buid graphs and site.
## Usage

## Contributing
## Credits
Hromyak Diana, UCU
## License
