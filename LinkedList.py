# Create the node holding the data and the pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: any):
        new_node = Node(data)  #? Create a new node
        if not self.head:  #? If the list is empty (no head), make this node the head
            self.head = new_node
            return

        current = self.head  #? Make the head the current node
        while current.next:  #? Traverse the list as long as there's a "next" node
            current = current.next
        else:
            current.next = new_node  #? The last node to have a next, append the node after it

    def delete_node(self, data: any):  # specify head/tail/position
        if data == self.head.data:
            current = self.head
            self.head = self.head.next
            current.next = None

    def insert(self):  # specify head/tail/position
        pass

    def find_node(self):
        pass

    def reverse(self):
        pass

    def find_middle(self):
        pass

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        # print("None")


llist = LinkedList()
llist.append(2)
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(10)
llist.append(12)
llist.append(24)
llist.print_list()
