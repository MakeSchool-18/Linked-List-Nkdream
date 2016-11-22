#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None


    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))



class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO:
        #set a counter
        myint = 0
        #create a pointer that points to head
        firstNode = self.head
        #while the firstNode has a value +1 to the counter
        while firstNode is not  None:
            myint+=1
            firstNode = firstNode.next
        return myint




    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        #create a new node
        newNode = Node(item)
        #find node at tail
        self.tail
        #point from that last node in tail to new node
        if self.tail == None :
            self.tail = newNode
            self.head = newNode
            return

        self.tail.next = newNode
        #point tail to newNode
        self.tail = newNode
        pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        if self.head == None:
            self.head = Node(item)
            self.tail = Node(item)
            return
        nodeNew = Node(item)
        nodeNew.next = self.head
        self.head = nodeNew
        pass


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        cur = self.head
        # while cur.next is not None:
        #         if cur.next == item:
        #             nextNode = cur.next.next
        #             cur.next = nextNode
        #             break
        #         pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        pass


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
