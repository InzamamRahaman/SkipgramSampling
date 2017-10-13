
from vocab import Vocabulary

class Sampler(object):

    def __init__(self, corpus, window_size):
        self.vocab = Vocabulary(corpus, window_size)

    def sample_word(self):
        pass

    def sample_neighbor(self, centre_word):
        pass

    def sample_negative_word(self, centre_word):
        actual_neighbors = self.sample_neighbor(centre_word)
        pass