import timeit
import statistics

#regList
myList = []

myList.append(1)
myList.insert(1,2)
myList.append(3)
myList.append(4)
myList.insert(4, 5)
print("Regular list: ")
print(myList)
print(" ")
myList.remove(3)
print("Updated list: ")
print(myList)
print("")
t1 = timeit.repeat(repeat = 5, number = 1000000)
print("Run times: ")
print(t1)
avg = statistics.mean(t1)
print("Average run time is: ", avg)
print("  ")
print("***Compared to linked list and run times below: ")
print(" ")

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class unorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, value):
        position = 0
        while value != None:
            value.position = position
            position += 1
            value = value.next

    def append(self, newData): 
        newNode = Node(newData) 
  
        if self.head is None: 
            self.head = newNode 
            return
  
        last = self.head 
        while (last.next): 
            last = last.next
        last.next = newNode

    def push(self, newData): 
        newNode = Node(newData) 
        newNode.next = self.head  
        self.head = newNode
   
    def printLinkedList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data, end = " ") 
            temp = temp.next

if __name__ == "__main__":
    myLinkedList = unorderedList()

        
    myLinkedList.push(4)
    myLinkedList.add(3)
    myLinkedList.add(2)
    myLinkedList.append(5)
    myLinkedList.push(1)
    print("Size: ", myLinkedList.size())
    print("Linked list: ")
    myLinkedList.printLinkedList()
    print(" ")
    myLinkedList.remove(3)
    print("Updated list:")
    myLinkedList.printLinkedList()
    print(" ")
    print("Size: ", myLinkedList.size())
    print("Searching for 3:")
    print(myLinkedList.search(3),".", " Cant find 3",sep="")
    print(" ")
    
print("Run times: ")
t1 = timeit.repeat(repeat = 5, number = 1000000)
print(t1)
avg = statistics.mean(t1)
print("Average run time is: ", avg)    





  
