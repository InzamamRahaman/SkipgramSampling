

from .sampler import Sampler
import torch
from torch.autograd import Variable

class PyTorchSampler(Sampler):
    def __init__(self, corpus, window_size):
        super(PyTorchSampler, self).__init__(corpus, window_size)

    def get_batch(self, batch_size=2, negative_samples=8):
        batch = super(PyTorchSampler, self).get_batch(batch_size, negative_samples)
        for (centre, target, negs) in batch:
            centre_variable = Variable(torch.LongTensor([centre]))
            target_variable = Variable(torch.LongTensor([target]))
            negs_variable = Variable(torch.LongTensor(negs))
            yield (centre_variable, target_variable, negs_variable)