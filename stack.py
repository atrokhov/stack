class Stack(object):

    def __init__(self, length):
        self.items = []
        self.length = length

    def is_empty(self):
        return self.items == []

    def is_full(self):
        if len(self.items) >= self.length:
            return True
        else:
            return False

    def push(self, item):
        if self.is_full() == False:
            self.items.append(item)
        else:
            return "Stack is full!"

    def pop(self):
        if self.is_empty() == False:
            return self.items.pop()
        else:
            return "Stack is empty!"

    def top(self):
        if self.is_empty() == False:
            return self.items[-1]
        else:
            return "Stack is empty!"

    def size(self):
        return "Stack length: {0}. Places left: {1}".format(len(self.items), self.length - len(self.items))



    