'''Module with linked list and linked dictionary'''
class Node:
    '''Represents Node'''
    def __init__(self, data, id=None, next=None):
        '''
        Node, str/int, str/int, Node -> NoneType
        '''
        self.data = data
        self.next = next
        self.id = id

class LinkedList:
    '''Represents linked list'''
    def __init__(self):
        '''
        LinkedList -> NoneType
        '''
        self.head = None
    
    def add(self, data):
        '''
        LinkedList, str/int -> NoneType
        Take string or number and add it to LinkedList.
        '''
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def __str__(self):
        '''
        LinkedList -> str
        Return string with all elements from list.
        '''
        current = self.head
        st = ''
        while current:
            st += str(current.data) + ', '
            current = current.next
        return st[:-2]

    def __len__(self):
        '''
        LinkedList -> int
        Return length of linked list.
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def __iter__(self):
        '''
        LinkedList -> str
        Return elements of list
        '''
        return LinkedListIterator(self.head)

class LinkedDict:
    '''Represent dictionary'''
    def __init__(self):
        '''
        LinkedDict -> NoneType
        '''
        self.head = None
    
    def add(self, data, id):
        '''
        LinkedDict -> NoneType
        Take two values add them to LinkedDict.
        First as data(value) and second as id(key).
        '''
        newNode = Node(data, id)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def __getitem__(self, id):
        '''
        LinkedDict -> str/int
        Return value by key.
        '''
        current = self.head
        assert len(self) != 0, "Your dict is empty."
        while current:
            if current.id == id:
                return current.data
            current = current.next
        return 'Wrong id'

    def __str__(self):
        '''
        LinkedDict -> str
        Return string with all elements from dictionary.
        '''
        current = self.head
        st = ''
        while current:
            st += str(current.id) + ': ' + str(current.data) + ', '
            current = current.next
        return st[:-2]
    
    def __len__(self):
        '''
        LinkedDict -> int
        Return length by dictionary.
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def __iter__(self):
        '''
        LinkedDict -> str/int
        Return keys of dictionary.
        '''
        return LinkedDictIterator(self.head)
    
    def items(self):
        '''
        LinkedDict -> str/int
        Return values of dictionary.
        '''
        return LinkedDictIterator(self.head)

    def __setitem__(self, key, value):
        '''
        LinkedDict -> str/int
        Change value of key.
        '''
        current = self.head
        while current:
            if current.id == key:
                current.data = value
                return None
            else:
                current = current.next


class LinkedListIterator:
    '''Represents linked list Iterator'''
    def __init__(self, head):
        '''
        LinkedListIterator, str/int -> NoneType
        '''
        self.current = head

    def __iter__(self):
        '''
        LinkedListIterator -> LinkedListIterator
        '''
        return self

    def __next__(self):
        '''
        LinkedListIterator -> int/str
        '''
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class LinkedDictIterator:
    def __init__(self, head):
        '''
        LinkedDictIterator -> NoneType
        '''
        self.cur = head

    def __iter__(self):
        '''
        LinkedDictIterator -> LinkedDictIterator
        '''
        return self

    def __next__(self):
        '''
        LinkedDictIterator -> str/int
        '''
        if not self.cur:
            raise StopIteration
        else:
            key = self.cur.id
            self.cur = self.cur.next
            return key
