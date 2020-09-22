
from collections import OrderedDict
 
class LruCache:
 
    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
       