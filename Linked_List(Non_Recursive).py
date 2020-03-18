class Node:
    def __init__(self,data,link):
        self._data = data
        self._link = link

    def get_data(self):
        return self._data

    def get_link(self):
        return self._link

    def change_data(self,data):
        self._data = data

    def change_link(self,link):
        self._link = link

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def inserthead(self,data):
        node = Node(data,None)
        node.change_link(self._head)
        self._head = node

    def inserttail(self,data):
        node = Node(data,self._tail)
        if self._head == None:
            self._head = node
        else:
            temp = self._head
            while temp != None:
                if temp.get_link() == None:
                    temp.change_link(node)
                    temp = None
                else:
                    temp = temp.get_link()

    def search(self,data):
        if self._head == None:
            return False
        elif self._head.get_data() == data:
            return True
        else:
            node = self._head.get_link()
            while node != None:
                if node.get_data() == data:
                    node = None
                    return True
                else:
                    node = node.get_link()
                    if node == None:
                        return False

    def get_head(self):
        return self._head.get_data()

    def get_tail(self):
        if self._head == None:
            return None
        else:
            node = self._head
            while node != None:
                if node.get_link() == None:
                    return node.get_data()
                else:
                    node = node.get_link()

    def insert_head_2(self,data):
        if self._head == None:
            self._head == Node(data,self._tail)
        else:
            if self.search(data) == False:
                node = Node(data, self._head)
                self._head = node
            else:
                print("Data already exists in List")

    def print(self):
        node = self._head
        while node != None:
            print(node.get_data())
            node = node.get_link()

LIST = LinkedList()
for i in range(15):
    LIST.inserthead(i+1)
#print(LIST.search(12))
#LIST.inserttail(20)
#LIST.insert_head_2(20)
#LIST.insert_head_2(12)
#LIST.print()      
#print(LIST.get_head())
#print(LIST.get_tail())      