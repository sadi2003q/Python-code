class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def addtohead(self, data):
        node = Node(data)
        self.head = node

    def addtotail(self, data):
        if self.head is None:
            self.addtohead(data)
        else:
            node = Node(data)
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = node

    def deletenode(self, data):
        if self.head is None:
            print("list is empty")
        elif self.head.data == data:
            node = self.head
            self.head = self.head.next
            del node
        else:
            currentNode = self.head
            while currentNode.next is not None:
                if currentNode.next.data == data:
                    node = currentNode.next
                    currentNode.next = currentNode.next.next
                    del node
                    break
                else:
                    currentNode = currentNode.next

    def reverse(self):
        if self.head is None:
            print('List is empty')
        elif self.head.next is None:
            return
        else:
            previous = None
            current = self.head

            while current is not None:
                next = current.next

                current.next = previous
                previous = current

                current = next
            self.head = previous

    def swapPair(self):
        if self.head is None or self.head.next is None:
            return
        else:
            dummy = Node(self.head, 0)
            dummy.next =self.head
            previous = dummy

            while previous.next is not None and previous.next.next is not None:
                first = previous.next
                second = previous.next.next

                previous.next = second
                first.next = second.next
                second.next = first

                previous = first
            self.head = dummy.next

    def printlist(self):
        if self.head is None:
            print("list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.data, end="->")
                node = node.next


list = LinkedList()
for i in range(21):
    list.addtotail(i)
print("before deleting")
list.printlist()

# print("After deleting")
# list.deletenode(13)
# list.printlist()


# print("reverse linked List")
# list.reverse()
# list.printlist()
print('\n\nafter deleting')
list.swapPair()
list.printlist()
