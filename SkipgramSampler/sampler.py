
import numpy as np

import random

from .vocab import Vocabulary

from .unigram import UnigramDistribution

class Sampler(object):

    def __init__(self, corpus, window_size):
        self.vocab = Vocabulary(corpus, window_size)
        self.n = len(self.vocab)

        def mapping_func(x):
            return self.vocab.id2word(x)

        self.noise_distribution = UnigramDistribution(self.n, self.vocab.frequencies, mapping_func)

    def sample_word(self):
        idx = np.random.randint(1, self.n + 1)
        return idx

    def sample_neighbor(self, centre_word_idx):
        neighbors = self.vocab.get_neighbors_ids(centre_word_idx)
        elem = random.sample(neighbors, 1)[0]
        return elem

    def sample_negative_words(self, centre_word_idx, num=1):
        avoid = set()
        avoid.add(centre_word_idx)
        arr = self.noise_distribution.sample(num=num, avoid=avoid, with_replacement=False)
        return arr

    def batch_sample(self, batch_size=2, negative_samples=8):
        arr = []
        for i in range(batch_size):
            centre_word_idx = self.sample_word()
            neighbor = self.sample_neighbor(centre_word_idx)
            negatives = self.sample_negative_words(centre_word_idx, negative_samples)
            arr.append((centre_word_idx, neighbor, negatives))
        return arr

    def get_batch(self, batch_size=2, negative_samples=8):
        for batch_num in range(batch_size):
            centre_word_index = self.sample_word()
            target_word_index = self.sample_neighbor(centre_word_index)
            negative_target_indicies = self.sample_negative_words(centre_word_index, num=negative_samples)
            yield (centre_word_index, target_word_index, negative_target_indicies)


    def get_pairs(self, negative_samples=8):
        for centre_word_idx, neighbor in self.vocab.get_pairs():
            negatives = self.sample_negative_words(centre_word_idx, negative_samples)
            yield (centre_word_idx, neighbor, negatives)






