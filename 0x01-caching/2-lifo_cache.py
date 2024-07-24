#!/usr/bin/env python3
'''LIFO caching
'''
from base_caching import BaseCaching as base


class LIFOCache(base):
    '''implements LIFO caching
    '''
    # super().__init__()

    def put(self, key, item):
        '''puts a value in cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        keys = [key for key in self.cache_data.keys()]
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            key = keys.pop()
            self.cache_data.pop(key)
            print('DISCARD:', key)

    def get(self, key):
        '''retrieves a value associated with a key
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        return value
