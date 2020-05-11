from LinkedList import LinkedList, LinkedDict
import json

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
                        value = int(item['price'].replace(',', ''))
                    # convert rate into int
                    if param == 'rate':
                        value = int(item['rate'].replace(',', ''))
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
        diction = LinkedDict()
        for item in self.list:
            if item['date'] in diction:
                diction[item['date']] = diction[item['date']] + 1
            else:
                diction.add(1, item['date'])
        return diction
    
    def date_count_avail(self):
        diction = LinkedDict()
        for item in self.list:
            if item['price'] != 'Pending':
                if item['date'] in diction:
                    diction[item['date']] = diction[item['date']] + 1
                else:
                    diction.add(1, item['date'])
        return diction

    def category_count(self):
        diction = LinkedDict()
        for item in self.list:
            for category in item['category']:
                if item['date'] == self.newest:
                    if category in diction:
                        diction[category] = diction[category] + 1
                    else:
                        diction.add(1, category)
        return diction
    
    def category_count_avail(self):
        diction = LinkedDict()
        for category in self.categories:
            diction.add(0, category)
        for item in self.list:
            if item['price'] != 'Pending' and item['date'] == self.newest:
                for category in item['category']:
                    diction[category] = diction[category] + 1
        return diction

    def price_range(self, lowest, highest):
        assert lowest <= highest, "Lowest price should be smaller than highest!"
        lst = LinkedList()
        for item in self.list:
            if item['price'] != 'Pending' and item['date'] == self.newest:
                if int(item['price']) in range(lowest, highest+1):
                    lst.add(item)
        return lst

d = DataADT()
with open('data1.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)

d.insert(data)
