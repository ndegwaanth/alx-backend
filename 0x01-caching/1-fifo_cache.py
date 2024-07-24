#!/usr/bin/env python3
'''FIFO caching
'''
from base_caching import BaseCaching as base


class FIFOCache(base):
    '''implements FIFO caching
    '''
    # super().__init__()

    def put(self, key, item):
        '''puts a key-value in cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = item
        keys = [key for key in self.cache_data.keys()]
        if len(keys) > self.MAX_ITEMS:
            key = keys.pop(0)
            self.cache_data.pop(key)
            print('DISCARD:', key)

    def get(self, key):
        '''retrieves value of key in cache
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)
        return value
