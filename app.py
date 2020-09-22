
from collections import OrderedDict
 
class LruCache:
 
    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        
    def put(self, key: int, value: int) -> None: