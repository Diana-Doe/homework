'''
Module with ADT class. 
'''
import json
from LinkedList import LinkedDict, LinkedList

class DataADT:
    '''Represents data'''
    def __init__(self):
        '''
        DataADT -> NoneType
        '''
        self.list = LinkedList()
        self.categories = LinkedList()
        self.dates = LinkedList()
        self.newest = ''
        self.highestprice = 0
        self.lowestprice = 10000

    def insert(self, data):
        '''
        DataADT, dict -> NoneType
        Take only specific data which you can get by using module for scraping.
        How parameter data should look :: {data} -> {date} -> [{device},..,{device}] 
        '''
        # in the first dictionary we have only one 
        data = data['data']
        # in second dictionary we have dates as keys and list with
        # items` dictionaries as values
        for date, data_list in data.items():
            # add date into LinkedList which contains only dates
            self.dates.add(date)
            # go through each device in the list
            for item in data_list:
                # create LinkedDictionary for each device
                newDict = LinkedDict()
                newDict.add(date, 'date')
                for param, value in item.items():
                    # as some devices can belong to several categories 
                    # - we create the LinkedList for categories
                    if param == 'category':
                        catList = LinkedList()
                        for i in value:
                            catList.add(i)
                            if i not in self.categories:
                                self.categories.add(i)
                        value = catList
                    # convert price into int
                    if param == 'price' and item['price'] != 'Pending':
                        value = int(item['price'].replace(',', '').replace(' ',''))
                        if value > self.highestprice:
                            self.highestprice = value
                        elif value < self.lowestprice:
                            self.lowestprice = value
                    # convert rate into int
                    if param == 'rate':
                        value = int(item['rate'].replace(',', ''))
                    # convert customers into int
                    if param == 'customers' and item['customers'] != "":
                        value = int(item['customers'].replace(',', '').replace(' ',''))
                    elif param == 'customers' and item['customers'] == "":
                        value = 0
                    newDict.add(value, param)
                # add created dictionary to main LinkedList
                self.list.add(newDict)
        # write the newest date
        self.newest = date

    def __len__(self):
        '''
        DataADT -> int
        Return length of DataADT
        '''
        return len(self.list)

    def date_count(self):
        '''
        DataADT -> LinkedDict()
        Counts the number of devices in each available date.
        Return linked dict whith date as key and number of devices
        as value.
        '''
        diction = LinkedDict()
        for item in self.list:
            if item['date'] in diction:
                diction[item['date']] = diction[item['date']] + 1
            else:
                diction.add(1, item['date'])
        return diction
    
    def date_count_avail(self):
        '''
        DataADT -> LinkedDict()
        Counts the number of available devices in each available date.
        Return linked dict whith date as key and number of available devices
        as value.
        '''
        diction = LinkedDict()
        for item in self.list:
            if item['price'] != 'Pending':
                if item['date'] in diction:
                    diction[item['date']] = diction[item['date']] + 1
                else:
                    diction.add(1, item['date'])
        return diction

    def date_customers(self):
        '''
        DataADT -> LinkedDict()
        Counts the number of available customers in each available date.
        Return linked dict whith date as key and number of customers
        as value.
        '''
        diction = LinkedDict()
        for item in self.list:
            if item['date'] in diction:
                diction[item['date']] = diction[item['date']] + item['customers']
            else:
                diction.add(item['customers'], item['date'])
        return diction

    def category_count(self,date=None):
        '''
        DataADT, str -> LinkedDict()
        Counts the number of devices in each category.
        Return linked dict with catogory as key and number of devices
        as value.
        If you don`t enter date it will return data about newest date.
        Date should look like: 2020-04-20
        '''
        if date is None:
            date = self.newest
        diction = LinkedDict()
        for item in self.list:
            for category in item['category']:
                if item['date'] == date:
                    if category in diction:
                        diction[category] = diction[category] + 1
                    else:
                        diction.add(1, category)
        return diction
    
    def category_count_avail(self, date=None):
        '''
        DataADT, str -> LinkedDict()
        Counts the number of available devices in each category.
        Return linked dict with catogory as key and number of available devices
        as value.
        If you don`t enter date it will return data about newest date.
        Date should look like: 2020-04-20
        '''
        if date is None:
            date = self.newest
        assert date in self.dates, "Not available date."
        diction = LinkedDict()
        for category in self.categories:
            diction.add(0, category)
        for item in self.list:
            if item['price'] != 'Pending' and item['date'] == date:
                for category in item['category']:
                    diction[category] = diction[category] + 1
        return diction

    def price_range(self, lowest, highest, date=None):
        '''
        DataADT, int, int -> LinkedDict()
        Take lowest and highest price and return all devices that are
        in range of these prices.  
        If you don`t enter date it will return data about newest date.
        Date should look like: 2020-04-20
        '''
        assert lowest <= highest, "Lowest price should be smaller than highest!"
        assert lowest >= self.lowestprice and highest <= self.highestprice, 'PriceError'
        if date is None:
            date = self.newest
        assert date in self.dates, "Not available date."
        lst = LinkedList()
        for item in self.list:
            if item['price'] != 'Pending' and item['date'] == date:
                if int(item['price']) in range(lowest, highest+1):
                    lst.add(item)
        return lst

    def rate_range(self, lowest, highest, date=None):
        '''
        DataADT, int, int -> LinkedDict()
        Take lowest and highest rate and return all devices that are
        in range of these rates.  
        If you don`t enter date it will return data about newest date.
        Rate should be between 0 and 100.
        '''
        assert lowest <= highest, "Lowest rate should be smaller than highest!"
        assert lowest >= 0 and highest <= 100, 'RateError'
        if date is None:
            date = self.newest
        assert date in self.dates, "Not available date."
        lst = LinkedList()
        for item in self.list:
            if item['date'] == date:
                if int(item['rate']) in range(lowest, highest+1):
                    lst.add(item)
        return lst
            