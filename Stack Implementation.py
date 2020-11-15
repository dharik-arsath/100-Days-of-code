class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None
class Stack:
    """
    Stack is a LastInFirstOut Data Structure which is used for deleting the element which comes very recently
    It is used in places like out browser history where our old history goes down and down and our
    new search history appears on top of all. It is implemented in a same way where elements are stored in
    reverse order as Last added element will placed at first and first added element will go at last
    """
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
    def create(self):
        """
        Create a elements to make a stack of it.
        """
        head = self.head
        n = int(input("Enter a number of node to insert into a stack: "))
        for i in range(n):
            new_node = Node(int(input("Enter a number to add into the stack: ")))
            if head != None:
                new_node.next = head
                head = new_node
                self.head = head
            else:
                head = new_node
                self.head = new_node

    def popitem(self):
        """
        As per the principle of Stack DataStructure we have removed the recently added element
        """
        head = self.head
        print(f"\nThe Deleted Element is: {head.data}")
        head = head.next
        self.head = head

    def printstack(self):
        head = self.head
        print("The Elements of Stack are:  ",end=" ")
        while(head!=None):
            print(head.data,end=" ")
            head = head.next

# Let's Create an object named my_stack
stack = Stack()
# Calling the methods in my object
stack.create()
stack.printstack()
stack.popitem()
stack.printstack()
