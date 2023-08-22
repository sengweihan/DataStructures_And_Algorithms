#  DATA STRUCTURES FOR A LINKED LIST

"""

AUTHOR: SENG WEI HAN

WHY CHOOSE LINKED LIST OVER ARRAY
    ---> DONT NEED TO PRE-ALLOCATE SPACE
    ---> INSERTION IS EASY

TIME COMPLEXITY 
    ---> INSERT ELEMENT AT BEGINNING = O(1) 
    ---> DELETE ELEMENT AT BEGINNING = O(1)
    ---> INSERT/DELETE AT MIDDLE = O(N) BECAUSE WE NEED TO TRAVERSE DOWN THE LINKED LIST
    ---> INSERT/DELETE AT END = O(N) BECAUSE WE NEED TO TRAVERSE DOWN THE LINKED LIST
    ---> LINKED LIST TRAVERSAL = O(N)
    ---> ACCESSING ELEMENT BY VALUE = O(N) BECAUSE WE NEED TO TRAVERSE DOWN THE LINKED LIST
"""


#  INDIVIDUAL NODE CLASS
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    #  INSERT AT THE END OF THE LINKED LIST
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        #  traverse through the linked list to reach the end of the node.
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for i in range(len(data_list)-1, -1, -1):
            self.insert_at_beginning(data_list[i])

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0 and self.head is not None and self.head.next is not None:
            self.head = self.head.next
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next

        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        elif index == self.get_length() - 1:
            self.insert_at_end(data)
        else:
            itr = self.head
            for i in range(index-1):
                itr = itr.next
            itr.next = Node(data, itr.next)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        if itr.data == data_after:
            itr.next = Node(data_to_insert, itr.next)
        else:
            while itr.next:
                itr = itr.next
                if itr.data == data_after:
                    itr.next = Node(data_to_insert, itr.next)
                    break

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        if itr.data == data:
            self.head = itr.next
        else:
            while itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                else:
                    itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        list_str = ""
        itr = self.head
        while itr:
            list_str += str(itr.data) + "-->"
            itr = itr.next

        print(list_str)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])
    # linked_list.remove_at(30)
    linked_list.insert_after_value("mango", "apple")
    linked_list.insert_after_value("banana", "dududu")
    linked_list.remove_by_value("apple")
    # linked_list.insert_at(0, "dragonfruit")
    # linked_list.insert_at(2, "bamboo")
    linked_list.print()
