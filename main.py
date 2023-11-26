# CS331 Assignment 3, 02/14/2023

# In this assignment, you are asked to implement methods in DoublyLinkedList class following the design we discussed.
# Remind that, we are using a DoublyLinkedList with a sentinel head and a cursor pointer.
# The next node of the tail is the sentinel head, and the previous node of the sentinel head is the tail.

class DoublyLinkedList:
    # Please implement each of the following methods following the guide.
    # Here, I've only implemented the construction methods and the dunder __repr__ method. Do not change them.
    # Do not use other designs of a LinkedList.

    class Node:
        ####################    DO NOT CHANGE   ####################
        def __init__(self, item, prev=None, next=None):
            self.data = item
            self.prev = prev
            self.next = next

    def __init__(self):
        ####################    DO NOT CHANGE   ####################
        self.head = DoublyLinkedList.Node(None)  # Sentinel Head, do not delete or update this node.
        self.head.prev = self.head.next = self.head
        self.cursor = self.head
        self.length = 0

    def __len__(self):
        # return the number of items stored in this DoublyLinkedList (aka, the length)
        return self.length

    def prepend(self, item):
        # Insert item as a node right after the sentinel head.
        # Make sure the pointers are pointing to correct nodes.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        secondNode = self.head.next
        NewNode = DoublyLinkedList.Node(item, self.head, secondNode)
        self.head.next = NewNode
        secondNode.prev = NewNode
        self.length += 1

    def append(self, item):
        # Insert item as a node to the tail of this DoublyLinkedList
        # Make sure the pointers are pointing to correct nodes.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        lastNode = self.head.prev
        NewNode = DoublyLinkedList.Node(item, lastNode, self.head)
        self.head.prev = NewNode
        lastNode.next = NewNode
        self.length += 1

    def __iter__(self):
        # This method implements "for x in DoublyLinkedList".
        # You may use a generator (with keyword "yield" ) to implement the iterator method.
        # For each node after the Sentinel Head, yield its data (instead of yielding the node itself).
        currentNode = self.head.next
        while currentNode.next is not self.head:
            yield currentNode.data
            currentNode = currentNode.next
        yield self.head.prev.data

    def __repr__(self):
        ####################    DO NOT CHANGE   ####################
        return "[" + ", ".join(repr(x) for x in self) + "]"

    def cursor_set(self, index):
        assert (isinstance(index, int)) and index >= 0 and index < self.length
        # Move the cursor to the given index, where index is in range(0, self.length).
        # Don't return anything in this method.

        # Why do u start at self.head.next, what if the cursor needs to be set at self.head?

        startingNode = self.head.next
        for i in range(0, self.length):
            if i == index:
                self.cursor = startingNode
                break
            startingNode = startingNode.next

    def cursor_get(self):
        assert self.cursor is not self.head
        # Return the data in the node where the cursor points to.
        return self.cursor.data

    def cursor_update(self, item):
        assert self.cursor is not self.head
        # Update the data in the cursor to the input item.
        # Don't return anything in this method.
        self.cursor.data = item

    def __getitem__(self, index):
        assert (isinstance(index, int))
        # This method implements "DoublyLinkedList[index]".
        # Use cursor_set(.) and cursor_get(.) to return the data in the node at index.
        self.cursor_set(index)
        return self.cursor_get()

    def __setitem__(self, index, item):
        assert (isinstance(index, int))
        # This method implements "DoublyLinkedList[index] = item".
        # Use cursor_set(.) and cursor_update(.) to update the data in the node at index to the input item.
        # Don't return anything in this method.
        self.cursor_set(index)
        self.cursor_update(item)

    def cursor_insert(self, item):
        # Insert item within a node after the cursor.
        # Move the cursor to the inserted node.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        currentNode = self.cursor
        nextNode = self.cursor.next
        NewNode = DoublyLinkedList.Node(item, currentNode, nextNode)
        currentNode.next = NewNode
        nextNode.prev = NewNode
        self.cursor = NewNode
        self.length += 1

    def cursor_delete(self):
        assert self.cursor is not self.head and len(self) > 0
        # Delete the cursor node and let cursor.next be the new cursor.
        # Remember to decrease the length of this DoublyLinkedList.
        # Don't return anything in this method.

        # Don't you have to make the old cursor node equal to 'None'?

        lastNode = self.cursor.prev
        nextNode = self.cursor.next
        lastNode.next = nextNode
        nextNode.prev = lastNode
        self.cursor = nextNode
        self.length -= 1

    def __contains__(self, item):
        # This method implements "item in DoublyLinkedList" as a Boolean.
        # Return True if item is in this DoublyLinkedList, or else return False.
        currentNode = self.head
        while currentNode.next is not self.head:
            if currentNode == item:
                return True

            # What's the purpose of this statement?
            elif self.head.prev == item:
                return True


            else:
                currentNode = currentNode.next
        return False

    def __add__(self, other):
        assert (isinstance(other, DoublyLinkedList))
        # This is implementing "self + other"
        # Append the other DoublyLinkedList to the tail of this DoublyLinkedList (self).
        # Make sure that all the pointers are pointing to the correct nodes.
        # Remember to change the self.length of the updated DoublyLinkedList accordingly.
        # Don't return anything in this method, the head of the updated DoublyLinkedList is still self.head.
        other_current = other.head.next
        while other_current is not other.head:
            self.append(other_current.data)
            other_current = other_current.next
        self.length = self.__len__()

    def remove_items(self, item):
        # Remove each node in this DoublyLinkedList containing the input item as its data.
        # If at least one node is removed, remember to decrease the length of this DoublyLinkedList.
        # Don't return anything in this method.

        # NEED TO LEARN THIS ONE!
        
        lastNode = self.head.prev
        if lastNode.data == item:
            lastNode.prev.next = self.head
            self.head.prev = lastNode.prev
            self.length -= 1
        currentNode = self.head.next
        while currentNode.next is not self.head:
            previousNode = currentNode.prev
            nextNode = currentNode.next
            if currentNode.data == item:
                previousNode.next = nextNode
                nextNode.prev = previousNode
                self.length -= 1
            currentNode = currentNode.next

    def reverse_list(self):
        # Reverse the order of nodes in this DoublyLinkedList.
        # For example: if you have a DoublyLinkedList = SH <-> 1 <-> 3 <-> 5,
        # after reverse_list(), you need to update it to  SH <-> 5 <-> 3 <-> 1.
        # Here, SH means the sentinel head.
        # Since you are updating this list, don't return anything in this method.
        temporary = None
        currentNode = self.head.next
        while currentNode is not self.head:
            temporary = currentNode.prev
            currentNode.prev = currentNode.next
            currentNode.next = temporary
            currentNode = currentNode.prev

        if temporary is not None:
            self.head = temporary.prev


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
list1 = DoublyLinkedList()
# ✅
for x in range(1, 5):
    list1.append(x)
