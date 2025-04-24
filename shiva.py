class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=",")
            current = current.next
        print("none")
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    def prepend(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def remove(self, key):
        current = self.head
        pre = None
        while current:
            if current.data == key:
                if pre:
                    pre.next = current.next
                else:
                    self.head = current.next
                return True
            pre = current
            current = current.next
        return False
ll = SinglyLinkedList()
ll.prepend(30)
ll.prepend(20)
ll.prepend(10)
print('the linked list element are:')
ll.traverse()
print("Searching for 20:", ll.search(20))
print("Searching for 40:", ll.search(40))
print("Removing 20...", ll.remove(20))
ll.traverse()