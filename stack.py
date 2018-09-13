class Stack:

    def __init__(self, length):
        self.items = []
        self.length = length

    def is_empty(self):
        return not bool(self.items)

    def is_full(self):
        return bool(len(self.items) >= self.length)

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            return "Stack is full!"

    def pop(self):
        try: 
            return self.items.pop()
        except IndexError:
            return "Stack is empty!"

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return "Stack is empty!"

    def size(self):
        return "Stack length: {0}. Places left: {1}".format(len(self.items), self.length - len(self.items))