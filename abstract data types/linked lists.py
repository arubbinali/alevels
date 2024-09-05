#linked list
class Node():
    def __init__(self, element):
        self.element = element
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        else:
            self.head = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.element, end = " -> ")
            current = current.next
        print("None")

linked_list = LinkedList()

for _ in range(int(input("Enter number of nodes you'd want to add:   "))):
    linked_list.append(int(input("Enter node value:   ")))

linked_list.display()
