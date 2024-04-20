class Node:

    def Node(self, element: int):
        self.element = element
        self.next = None


class LinkedList:
    
    def LinkedList(self):
        self.head: Node = None
        self.tail: Node = None
        self.count: int = 0

    def insert(self, element):
        n: Node = Node(element)

        if self.head is None:
            self.head = n
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = n
            self.tail = self.tail.next
            count += 1


def reverse_linked_list(ll: LinkedList) -> LinkedList:
    if ll.count == 0:
        raise Exception('LinkedList is empty')
    
    prev: Node = ll.head
    actual: Node = prev.next
    newHead = reverse_linked_list(prev, actual)
    ll.head = newHead
    ll.tail = prev
    ll.tail.next = None

    return ll

def reverse_linked_list(prev: Node, actual: Node) -> Node:
    if actual.next is None:
        actual.next = prev
        return actual
    
    head = reverse_linked_list(actual, actual.next)
    actual.next = prev
    return head
