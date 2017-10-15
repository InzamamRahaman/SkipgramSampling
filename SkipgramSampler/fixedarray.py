from collections import deque

class FixedArray(object):
    """
    Object acts a queue of fixed length
    """

    def __init__(self, limit):
        self.count = 0
        self.limit = limit
        self.contents = deque()

    def append(self, x, callback=None):
        if self.count < self.limit:
            self.contents.append(x)
            self.count += 1
        else:
            elem = self.contents.popleft()
            if callback:
                callback(elem, x, self)
            self.contents.append(x)
            self.count += 1

    def __contains__(self, item):
        item in self.contents

    def __len__(self):
        return self.count

    def get_distinct_elements(self):
        return set(self.contents)

    def empty_contents(self):
        for i in range(self.count):
            print('Pop')
            self.contents.popleft()
            print(self.contents)


