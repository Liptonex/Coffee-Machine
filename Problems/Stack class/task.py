class Stack():
    elements = []
    def __init__(self):
        pass

    def push(self, el):
        Stack.elements.append(el)
        pass

    def pop(self):
        self.popped = Stack.elements[-1]
        Stack.elements.pop()
        return self.popped

    def peek(self):
        return Stack.elements[-1]
    def is_empty(self):
        if Stack.elements == []:
            return True
        else:
            return False

