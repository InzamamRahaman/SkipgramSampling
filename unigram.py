import numpy as np


class UnigramDistribution(object):

    def __init__(self, vocab_size, frequencies, mapping_func=None, alpha=0.75):
        self.probs = np.zeros(vocab_size + 1)
        self.vocab_size = vocab_size
        for i in range(1, vocab_size + 1):
            elem = i
            if mapping_func:
                elem = mapping_func(i)
            self.probs[i] = frequencies[elem]
        self.probs = np.power(self.probs, alpha)
        normalizing_const = np.sum(self.probs)
        self.probs /= normalizing_const

    def sample(self, num=1, with_replacement=False):
        selected = np.random.choice(self.vocab_size + 1, num, p=self.probs, replace=with_replacement)
        if num == 1:
            selected = selected[0]
        return selected

