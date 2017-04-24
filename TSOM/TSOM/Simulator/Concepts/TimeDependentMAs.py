import math

from Simulator.TimeSeries import TimeSeries

from Simulator.LinearTimeFunction import LinearTimeFunction


class TimeDependentMovingAverage:
    def __init__(self, memory, t_start):
        self.reset(memory, t_start)
        self._granularity = 0.01

    def reset(self, memory, t_start):
        self._memory = memory
        self._t_start = t_start
        self._n = 0
        self._s = 0
        self._avg = 0
        self._additionalSamplingInstants = []

    def reset_average(self):
        self.reset(self._memory, self._t_start)


    def new_sample(self, t, x):
        self._avg = x

    def update(self, t):
        pass

    def get_average(self, t):
        self.update(t)
        return self._avg

    def add_sampling_instant(self, t):
        i = 0
        while i < len(self._additionalSamplingInstants) and self._additionalSamplingInstants[i] < t:
            i += 1
        self._additionalSamplingInstants.insert(i, t)

    # self._maxNumASI=max(self._maxNumASI,len(self._additionalSamplingInstants))

    def initialize_asi(self, t_stop):
        self.add_sampling_instant(t_stop)

    def update_asi_asi(self, t):
        pass

    def update_asi_sample_instant(self, t):
        pass

    def get_next_instant(self, t_stop, times, i):
        if i < len(times):
            tmp0 = times[i]
        else:
            tmp0 = t_stop + 1
        if self._additionalSamplingInstants:
            tmp1 = self._additionalSamplingInstants[0]
        else:
            tmp1 = t_stop + 1
        return min(tmp0, tmp1)

    def get_avg_ltf(self, t_stop, ts):
        avgs = TimeSeries()
        avgs.add(self._t_start, self._avg)
        self.initialize_asi(t_stop)
        i = 0
        next_instant = self.get_next_instant(t_stop, ts.t, i)

        while next_instant <= t_stop:

            if i < len(ts.t) and ts.t[i] == next_instant:
                self.new_sample(ts.t[i], ts.v[i])
                val = self.get_average(ts.t[i])
                self.update_asi_sample_instant(ts.t[i])
                i += 1
            elif self._additionalSamplingInstants and self._additionalSamplingInstants[0] == next_instant:
                self._additionalSamplingInstants.pop(0)
                val = self.get_average(next_instant)
                self.update_asi_asi(next_instant)
            else:
                print("This should not happen.")
            if len(avgs.t) > 0 and avgs.t[-1] == next_instant:
                avgs.v[-1] = val
            else:
                avgs.add(next_instant, val)
            next_instant = self.get_next_instant(t_stop, ts.t, i)
        return LinearTimeFunction.staircase_from_time_series(avgs)

    """
    def test(self, memory, t_start, t_stop):
        print(type(self).__name__)
        style = ['r-', 'g-', 'b-']
        for i in range(0, 3):
            self.reset(memory, t_start)
            ts = TimeSeries.from_files("samples" + str(i) + ".t", "samples.v")
            ltf = self.get_avg_ltf(t_stop, ts)
            plt.plot(ltf.t, ltf.v, style[i])
        plt.show()
    """

class TWMA(TimeDependentMovingAverage):

    def reset(self, memory, t_start):
        super(TWMA, self).reset(memory, t_start)
        self._w = memory
        self._times = []
        self._values = []

    def initialize_asi(self, t_stop):
        super(TWMA, self).initialize_asi(t_stop)
        delta = self._granularity * self._memory
        n = self._w / delta
        for i in range(1, math.ceil(n) + 1):
            self.add_sampling_instant(self._t_start + i * delta)

    def update_asi_sample_instant(self, t):
        self.add_sampling_instant(t + self._w)

    def update(self, t):
        while self._times != [] and (t - self._times[0]) >= self._w:
            self._times.pop(0)
            tmp = self._values.pop(0)
            self._s -= tmp
            self._n -= 1
        if self._n > 0:
            self._avg = self._s / self._n
        else:
            self._avg = 0

    def new_sample(self, t, x):
        self._values.append(x)
        self._times.append(t)
        self._s += x
        self._n += 1
        return self.get_average(t)


class DTWMA(TWMA):
    def reset(self, memory, t_start):
        super(DTWMA, self).reset(memory, t_start)
        self._t_last = t_start


    def initialize_asi(self, t_stop):
        self.add_sampling_instant(self._t_start + self._w)
        self.add_sampling_instant(t_stop)

    def update_asi_asi(self, t):
        self.add_sampling_instant(t + self._w)

    def update_asi_sample_instant(self, t):
        pass

    def update(self, t):
        while t >= self._t_last + self._w:
            self._t_last += self._w
            self._s = 0
            self._n = 0
            while self._times and self._times[0] <= self._t_last + self._w:
                self._times.pop(0)
                self._s += self._values.pop(0)
                self._n += 1
            if self._n > 0:
                self._avg = self._s / self._n
            else:
                self._avg = 0

    def new_sample(self, t, x):
        self._values.append(x)
        self._times.append(t)
        return self.get_average(t)


class UTEMA(TimeDependentMovingAverage):
    def reset(self, memory, t_start):
        super(UTEMA, self).reset(memory, t_start)
        self._beta = 1 / memory
        self._t_last = t_start

    # not needed because avg is zero until first sample
    # self.update_asi_asi(t_start)

    def update_asi_asi(self, t):
        delta = self._granularity / self._beta
        tmp = t + delta
        if len(self._additionalSamplingInstants) > 0:
            if self._additionalSamplingInstants[0] >= t + 2 * delta:
                self.add_sampling_instant(tmp)
        else:
            self.add_sampling_instant(tmp)

    def update_asi_sample_instant(self, t):
        self.update_asi_asi(t)

    def update(self, t):
        self._s *= math.exp(-self._beta * (t - self._t_last))
        self._n *= math.exp(-self._beta * (t - self._t_last))
        self._t_last = t
        if self._n > 0:
            self._avg = self._s / self._n
        else:
            self._avg = 0

    def new_sample(self, t, x):
        self.update(t)
        self._s += x
        self._n += 1

    def adapted_memory(self):
        # computes memory for UEMA so that it has the same devaluation speed as UTEMA
        return 1 / (1 - math.exp(-self._beta))


class TEMA(UTEMA):

    def update(self, t):
        self._avg = self._s

    def new_sample(self, t, x):
        if self._n == 0:
            self._s = x
            self._n = 1
        else:
            tmp = math.exp(-self._beta * (t - self._t_last))
            self._s *= tmp
            self._s += x * (1 - tmp)
        self._t_last = t
