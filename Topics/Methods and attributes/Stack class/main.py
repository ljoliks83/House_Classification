class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        temp = self.stack[len(self.stack)-1]
        self.stack.remove(self.stack[-1])
        return temp

    def peek(self):
        return self.stack[len(self.stack)-1]

    def is_empty(self):
        return len(self.stack) == 0