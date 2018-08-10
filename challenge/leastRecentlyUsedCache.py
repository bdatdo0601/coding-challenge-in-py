class CacheItem(object):
    def __init__(self, key, prevItem):
        self.__key = key
        self.prev = prevItem
        self.next = None
    def getKey(self):
        return self.__key

class LRUCache(object):
    def __init__(self, n):
        self.limit = n
        self.count = 0
        self.head = None
        self.current = self.head
        self.cache = {}

    def setKeyValue(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            examiningKey = self.head.getKey()
            # move to the front of the list when it got used
            if (key == examiningKey):
                item = self.head
                if self.current is not None:
                    self.current.next = item
                self.current = item
                self.head = self.head.next
        else:
            if self.count >= self.limit:
                removingKey = self.head.getKey()
                self.head = self.head.next
                del self.cache[removingKey]
                self.count -= 1
            newCacheItem = CacheItem(key, self.current)
            if self.head is None:
                self.head = newCacheItem
                self.current = self.head
            else:
                self.current.next = newCacheItem
                self.current = self.current.next
            self.cache[key] = value
            self.count += 1

    def get(self, key):
        if key in self.cache:
            examiningKey = self.head.getKey()
            # move to the front of the list when it got used
            if (key == examiningKey):
                item = self.head
                self.current.next = item
                item.next = None
                self.head = self.head.next
            return self.cache[key]
        else:
            return None
