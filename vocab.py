
from collections import defaultdict
from fixedarray import FixedArray


class Vocabulary(object):

    def __init__(self, contents, window_size=8):
        self.id2word = dict()
        self.word2id = dict()
        self.neighbors = defaultdict(set)
        self.neighbors_ids = defaultdict(set)
        self.count = 0
        self.frequencies = defaultdict(int)
        self.array = FixedArray(window_size)
        self.words = set()

        def neighbors_callback(y, x, arr):
            self.neighbors[y].add(x)
            self.neighbors[x].add(y)
            it = arr.get_distinct_elements()
            for i in it:
                self.neighbors[y].add(i)
                self.neighbors[x].add(i)

        for idx, word in enumerate(contents):
            if word not in self.words:
                self.id2word[self.count + 1] = word
                self.word2id[word] = self.count + 1
                self.count += 1
                self.words.add(word)
            self.frequencies[word] += 1
            self.array.append(word, neighbors_callback)

    def id2word(self, id):
        return self.id2word[id]

    def word2id(self, word):
        return self.word2id[word]

    def get_neighbors(self, word):
        if isinstance(word, int):
            return self.neighbors[self.id2word[word]]
        return self.neighbors[word]

    def get_neighbors_ids(self, word):
        if isinstance(word, int):
            word = self.id2word[word]
        if word not in self.neighbors_ids:
            arr = set()
            neighbors = self.get_neighbors(word)
            for neighbor in neighbors:
                arr.add(self.word2id[neighbor])
            self.neighbors_ids[word] = arr
        return self.neighbors_ids[word]


    def __len__(self):
        return self.count


