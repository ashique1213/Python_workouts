class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_in_begning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self,data):
        current = self.head
        if current is None:
            print("Empty")
            return
        if current.data == data:
            self.head = current.next
            return
        while current.next !=None and current.next.data !=data:
            current = current.next
        current.next = current.next.next

    def delete_end(self):
        if self.head is None:
            print("Empty")
            return
        current = self.head
        while current.next != None and current.next.next != None:
            current = current.next
        current.next = None

    def delete_beg(self):
        if self.head is None:
            print("None")
        self.head = self.head.next

    def delete_occurance(self,value):
        if not self.head:
            print("Empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                print(current.data,"Found")
            current = current.next

    def count(self):
        current = self.head
        c=0
        while current:
            current = current.next
            c+=1
        print(c)


    def reverse(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def delete_duplicates(self):
        if self.head is None:
            print("Empty")
            return 
        current = self.head
        while current and current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next

    def middle_of_linkedlist(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        print(slow_pointer.data)
    
    def sum_of(self):
        current = self.head
        result = 0
        while current:
            result += current.data
            current = current.next
        print(result)

    def remove_4(self):
        if self.head is None:
            print("Empty")
            return
        while self.head and self.head.data == 4:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == 4:
                current.next = current.next.next
            else:
                current = current.next
    
    def remove_middle(self):
        if self.head is None:
            print("Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        slow_pointer = self.head
        fast_pointer = self.head
        value = None
        while fast_pointer and fast_pointer.next:
            value = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        print("Mid:",slow_pointer.data)
        if value:
            value.next = value.next.next


    def display(self):
        if not self.head:
            print("Empty")
            return
        current = self.head
        while current:
            print(current.data,end=' -> ')
            current = current.next
        print('None')

ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(4)
ll.display()
ll.insert_in_begning(5)
ll.display()
# ll.delete(4)
# ll.delete_end()
# ll.delete_beg()
# ll.delete_occurance(4)
ll.search(4)
ll.display()
ll.reverse()
ll.display()
# ll.delete_duplicates()
# ll.display()
# ll.middle_of_linkedlist()
# ll.sum_of()
ll.insert(4)
ll.display()
# ll.remove_4()
ll.display()
ll.remove_middle()
ll.display()
