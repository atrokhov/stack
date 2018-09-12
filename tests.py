import random
from stack import * 

def test_stack_is_empty():
    stack = Stack()
    if stack.is_empty() == True:
        return "Test for is_empty is OK"
    else:
        return "Test for is_empty is failed"

def test_stack_push():
    stack = Stack()

    stack.push("Hi")
    if stack.is_empty() == False and stack.top() == "Hi":
        return "Test for push is OK"
    else:
        return "Test for push is failed"

def test_stack_pop():
    stack = Stack()

    stack.push("Hi")
    stack.push("Hello")
    stack.pop()
    if stack.top() == "Hi" and stack.size() == 1:
        return "Test for pop is OK"
    else:
        return "Test for pop is failed"

def test_empty_stack_pop():
    stack = Stack()

    stack.pop()
    if stack.top() == "Stack is empty" and stack.size() == 0 and stack.pop() == "Can't pop. Stack is empty":
        return "Test for empty pop is OK"
    else:
        return "Test for empty pop is failed"

def test_stack_top():
    stack = Stack()

    stack.push("Hi")
    if stack.top() == "Hi" and stack.size() == 1:
        return "Test for top is OK"
    else:
        return "Test for top is failed"

def test_empty_stack_top():
    stack = Stack()

    if stack.top() == "Stack is empty" and stack.size() == 0:
        return "Test for empty top is OK"
    else:
        return "Test for empty top is failed"

def test_empty_stack_size():
    stack = Stack()

    if stack.size() == 0:
        return "Test for empty size is OK"
    else:
        return "Test for empty size is failed"

def test_stack_size():
    stack = Stack()

    stack.push("Hi")
    if stack.size() == 1:
        return "Test for size is OK"
    else:
        return "Test for size is failed"

def test_stack_is_full():
    stack = Stack()

    for i in xrange(1, 1000000):
        item = random.randint(1, 10000)
        stack.push(item)

    if stack.is_full() == False:
        return "Test for full is OK"
    else:
        return "Test for size is failed"

print test_stack_is_empty()
print test_stack_push()
print test_stack_pop()
print test_empty_stack_pop()
print test_stack_top()
print test_empty_stack_top()
print test_empty_stack_size()
print test_stack_size()
print test_stack_is_full()