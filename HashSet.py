class HashSet:
    def __init__(self, contents=[]):
        self.items = [None]*10
        self.numItems = 0

        for item in contents:
            self.add(item)

    # HashSet  Add Helper Function

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            # items already exists in the set
            if items[idx] == item:
                return False

            if loc < 0 and type(item[idx]) == HashSet.__Placeholder:
                loc = idx
            idx = (idx+1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True

    # <h1>Load Factor MGMT</h1>
    # HashSet Add

    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)
        return newList

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems/len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(
                    self.items, [None]*2*len(self.items))

    # Deleting an item form the HashSet
    # Since deleting an item from the middle of the set will mean a reduction in the set we replace it with a __Placeholder.
    # THis requires the need for a remove helper function

    # Remove Helper function
    class ___Placeholder:
        def ___init___(self):
            pass

        def __eq__(seld, other):
            return False

        def __remove(item, items):
            idx = hash(item) % len(items)

            while items(idx) != None:
                if items[idx] == item:
                    nextIdx = (idx+1) % len(item)
                    if items(nextIdx) == None:
                        items(idx) = None
                    else:
                        items[idx] = HashSet.___Placeholder()
                    return True
                idx = (idx+1) % len(items)
            return False

    # HashSet Remover Function
    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10)/len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(
                    self.items, [None]*int(len(self.items)/2))
            else:
                raise KeyError('Item not in the HashSet')

    # Finding Items in a HashSet
    # Means hashing  the item to find the address and
    # Then searching the possible chain of values

    # HashSet Membership

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx+1) % len(self.items)

        return False

    # Iterating over a set

    # We need to define the  __iter__ method  to yeild the elements of the set

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.___Placeholder:
                yield self.items[i]
