class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class steck:
    def __init__(self ):
        self.top = None

    def push(self,data):
        new_node = Node (data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        current = self.top
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
#main program
x = steck()
x.push = (10)
x.push = (20)

x.display()





    
