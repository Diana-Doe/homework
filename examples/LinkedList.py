class Node:
    '''Represents Node'''
    def __init__(self, data, id=None, next=None):
        self.data = data
        self.next = next
        self.id = id

class LinkedList:
    '''Represents linked list'''
    def __init__(self):
        self.head = None
    
    def add(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def __str__(self):
        current = self.head
        st = ''
        while current:
            st += str(current.data) + ', '
            current = current.next
        return st[:-2]

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedDict:
    '''Represent dictionary'''
    def __init__(self):
        self.head = None
    
    def add(self, data, id):
        newNode = Node(data, id)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def __getitem__(self, id):
        current = self.head
        assert len(self) != 0, "Your dict is empty."
        while current:
            if current.id == id:
                return current.data
            current = current.next
        return 'Wrong id'
    
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item
# a = LinkedList()
# a.add('1')
# a.add('2')
# if '3' not in a:
#     print('no')