print("Let's start with a list consists of the first four positive integers: list1 =", list1,
      ", and its length =", list1.length, ".")
# ✅
for x in range(4, 8):
    list1.prepend(x)
print("Then we prepend integers 7,6,5,4 to the front, and list1 =", list1, ", and its length =", list1.length, ".")

# ✅
list1.remove_items(4)
print("After removing all 4's from list1, we get list1 =", list1, ", and its length =", list1.length, ".")

# ✅
list1[3] = 8
print("Let's update number 1 in list1 to 8, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

# ✅
list1.cursor_set(2)
for x in range(9, 11):
    list1.cursor_insert(x)
print("Insert number 9 and 10 after number 5, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

# ✅
list1.cursor_set(1)
for x in range(3):
    list1.cursor_delete()
print("Delete three continuous numbers starting with 6, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

print("Does list1 contains number 5? The answer is", 5 in list1, ".")

# ✅
list2 = DoublyLinkedList()
list2.cursor_insert(1)
print("Let list2 be a list containing only number 1: list2 =", list2, ".")

# list2 + list1
# print("If we add list1 to the tail of list2, the new list2 =", list2, ", and its length =", list2.length, ".")
#
# list2.reverse_list()
# print("Let's reverse the order of numbers in list2, we get list2 =", list2, ".")
