import random
from Simulator.Counter.Counter import TIC
import numpy as np

class RandomProcess:

    def reset(self, s, mean):
        random.seed(s)
        self._s = s
        self._mean = mean
        self._tic = TIC()

    def get_rv(self):
        pass

    def test_rv(self, n):
        self._tic.reset()
        X = []
        for i in range(0, n):
            X.append(self.get_rv())
        print(n, " random variables of ", type(self).__name__, " with configured mean=", self._mean)
        print("E=", self._tic.mean(), " cvar=", self._tic.cvar())
        # print("values=", X)




class AutoregressiveProcess(RandomProcess):
    # autoregressive process of order 3

    def reset(self, s, mean, off0, off1, off2, phi1, phi2, phi3):
        super(AutoregressiveProcess, self).reset(s, mean)
        self._mean = mean
        self._off = [off0, off1, off2, 0]
        self._phi = [phi1, phi2, phi3]
        self._k = -1

    def get_rv(self):
        self._k += 1
        off_len = len(self._off)
        if self._k > 2:
            tmp = 0
            for i in range(0, len(self._phi)):
                tmp += self._phi[i] * (self._off[(self._k - i - 1) % off_len])
            tmp += random.gauss(0, 1)
            self._off[self._k % off_len] = tmp
        v = self._mean + self._off[self._k % off_len]
        self._tic.new_sample(v)
        return v



class ArrivalProcess(RandomProcess):
    def reset(self, s, mean, t_start):
        super(ArrivalProcess, self).reset(s, mean)
        self._t_start = t_start
        self._t_last = t_start

    def next_sample(self):
        self._t_last += self.get_rv()
        return self._t_last

    def get_time_vector(self, t_stop, time_shift=0):
        self.reset(self._s, self._mean, self._t_start)
        t = []
        while self._t_last < t_stop:
            t.append(self.next_sample())
        print(type(self).__name__, ".get_time_vector: E=", self._tic.mean(), " cvar=", self._tic.cvar(), " t_start=",
              self._t_start, " t_stop=", t_stop)
        t = [t +time_shift for t in t]
        return t

    def get_time_vector_from_length(self, vector_length, time_shift=0):
        t = []
        while len(t) < vector_length:
            t.append(self.next_sample())
        print(type(self).__name__, ".get_time_vector: E=", self._tic.mean(), " cvar=", self._tic.cvar(), " t_start=",
              self._t_start, " t_last=", self._t_last)
        t = [t+time_shift for t in t]
        return t

class PoissonArrivalProcess(ArrivalProcess):
    def __init__(self, s, mean, t_start):
        super(PoissonArrivalProcess, self).reset(s, mean, t_start)

    def get_rv(self):
        tmp = random.expovariate(1 / self._mean)
        self._tic.new_sample(tmp)
        return tmp


class GammaArrivalProcess(ArrivalProcess):
    def __init__(self, s, mean, t_start, cvar):

        super(GammaArrivalProcess, self).reset(s, mean, t_start)
        self._cvar = cvar
        self._alpha = 1.0 / (cvar * cvar)
        self._beta = mean / self._alpha


    def get_rv(self):
        tmp = random.gammavariate(self._alpha, self._beta)
        if tmp < 10 ** -10:
            tmp = 10 ** -10
        self._tic.new_sample(tmp)
        return tmp

class SampleSizeProcess(RandomProcess):
    def reset(self, s, mean):
        super(SampleSizeProcess, self).reset(s, mean)

    def next_sample(self):
        return self.get_rv()

    def get_sample_vector_from_length(self, vector_length):
        v = []
        while len(v) < vector_length:
            v.append(self.next_sample())
        print(type(self).__name__, ".get_sample_vector: E=", self._tic.mean(), " cvar=", self._tic.cvar())
        return v

class ExponentialSampleSizeProcess(SampleSizeProcess):
    def __init__(self, s, mean):
        super(ExponentialSampleSizeProcess, self).reset(s, mean)

    def get_rv(self):
        tmp = random.expovariate(1.0 / self._mean)
        if tmp < 10 ** -10:
            tmp = 10 ** -10
        self._tic.new_sample(tmp)
        return tmp

class UniformSampleSizeProcess(SampleSizeProcess):
    def __init__(self, s, low, high):
        super(UniformSampleSizeProcess, self).reset(s, (low+high)/2)
        self._low = low
        self._high = high

    def get_rv(self):
        tmp = np.random.uniform(self._low, self._high)
        self._tic.new_sample(tmp)
        return tmp

class BinomialSampleSizeProcess(SampleSizeProcess):
    def __init__(self, s, n, p):
        super(BinomialSampleSizeProcess, self).reset(s, n*p)
        self._n = n
        self._p = p

    def get_rv(self):
        tmp = np.random.binomial(self._n, self._p, 1)[0]
        self._tic.new_sample(tmp)
        return tmp




