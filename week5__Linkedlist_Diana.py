# Node class represents each element in thw linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, pos):
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.prepend(data)
            return
        new_node = node(data)
        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value not found")

    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    def display(self):
        temp = self.head

        if self.is_empty():
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# TEST CASES
if __name__ == "__main__":
    print("=== Singly Linked List Test Cases ===")

    sll = SinglyLinkedList()

    # Test 1: Empty list
    print("check if list is empty")
    print("Is empty:", sll.is_empty()) 

    # Test 2: Append elements
    print("Append elements")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.display()  

    # Test 3: Prepend element
    print("Prepend element")
    sll.prepend(5)
    sll.display() 

    # Test 4: Insert at position
    print("Insert at position 2")
    sll.insert_at_position(15, 2)
    sll.display()  

    # Test 5: Delete by value
    print("Delete value 20")
    sll.delete_by_value(20)
    sll.display()  

    # Test 6: Search value
    print("Search for 15")
    print("Index:", sll.search(15))  

    # Test 7: Size of list
    print("Size of list")
    print("Size:", sll.size())  

    # Test 8: Delete non-existing value
    print("Delete non-existing value 100")
    sll.delete_by_value(100)  

    # Test 9: single element list
    print("Single element list")
    single = SinglyLinkedList()
    single.append(1)
    single.display()
    single.delete_by_value(1)
    single.display()  
