#!/usr/bin/env python3
'''LRU caching
'''
from base_caching import BaseCaching as base


class LRUCache(base):
    '''implements LRU caching
    '''
    # super().__init__()
    visited = []

    def put(self, key, item):
        '''puts a value in cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.visited.remove(key)
        self.cache_data[key] = item
        self.visited.append(key)
        # keys = [key for key in self.cache_data.keys()]
        if len(self.cache_data) > self.MAX_ITEMS:
            key = self.visited.pop(0)
            self.cache_data.pop(key)
            print('DISCARD:', key)

    def get(self, key):
        '''retrieves a value associated with a key from cache
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        self.visited.remove(key)
        self.visited.append(key)
        return value
