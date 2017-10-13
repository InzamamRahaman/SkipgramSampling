
import numpy as np

import random

from vocab import Vocabulary

class Sampler(object):

    def __init__(self, corpus, window_size):
        self.vocab = Vocabulary(corpus, window_size)
        self.n = len(self.vocab)

    def sample_word(self):
        idx = np.random.randint(1, self.n + 1)
        return idx

    def sample_neighbor(self, centre_word_idx):
        neighbors = self.vocab.get_neighbors_ids(centre_word_idx)
        elem = random.sample(neighbors, 1)[0]
        return elem

    def sample_negative_words(self, centre_word_idx, num=1):
        arr = []
        count = 0
        neighbors = self.vocab.get_neighbors_ids(centre_word_idx)
        while count < num:
            jdx = np.random.randint(1, self.n + 1)
            while jdx in neighbors or jdx == centre_word_idx:
                jdx = np.random.randint(1, self.n + 1)
            arr.append(jdx)
            count += 1
        return arr

    def batch_sample(self, batch_size=2, negative_samples=8):
        arr = []
        for i in range(batch_size):
            centre_word_idx = self.sample_word()
            neighbor = self.sample_neighbor(centre_word_idx)
            negatives = self.sample_negative_words(centre_word_idx, negative_samples)
            arr.append((centre_word_idx, neighbor, negatives))
        return arr