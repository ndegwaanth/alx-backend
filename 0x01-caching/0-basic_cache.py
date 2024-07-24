#!/usr/bin/env python3
'''basic dictionary caching strategy
'''
from base_caching import BaseCaching as cache


class BasicCache(cache):
    '''implements a cache using a plain old dict
    '''
    def put(self, key, item):
        '''adds an item in the cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
