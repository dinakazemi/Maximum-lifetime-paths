from node import node
class linkedList:
        def __init__(self):
                self.head = node(None, None)
        def put(self, key, value):
                n = node(key, value)
                current = self.head
                while (current.get_next()!=None):
                        current = current.get_next()
                current.set_next(n)
        
        def get(self, key):
                current = self.head
                while (current.get_next() != None):
                        current = current.get_next()
                        if (current.get_key() == key):
                                return current
                return None
        def remove(self, key):
                current = self.head
                while (current.get_next() != None):
                        if (current.get_next().get_key() == key):
                                n = current.get_next()
                                n = None
                                current.set_next(current.get_next().get_next())
                                #print (True)
                                return True
                        current = current.get_next()
                return False
        def is_empty(self):
                if self.head.get_next() == None:
                        return True
                return False
        def __repr__(self):
                s = ''
                current = self.head
                while (current.get_next() != None):
                        current = current.get_next()
                        str_id = str(current.get_key().get_id())
                        s += str_id
                        s+=":"
                        str_val = str(current.get_value())
                        s+= str_val
                        s+= ' '
                return s
        def get_last_node(n):
                current = n
                while (current.get_next()!= None):
                        current = current.get_next()
                return current
                
                
