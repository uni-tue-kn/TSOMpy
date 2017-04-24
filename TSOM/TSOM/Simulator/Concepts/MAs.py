import math

from Simulator.TimeSeries import TimeSeries

from Simulator.LinearTimeFunction import LinearTimeFunction


class MovingAverage:
    # computed average is only a dummy function returning last sampled value

    def __init__(self, memory):
        self.reset(memory)

    def reset(self, memory):
        self._memory = memory
        self._avg = 0

    def reset_average(self):
        self.reset(self._memory)

    def new_sample(self, x):
        self._avg = x

    def get_average(self):
        return self._avg

    def get_avg_time_series(self, ts):
        avgs = TimeSeries()
        for i in range(0, len(ts.v)):
            self.new_sample(ts.v[i])
            avgs.add(ts.t[i], self.get_average())
        return avgs

    def get_avg_ltf(self, ts):
        avgts = self.get_avg_time_series(ts)
        ltf = LinearTimeFunction.staircase_from_time_series(avgts)
        ltf.add(ltf.t[-1] + 1, ltf.v[-1])
        return ltf

    """
    def test(self, memory, ts):
        print(type(self).__name__)
        self.reset(memory)
        ltf = self.get_avg_ltf(ts)
        plt.plot(ltf.t, ltf.v)
        plt.show()
    """

class CumMean(MovingAverage):
    # memory is unused

    def reset(self, memory):
        super(CumMean, self).reset(memory)
        self._s = 0
        self._n = 0

    def new_sample(self, x):
        self._s += x
        self._n += 1
        if self._n == 0:
            self._avg = 0
        else:
            self._avg = self._s / self._n


class DWMA(CumMean):

    def reset(self, memory):
        super(DWMA, self).reset(memory)
        self._w = memory

    def new_sample(self, x):
        self._s += x
        self._n += 1
        if self._n >= self._w:
            self._avg = self._s / self._n
            self._n = 0
            self._s = 0


class WMA(DWMA):
    def reset(self, memory):
        super(WMA, self).reset(memory)
        self._values = []

    def new_sample(self, x):
        self._values.append(x)
        if self._n < self._w:
            self._s += x
            self._n += 1
        else:
            tmp = self._values.pop(0)
            self._s += (x - tmp)
        self._avg = self._s / self._n


class EMA(CumMean):
    def reset(self, memory):
        super(EMA, self).reset(memory)
        self._a = 1 - 1 / (1.0 * memory)

    def new_sample(self, x):
        if self._n == 0:
            self._avg = x
        else:
            self._avg = self._a * self._avg + (1 - self._a) * x
        self._n += 1


class UEMA(EMA):

    def new_sample(self, x):
        self._s = self._a * self._s + x
        self._n = self._a * self._n + 1
        self._avg = self._s / self._n

    def adapted_memory(self):
        # computes memory for UTEMA so that it has the same devaluation speed as UEMA
        return 1 / (-math.log(self._a))