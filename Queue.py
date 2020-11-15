class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Queue:
    """
    Queue is Data Structure which Follows a Principle of FirstInFirstOut which means the element entered
    first will be the element deleted at first and the element entered at last will be the element to be
    deleted at last. Queue is otherwise called as LastInLastOut.

    Use Cases:
        Queue is widely used Data Structure like Booking services where a person books first will get
        his ticket at first.
    """
    def __init__(self,head =None, tail = None):
        self.head = head
        self.tail = tail

    def enque(self):
        """
        Adding Elements into the Queue
        """
        n = int(input("Enter a number of N terms you would likely to create: "))
        for i in range(n):
            new_node = Node(int(input()))
            tail = self.tail
            if self.head is not None:
                tail.next = new_node
                tail = new_node
                self.tail =  tail
            else:
                self.head = new_node
                self.tail = new_node

    def dequeue(self):
        """
        Deleting the First Element from the Queue
        """
        self.head = self.head.next
    def printqueue(self):
        head = self.head
        print("The Queue Elements are: ",end=" ")
        while(head!=None):
            print(head.data,end=" ")
            head = head.next

queue = Queue()
queue.enque()
queue.printqueue()
queue.dequeue()
queue.printqueue()
print('\n')
