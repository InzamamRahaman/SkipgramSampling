
from collections import defaultdict
from fixedarray import FixedArray


class Vocabulary(object):

    def __init__(self, contents, window_size=8):
        self.id2word = dict()
        self.word2id = dict()
        self.neighbors = defaultdict(set)
        self.count = 0
        self.frequencies = defaultdict(int)
        self.array = FixedArray(window_size)
        self.words = set()

        def neighbors_callback(y, x, arr):
            self.neighbors[y].add(x)
            self.neighbors[x].add(y)

        print('Processing')
        for idx, word in enumerate(contents):
            if word not in self.words:
                self.id2word[id] = word
                self.word2id[word] = id
                self.count += 1
                self.words.add(word)
            self.frequencies[word] += 1
            self.array.append(word, neighbors_callback)

    def id2word(self, id):
        return self.id2word[id]

    def word2id(self, word):
        return self.word2id[word]

    def get_neighbors(self, word):
        return self.neighbors[word]

    def __len__(self):
        return self.count



