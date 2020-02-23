from collections import OrderedDict

from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        # self.storage = {}
        self.storage = OrderedDict({"key": "Shelbs", "keyy": 18, "rebeccapurple": "color"})

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.dll.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
# add to cache
# move to front
# IF MAX CAPACITY - remove tail and add to head
# if key exists, re-assign new value
# def set(self, key, value):
#     if key in self.storage: # Key/Value exists
#         self.storage[key] = value # Overwrite
#         self.dll.move_to_front(self.storage[key]) # Set key/value as head
#         return
#     if self.size == self.limit: # if MAX CAPACITY is reached
#         self.storage.popitem(last=True) #remove tail
#         self.size -= 1 # adjust size after pop
#     self.storage[key] = value # add node to dict
#     self.size += 1 # adjust size after adding new node
#     self.storage.move_to_end(key, False) # move newly added node to head
#     return self.storage
# check and see if key is in cache
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            return
        # If it is int he cache move to front and update value
        if self.size == self.limit:
            del self.storage[self.dll.head.value[0]]  # deletes first item in tuple - (key value) pair
            self.dll.remove_from_head()
            self.size -= 1
# If not Add to the front of the cache
# Defining tail as most recent and head as oldest
self.dll.add_to_tail((key, value))
self.storage[key] = self.dll.tail
self.size += 1

test = LRUCache()
# print(test.get("keyy"))
print(test.set('k', 'v'))
