

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time

    def insert(self, data):
        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if there is atleast 1 item in the data structure, we keep inserting items at the
        # end of the linked lists
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            # print("%d" % actual_node.data)
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            # print("%d" % actual_node.data)
            print(actual_node.data)
            actual_node = actual_node.previous


if __name__ == "__main__":
    linkedlist = DoublyLinkedList()
    linkedlist.insert("hai")
    linkedlist.insert("hello")
    linkedlist.insert(10)
    linkedlist.insert(4)
    linkedlist.insert(5)
    print("traversing in forward direction")
    linkedlist.traverse_forward()
    print("traversing in backward direction")
    linkedlist.traverse_backward()

