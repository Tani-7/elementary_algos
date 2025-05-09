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
