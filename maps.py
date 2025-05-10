'''A private __KVPair class is defined. Instances
of __KVPair hold the key/value pairs as they are added to the HashMap object.With
the addition of a __getitem__ method on the HashSet class, the HashSet class could
be used for the HashMap class implementation.'''

from HashSet import HashSet

# Hashset getItem()


def __getItem__(self, item):
    idx = hash(item) % len(self.items)
    while self.items[idx] != None:
        if self.items[idx] == item:
            return self.items[idx]

        idx = (idx+1) % len(self.items)
    return None

# THe HashMap Class


class HashMap:
    class __KVPair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if tyepe(self) != type(other):
                return False

            return self.key == other.key

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def __hash__(self):
            return hash(self.key)

    def __init__(self):
        self.hSet = hashset.HashSet()

    def __len__(self):
        return len(self.hSet)

    def __contains__(self, item):
        return HashSet.__KVPair(item, None) in self.hSet

    def not__contains__(self, item):
        return item not in self.hSet

    def __setItem__(self, key, value):
        self.hSet.add(HashMap.__KVPair(key, value))

    def __getItem__(self, key):
        if HashMap.__KVPair(key, None) in self.hSet:
            val = self.hSet[HashMap.__KVPair(key, None)].getValue()
            return val
        raise KeyError("key" + str(key) + "not in HashMap")

    def __iter__(self):
        for x in self.hSet:
            yield x.getKey()
