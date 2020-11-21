
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
        self._work = self._anchor
        while True:
            print(self._work.data)
            if self._work.next == None: break
            self._work = self._work.next


    # recorrer lista hacia atras
    def showListBackward(self):
        self._work = self._last
        while True:
            print(self._work.data)
            if self._work.head == None: break
            self._work = self._work.head

    # borrar nodo
    def deleteNode(self, data):
        self._work = self._anchor
        nodeToDelete = None
        while True:
            if self._work.data == data:
                nodeToDelete = self._work
                self._work.head.next = self._work.next
                self._work.next.head = self._work.head
                self.size -= 1
                break

            self._work = self._work.next
        return nodeToDelete


    # agregar un nodo antes de un dato
    def insertNodeBefore(self, dataBefore, data):
        self._work = self._anchor
        while True:
            if self._work.data == dataBefore:
                NewNode = Node(data)
                NewNode.next = self._work
                NewNode.head = self._work.head
                self._work.head.next = NewNode
                self._work.head = NewNode
                self.size -= 1
                break
            
            self._work = self._work.next
        return self._work.head

    # agregar un nodo despues de un dato
    def insertNodeAfter(self, dataAfter, data):
        self._work = self._anchor
        while True:
            if self._work.data == dataAfter:
                NewNode = Node(data)
                NewNode.next = self._work.next
                NewNode.head = self._work
                NewNode.next.head = NewNode
                self._work.next = NewNode
                self.size -= 1
                break

            self._work = self._work.next
        return self._work.next

    # actualizar nodo
    def updateNode(self, oldData, newData):
        self._work = self._anchor
        updatedNode = None
        while True:
            if self._work.data == oldData:
                self._work.data = newData
                updatedNode = self._work
                break

            self._work = self._work.next
        return updatedNode




miLista = LinkList()

miLista.appendNode(100)
miLista.appendNode(200)
miLista.appendNode(300)
miLista.appendNode(400)
miLista.appendNode(500)
miLista.appendNode(600)


x = miLista.insertNodeAfter(500, 50000)
miLista.showListForward()
print("\n******************************\n")
print(x.data)
