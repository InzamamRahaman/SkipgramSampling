from collections import defaultdict, Counter, Iterable
from .fixedarray import FixedArray


class Vocabulary(object):
    def __init__(self, contents, window_size=8):
        """
        Accepts a tokenized document or sequence of tokenized documents and assembles a Vocabulary object
        Parameters
        ----------
        contents list of str or list of list of str:
            A document or sequence of documents tokenized. The vocabulary is constructed from these
        window_size int:
            The window size of the context for skipgram
        """
        self._id2word = dict()
        self._word2id = dict()
        self.neighbors = defaultdict(set)
        self.neighbors_ids = defaultdict(set)
        self.count = 0
        self.frequencies = defaultdict(int)
        self.words = set()
        self.frequencies = defaultdict(int)

        def neighbors_callback(y, x, arr):
            self.neighbors[y].add(x)
            self.neighbors[x].add(y)
            it = arr.get_distinct_elements()
            for i in it:
                self.neighbors[y].add(i)
                self.neighbors[x].add(i)

        if not (isinstance(contents[0], Iterable)):
            contents = [contents]

        for doc in contents:
            arr = FixedArray(window_size)
            for idx, word in enumerate(doc):
                if word not in self.words:
                    self._id2word[self.count + 1] = word
                    self._word2id[word] = self.count + 1
                    self.count += 1
                    self.words.add(word)
                self.frequencies[word] += 1
                arr.append(word, neighbors_callback)

    def id2word(self, word_id):
        return self._id2word[word_id]

    def get_pairs(self):
        for word_id in range(1, self.count + 1):
            neighbours = self.get_neighbors_ids(word_id)
            for neighbour in neighbours:
                yield (word_id, neighbour)


    def word2id(self, word):
        return self._word2id[word]

    def get_neighbors(self, word):
        if isinstance(word, int):
            return self.neighbors[self._id2word[word]]
        return self.neighbors[word]

    def get_neighbors_ids(self, word):
        """
        Gets the ids of the words within the context window of the word/id supplied as argument
        Parameters
        ----------
        word int or str:
            int - the id of the center word
            str - the center word

        Returns
        -------
        set of int
        A set containing the ids of the context words

        """
        if isinstance(word, int):
            word = self._id2word[word]
        if word not in self.neighbors_ids:
            arr = set()
            neighbors = self.get_neighbors(word)
            for neighbor in neighbors:
                arr.add(self._word2id[neighbor])
            self.neighbors_ids[word] = arr
        return self.neighbors_ids[word]

    def __len__(self):
        return self.count
