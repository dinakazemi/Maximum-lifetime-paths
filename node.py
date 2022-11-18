class node:
        def __init__(self, key,value):
                self.key = key
                self.value = value
                self.next = None
        def get_key(self):
                return self.key
        def get_value(self):
                return self.value
        def get_next(self):
                return self.next
        def set_next(self, next):
                self.next = next
        def set_value(self, value):
                self.value= value
