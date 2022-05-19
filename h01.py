class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_Front(self, item):
        self.items.append(item)
    def add_Rear(self, item):
        self.items.insert(0,item)
    def remove_Front(self):
        return self.items.pop()
    def remove_Rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
d = Deque()
d.add_Front(1)
d.add_Front(2)
d.add_Rear(3)
d.add_Rear(4)
d.add_Front(5)
d.add_Rear(6)
d.remove_Front()
d.add_Front(7)
d.remove_Rear()
d.add_Rear(8)
print(d.items)
