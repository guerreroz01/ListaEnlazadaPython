
class Node:
    def __init__(self, data):
        self.head = None
        self.data = data
        self.next = None



class LinkList:
    def __init__(self):
        self._anchor = None
        self._last = None
        self._work = None
        self.size = 0

    # agregar Nodo
    def appendNode(self, data):
        if self._anchor == None:
            NewNode = Node(data)
            self._anchor = NewNode
            self._last = NewNode
            self.size += 1 
            return self._last
        else:
            self._work = self._anchor
            while True:
                if self._work.next == None:
                    NewNode = Node(data)
                    NewNode.head = self._work
                    self._work.next = NewNode
                    self._last = NewNode
                    self.size += 1
                    break
                
                self._work = self._work.next
            return self._last

    # recorrer lista hacia adelante
    def showListForward(self):
        if self.size == 0:
            print("The Linked List is Empty, please add Nodes with the appendNode")
            return
        self._work = self._anchor
        while True:
            print(self._work.data)
            if self._work.next == None: break
            self._work = self._work.next


    # recorrer lista hacia atras
    def showListBackward(self):
        if self.size == 0:
            print("The Linked List is Empty, please add Nodes with the appendNode")
            return
        self._work = self._last
        while True:
            print(self._work.data)
            if self._work.head == None: break
            self._work = self._work.head

    # borrar nodo
    def deleteNode(self, data):
        if self.size == 0:
            print("There's not Node to delete in this List, please add a Node before to delete")
            return None
        self._work = self._anchor
        nodeToDelete = None
        while True:
            if self._work.data == data:
                nodeToDelete = self._work
                self._work.head.next = self._work.next
                self._work.next.head = self._work.head
                self.size -= 1
                break
            elif self._work.data != data and self._work.next == None:
                print("the Node you try to delete is not in the List")
                return None

            self._work = self._work.next
        return nodeToDelete


    # agregar un nodo antes de un dato
    def insertNodeBefore(self, dataBefore, data):
        if self.size == 0:
            print("The List is empty, please add a Node before with the appendNode method")
            return None
        self._work = self._anchor
        while True:
            if self._work.data == dataBefore and self._work.head == None:
                NewNode = Node(data)
                NewNode.next = self._work
                self._work.head = NewNode
                self._anchor = NewNode
                self.size += 1
                break
            if self._work.data == dataBefore:
                NewNode = Node(data)
                NewNode.next = self._work
                NewNode.head = self._work.head
                self._work.head.next = NewNode
                self._work.head = NewNode
                self.size += 1
                break
            elif self._work.data != dataBefore and self._work.next == None:
                print("There's not Node with this data on the List, please add a Node before")
                return None
            
            self._work = self._work.next
        return self._work.head

    # agregar un nodo despues de un dato
    def insertNodeAfter(self, dataAfter, data):
        if self.size == 0:
            print("The List is empty, please add a Node before with the appendNode method")
            return None
        self._work = self._anchor
        while True:
            if self._work.data == dataAfter and self._work.next == None:
                NewNode = Node(data)
                NewNode.head = self._work
                self._work.next = NewNode
                self._last = NewNode
                self.size += 1
                break
            if self._work.data == dataAfter:
                NewNode = Node(data)
                NewNode.next = self._work.next
                NewNode.head = self._work
                NewNode.next.head = NewNode
                self._work.next = NewNode
                self.size += 1
                break
            elif self._work.data != dataAfter and self._work.next == None:
                print("There's not Node with this data on the List, please add a Node before")
                return None

            self._work = self._work.next
        return self._work.next

    # actualizar nodo
    def updateNode(self, oldData, newData):
        if self.size == 0:
            print("The List is empty, please add a Node before with the appendNode method")
            return None 
        self._work = self._anchor
        updatedNode = None
        while True:
            if self._work.data == oldData:
                self._work.data = newData
                updatedNode = self._work
                break
            elif self._work.data != oldData and self._work.next == None:
                print("There's not Node with this data on the List, please add a Node before")
                return None

            self._work = self._work.next
        return updatedNode




miLista = LinkList()

miLista.appendNode(100)
miLista.insertNodeAfter(100, 500)

miLista.showListForward()
miLista.showListBackward()
