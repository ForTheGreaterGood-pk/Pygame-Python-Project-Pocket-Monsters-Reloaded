class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(), "Empty stack!"
        x = self.elements.pop()
        return x

    def push(self, value):
        self.elements.append(value)