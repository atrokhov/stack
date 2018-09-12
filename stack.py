class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError: 
            return "Can't pop. Stack is empty"

    def top(self):
        try:
            return self.items[-1]
        except IndexError: 
            return "Stack is empty"

    def size(self):
        return len(self.items)

    def is_full(self):
        return False