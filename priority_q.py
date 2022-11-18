from node import node
from linkedList import linkedList
class priority_q:
        def __init__(self):
                self.q = linkedList()
        def put(self, key, value):
                self.q.put(key,value)
        def remove_max(self):
                current = self.q.head
                c = current.get_next()
                m = current.get_next()
                while (current.get_next()!=None):
                        current = current.get_next()
                        #print (m.get_key().get_id(), current.get_key().get_id())
                        if (m.get_value()<current.get_value()):
                                m = current
                                c = current
                self.q.remove(c.get_key())
                return c.get_key()
        def update(self, key, value):
                current = self.q.head.get_next()
                while current!= None:
                        if (current.get_key() == key):
                                current.set_value(value)
                                return True
                        current = current.get_next()
                return False
        def get(self, key):
                current = self.q.head.get_next()
                while current!= None:
                        if (current.get_key() == key):
                                return current.get_value()
                        current = current.get_next()
                return None
                
        def __repr__(self):
                s = ''
                current = self.q.head.get_next()
                while (current!=None):
                        str_k = str(current.get_key().get_id())
                        str_v = str(current.get_value())
                        s+="(" + str_k + ',' + str_v + ")"
                        current = current.get_next()
                return s
        def is_empty(self):
                if self.q.is_empty():
                        return True
                return False
        def get_keys(self):
                current  = self.q.head.get_next()
                outcome = []
                while current!= None:
                        outcome.append(current.get_key())
                        current = current.get_next()
                return outcome
                                
                        
                        
                
                        
                                
                                
                
                
