#!/usr/bin/env python3
'''LFU caching system
'''
from base_caching import BaseCaching as base


class LFUCache(base):
    '''implements LFU caching
    '''
    tracker = {}

    def put(self, key, item):
        '''puts a value in cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.tracker[key] += 1
        self.cache_data[key] = item
        if key not in self.tracker.keys():
            self.tracker[key] = 1
        if len(self.cache_data) > self.MAX_ITEMS:
            # sort tracker using values
            sorted_tupple = sorted(self.tracker.items(), key=lambda x: x[1])
            sort_tracker = {}
            for v in sorted_tupple:
                sort_tracker[v[0]] = v[1]
            for _ in range(1):
                for k, v in sort_tracker.items():
                    '''remove the key with least frequency except inserted key
                    '''
                    if k == key:
                        continue
                    # print(sort_tracker)
                    del self.cache_data[k]
                    del self.tracker[k]
                    print("DISCARD:", k)
                    break

    def get(self, key):
        '''retrieves a value associated with a key from cache
        '''
        if key is None or key not in self.cache_data.keys():
            return None
        val = self.cache_data.get(key)
        self.tracker[key] += 1
        return val
