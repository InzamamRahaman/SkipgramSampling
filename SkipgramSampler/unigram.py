import numpy as np


class UnigramDistribution(object):

    def __init__(self, vocab_size, frequencies, mapping_func=None, alpha=0.75):
        """

        Parameters
        ----------
        vocab_size: int
            The number of elements in the vocabulary
        frequencies: dict of Any to int
            A dictionary indicating the frequencies of each element of the vocabulary
            in the original corpus. Note that this provides a mapping from
            word id to number of occurrences
        mapping_func: func of int to Any or None, optional (default is None)
            A function that takes an id (i.e. an int) and returns the corresponding
            object from our vocabulary. Note that the type returned here must match the
            type accepted by the dictionary. If None is provided, then we assume that
            frequencies provides a direct mapping from word id to frequency
        alpha: float, optional, default is 0.75
            The exponent to which the frequencies are raised
        """
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
        """
        Samples from this unigram distribution
        Parameters
        ----------
        num: int, optional
            The number of elements to sample from this distribution (default is 1)
        with_replacement: bool, optional
            Whether sampling from this distribution should be done with or without replacement,
            (default is False)

        Returns
        -------
            iterable{int}
            The indicies/ids of the randomly selected elements
        """
        selected = np.random.choice(self.vocab_size + 1, num, p=self.probs, replace=with_replacement)
        if num == 1:
            selected = selected[0]
        return selected

