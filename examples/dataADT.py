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
                    newDict.add(value, param)
                # add created dictionary to main LinkedList
                self.list.add(newDict)


    def by_data(self, data):
        pass

    def by_name(self, name):
        pass


d = DataADT()
with open('data.json', 'r', encoding='utf-8') as ff:
    data = json.load(ff)
d.insert(data)
print(d.categories)
print(d.dates)