class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None
        self.prev = None
class Stack:
    """
    Stack is a LastInFirstOut Data Structure which is used for deleting the element which comes very recently
    It is used in places like out browser history where our old history goes down and down and our
    new search history appears on top of all. It is implemented in a same way where elements are printed in
    reverse order as Last added element will displayed at first and first added element will go at last
    """
    def __init__(self,tail = None):
        self.tail = tail
    def create(self):
        """
        Create a elements to make a stack of it.
        """
        tail = self.tail
        n = int(input("Enter a number of node to insert into a stack: "))
        for i in range(n):
            new_node = Node(int(input("Enter a number to add into the stack: ")))
            if tail != None:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node
                self.tail = tail
            else:
                tail = new_node
                self.tail = new_node

    def popitem(self):
        """
        As per the principle of Stack DataStructure we have removed the recently added element and
        printed in reverse order so that last added element visible at first and first added element
        goes at last
        """
        tail = self.tail
        print(f"The Deleted Element is {tail.data}")
        tail = tail.prev
        tail.next = None
        self.tail = tail
        self.backward_print()

    def backward_print(self):
        print("The elements is being printed based on new_comers:   ",end="")
        tail = self.tail
        while(tail!= None):
            print(tail.data,end=' ')
            tail = tail.prev
        print('\n')

# Let's Create an object named my_stack
stack = Stack()
# Calling the methods in my object
stack.create()
stack.popitem()
