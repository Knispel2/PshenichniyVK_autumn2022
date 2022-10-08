from collections import deque

class lru_cache():

    def __init__(self, limit=42) -> None:
        self.base = deque()
        self.map = {}
        self.limit = limit
        self.counter = 0
    
    def upper_key(self, key):
        self.base.remove(key)
        self.base.append(key)

    def get(self, key):
        if key in self.base:
            self.upper_key(key)
            return self.map[key]
        else:
            return None

    def set(self, key, value):
        if len(self.base) == self.limit:
            buf = self.base.popleft()
            del self.map[buf]
        self.map[key] = value
        self.base.append(key)

