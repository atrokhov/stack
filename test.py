# -*- coding: utf-8 -*-
import unittest
import random
from stack import * 

class TestStackMethods(unittest.TestCase):

    def test_empty_stack_is_empty(self):
        stack = Stack(12)

        self.assertEqual(stack.is_empty(), True)
    
    def test_stack_is_empty(self):
        stack = Stack(12)
        stack.push("Hi")

        self.assertEqual(stack.is_empty(), False)

    def test_stack_push(self):
        stack = Stack(12)
        stack.push("Hi")

        self.assertEqual(stack.top(), "Hi")

    def test_full_stack_push(self):
        stack = Stack(2)
        stack.push("Hi")
        stack.push("Hello")
        
        self.assertEqual(stack.push("Hi"), "Stack is full!")

    def test_stack_pop(self):
        stack = Stack(12)
        stack.push("Hi")
        stack.push("Hello")
        stack.pop()

        self.assertEqual(stack.top(), "Hi")

    def test_empty_stack_pop(self):
        stack = Stack(12)
        stack.pop()

        self.assertEqual(stack.pop(), "Stack is empty!")
    
    def test_stack_top(self):
        stack = Stack(12)
        stack.push("Hi")

        self.assertEqual(stack.top(), "Hi")

    def test_empty_stack_top(self):
        stack = Stack(12)

        self.assertEqual(stack.top(), "Stack is empty!")

    def test_empty_stack_size(self):
        stack = Stack(12)

        self.assertEqual(stack.size(), "Stack length: 0. Places left: 12")

    def test_stack_size(self):
        stack = Stack(12)
        stack.push("Hi")

        self.assertEqual(stack.size(), "Stack length: 1. Places left: 11")

    def test_not_full_stack(self):
        stack = Stack(12)
        stack.push("Hi")

        self.assertEqual(stack.is_full(), False)

    def test_stack_is_full(self):
        stack = Stack(12)

        for i in xrange(1, 100):
            item = random.randint(1, 10000)
            stack.push(item)

        self.assertEqual(stack.is_full(), True)

if __name__ == '__main__':
    unittest.main()