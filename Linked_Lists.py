#Question:
#Class should have identifiers that point to both the head and tail
#Should have a method to insert at the head 
#Should have a method to insert at the tail at the end of the list
#Should have a method to remove the head
#Should have a method to remove the tail
##########################################################################################
import string as string
class LinkedList:
    #LinkedList: A Linked list can peform the following operations
    # insert_head(a_node)
    #   Purpose: To make the given node the head of the LinkedList
    # insert_tail(a_node)
    #   Purpose: To make the given node the tail of the LinkedList
    # remove_head()
    #   Purpose: To remove initial head-node and make second node head-node
    # remove_tail()
    #   Purpose: To remove initial tail-node and make second-2-last node tail-node
    # change_head(a_node_data)
    #   Purpose: To update the data in the node at head of LinkedList
    # change_tail(a_node_data)
    #   Purpose: To update the data in the node at tail of LinkedList
    # printl(a-node)
    #   Purpose: To print out nodes in a LinkedList
    # search(a-node,key)
    #   Purpose: To compute if a node-data is in the LinkedList
    # remove(a-node)
    #   Purpose: To remove a node from the LinkedList

    #LinkedList: head tail
    # An Empty LinkedList has:
    #   head = None
    #   tail = None   
    def __init__(self):
        self._head = None
        self._tail = None        
    
    def get_head(self):
        return self._head

    #To make the given node the head
    def insert_head(self, node):
        node.change_link(self._head)
        self._head = node

    #To insert the given node into head avoiding repeated data
    def insert_head_2(self, node):
        if self.search(self._head, node.get_data()) == True:
            print("Error: Node already exists!")
        else:
            node.change_link(self._head)
            self._head = node
        
    #To get the last node in the Linked List
    #   To help the insert_tail function
    def get_last(self):
        Done = False
        node = self._head
        while Done is not True:
            if node.get_link() == self._tail:
                Done = True
                return node
            else:
                node = node.get_link()

    #To make the given node the tail of the LinkedList       
    def insert_tail(self, node):
        node.change_link(self._tail)
        self.get_last().change_link(node)
    
    #To remove node at head of the LinkedList
    def remove_head(self):
        self._head = self._head.get_link()
    
    #To remove node at tail of LinkedList
    def remove_tail(self):
        self.removetailhelper(self._head)

    #To help the remove_tail function
    def removetailhelper(self, node):
        if node != None:
            if node.get_link().get_link() == None:
                node.change_link(None)
            else:
                self.removetailhelper(node.get_link()) 

    #To Print out all the nodes in the LinkedList
    def printl(self, node):
        if (node != None):
            print(node.get_data())
            self.printl(node.get_link())

    #To mutate the data in the head node
    def change_head(self,data):
        self._head.change_data(data)

    #To mutate the data in the tail node
    def change_tail(self,data):
        self.get_last().change_data(data)

    #To compute if a node-data is in the LinkedList
    def search(self,node,key):
        if (node != None and node.get_data() == key):
            return True
        elif(node != None and node.get_link() != None):
            return self.search(node.get_link(),key)
        else:
            return False

    #To remove all duplicate data in a Linked_List
    def remove_duplicates(self):
        elem = []
        elem = self.removehelper(self._head, elem)
        elem.reverse()
        self._head = None
        for i in elem:
            self.insert_head_2(Node(i,None))

    #To remove a node from the LinkedList
    def remove(self, data):
        elem = []
        elem = self.removehelper(self._head, elem)
        elem.remove(data)
        elem.reverse()
        self._head = None
        for i in elem:
            self.insert_head(Node(i,None))

    #To help the remove function
    def removehelper(self,node,elem):
        if (node != None):
            elem.append(node.get_data())
            self.removehelper(node.get_link(),elem)
        return elem

    def nth_fromtail(self,node,n):
        len = self.getlent(self._head,0)
        index = len - (n-1)
        Nth = None
        i = 1
        while node != None:
            if i == index:
                Nth = node.get_data()
                node = None
                print(Nth)
            else:
                i += 1
                node = node.get_link()
            
    def getlent(self,node,i):
        if node != None:
            i += 1
            return self.getlent(node.get_link(),i)
        else:
            return i
        
##################################################################################
class Node:
    #Node: data Node
    def __init__(self,data,link):
        self._data = data
        self._link = link
    
    #To get the data in a node
    def get_data(self):
        return self._data
    
    #To mutate the data in a node
    def change_data(self, data):
        self._data = data
    
    #To get node that is linked to this node
    def get_link(self):
        return self._link
    
    #To mutate the node that is linked to this node
    def change_link(self, link):
        self._link = link
############################################################################################
#To insert the entire alphabet characters into a LinkedList
FullList = LinkedList()
for i in string.ascii_lowercase:
    FullList.insert_head(Node(i,None))

#To create an instance of the Node Class
A = Node("4",None)
B = Node("5",None)

#To test the LinkedList FullList

#FullList.insert_head(A)
#FullList.insert_tail(B)
#FullList.remove_head()
#FullList.remove_tail()
#FullList.change_head("0")
#FullList.change_tail("1")
#print(FullList.search(FullList.get_head(),"w"))
#FullList.remove("w")
#print(FullList.search(FullList.get_head(),"w"))
#FullList.insert_head_2(Node("3",None))
#FullList.printl(FullList.get_head())











'''
#Second Test Passed
A = Node("a",None)
B = Node("b",None)
C = Node("c",None)
D = Node("d",None)
E = Node("e",None)
F = Node("f",None)
mylist = LinkedList()
mylist.insert_head(A)
mylist.insert_head(B)
mylist.insert_head(C)
mylist.insert_head(D)
mylist.insert_head(E)
mylist.insert_tail(F)
mylist.remove_head()
mylist.remove_tail()
mylist.displayvals()
'''
#print(string.ascii_uppercase)

        
    

