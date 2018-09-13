class Stack(object):

    def __init__(self, length):
        self.items = []
        self.length = length

    def is_empty(self):
        if len(self.items) == 0:
            return True
        # This else need for returning False, not None
        else:
            return False

    def is_full(self):
        if len(self.items) >= self.length:
            return True
        # This else need for returning False, not None
        else:
            return False

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            return "Stack is full!"

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"

    def size(self):
        return "Stack length: {0}. Places left: {1}".format(len(self.items), self.length - len(self.items))