import math
import numpy
import matplotlib.pyplot as plt

class TDHCumMean:
    def __init__(self, n_bins, low, high):
        self.reset(n_bins, low, high)

    def reset(self, n_bins, low, high):
        self._n_bins = n_bins
        self._bins = numpy.zeros(n_bins)
        self._low = low
        self._high = high
        self._n = 0

    def new_sample(self, t, x):
        if x <= self._low:
            n_bin = 0
        elif x > self._high:
            n_bin = self._n_bins - 1
        else:
            n_bin = math.ceil((x - self._low) / (self._high - self._low) * (self._n_bins - 2))
        self._n += 1
        self._bins[n_bin] += 1

    def merge(self, other):
        if self._n_bins != other._n_bins:
            print(type(self).__name__ + "merge(): self._nBins and other._nBins are unequal")
        for i in range(0, self._n_bins):
            self._bins[i] += (other._bins[i] / other._n)
        self._n += other._n

    def histogram(self):
        ranges = [[float("-inf"), self._low]]
        s = 0

        for i in range(0, len(self._bins)):
            s += self._bins[i]
        probabilities = [self._bins[0] / s]
        for i in range(1, self._n_bins - 1):
            ranges.append([self._low + (i - 1) / (self._n_bins - 2) * (self._high - self._low),
                           self._low + i / (self._n_bins - 2) * (self._high - self._low)])
            probabilities.append(self._bins[i] / s)
        ranges.append([self._high, float("+inf")])
        probabilities.append(self._bins[len(self._bins) - 1] / s)
        return ranges, probabilities

    def print_histogram(self):
        tmp = self.histogram()
        for i in range(0, len(tmp[0])):
            print(tmp[0][i], ": ", tmp[1][i])

    def get_quantile(self, prob):
        tmp = 0
        i = 0
        r, p = self.histogram()
        while tmp < prob and i < len(p):
            tmp += p[i]
            i += 1
        i = min(i, len(r) - 1)
        if tmp < prob:
            ret = r[i][1]
        else:
            ret = r[i][0]
        return ret

    def test(self, values):
        # minimum = float("inf")
        # maximum = float("-inf")
        # for i in range(0,len(values)):
        # minimum=min(minimum,values[i])
        # maximum=max(maximum,values[i])
        # self.reset(memory,5,minimum,maximum)
        for i in range(0, len(values)):
            self.new_sample(i, values[i])
        self.print_histogram()






class TDH_UTEMA(TDHCumMean):
    def __init__(self, n_bins, low, high, memory):
        self.reset(n_bins, low, high, memory)

    def reset(self, n_bins, low, high, memory):
        super(TDH_UTEMA, self).reset(n_bins, low, high)
        self._memory = memory
        self._beta = 1 / memory
        self._t_last = 0
        self._threshold = 10 * math.log(10) / -self._beta

    def normalize(self, t):
        tmp = math.exp(-self._beta * (t - self._t_last))
        for i in range(0, len(self._bins)):
            self._bins[i] *= tmp
        self._t_last = t

    def new_sample(self, t, x):
        if x <= self._low:
            n_bin = 0
        elif x > self._high:
            n_bin = self._n_bins - 1
        else:
            n_bin = math.ceil((x - self._low) / (self._high - self._low) * (self._n_bins - 2))

        if t - self._t_last > self._threshold:
            self.normalize(t)
        if self._n == 0:
            self._t_last = t

        tmp = math.exp(+self._beta * (t - self._t_last))
        self._n += tmp
        self._bins[n_bin] += tmp
        self._t_last = t

    def calculate_histogram(self, values):

        self.reset(self._n_bins, self._low, self._high, self._memory)
        for i in range(0, len(values)):
            self.new_sample(i, values[i])

        return self.histogram()

