import math

from Simulator.Concepts.MAs import EMA, UEMA
from Simulator.Concepts.TimeDependentMAs import TimeDependentMovingAverage, TWMA, DTWMA, UTEMA
from Simulator.LinearTimeFunction import LinearTimeFunction


class TimeDependentRateMeasurement(TimeDependentMovingAverage):

    def get_time_interval(self, t):
        return 1

    def get_rate(self, t):
        self.update(t)
        if self._s > 0:
            time_interval = self.get_time_interval(t)
            if time_interval > 0:
                return self._s / time_interval
            else:
                return 0
        else:
            return 0

    def get_rate_ltf(self, t_stop, ts):
        rate_ltf = LinearTimeFunction()
        rate_ltf.add(self._t_start, self.get_rate(self._t_start))
        self.initialize_asi(t_stop)
        i = 0
        next_instant = self.get_next_instant(t_stop, ts.t, i)

        while next_instant <= t_stop:
            if i < len(ts.t) and ts.t[i] == next_instant:
                self.new_sample(ts.t[i], ts.v[i])
                val = self.get_rate(ts.t[i])
                self.update_asi_sample_instant(ts.t[i])
                i += 1
            elif self._additionalSamplingInstants:
                self._additionalSamplingInstants.pop(0)
                val = self.get_rate(next_instant)
                self.update_asi_asi(next_instant)
            else:
                print("This should not happen.")
            rate_ltf.add(next_instant, val)
            next_instant = self.get_next_instant(t_stop, ts.t, i)
        return LinearTimeFunction.staircase_from_time_series(rate_ltf)

    """
    def test_rates_times(self, memory, t_start, t_stop):
        print(type(self).__name__ + ": time experiment")
        line_style = ['r-', 'g-', 'b-', 'k-']
        for i in range(0, 3):
            self.reset(memory, t_start)
            ts = TimeSeries.from_time_file("samples" + str(i) + ".t")
            rate_ltf = self.get_rate_ltf(t_stop, ts)
            plt.plot(rate_ltf.t, rate_ltf.v, line_style[i])
        plt.show()

    def test_rates_memories(self, memories, t_start, t_stop):
        print(type(self).__name__ + ": memory experiment")
        line_style = ["r-", "g-", "b-", "k-"]
        ts = TimeSeries.from_time_file("samples.t")
        print("investigated memories=", memories)
        for i in range(0, len(memories)):
            self.reset(memories[i], t_start)
            rate_ltf = self.get_rate_ltf(t_stop, ts)
            plt.plot(rate_ltf.t, rate_ltf.v, line_style[i])
        plt.show()
    """

class TDRMCumMean(TimeDependentRateMeasurement):

    def reset(self, memory, t_start):
        super(TDRMCumMean, self).reset(memory, t_start)

    def update_asi_asi(self, t):
        delta = self._granularity * self._memory
        tmp = t + delta
        if len(self._additionalSamplingInstants) > 0:
            if self._additionalSamplingInstants[0] >= t + 2 * delta:
                self.add_sampling_instant(tmp)
        else:
            self.add_sampling_instant(tmp)

    def update_asi_sample_instant(self, t):
        self.update_asi_asi(t)

    def get_time_interval(self, t):
        return t - self._t_start

    def new_sample(self, t, x):
        self._s += x
        self._n += 1



class TDRM_TWMA(TWMA, TimeDependentRateMeasurement):
    def get_time_interval(self, t):
        return min(t - self._t_start, self._w)


class TDRM_DTWMA(DTWMA, TimeDependentRateMeasurement):
    def get_time_interval(self, t):
        return self._w

class TDRM_UTEMA(UTEMA, TimeDependentRateMeasurement):
    def get_time_interval(self, t):
        return (1 - math.exp(-self._beta * (t - self._t_start))) / self._beta

    def get_rate_ltf(self, t_stop, ts):
        rate_ltf = LinearTimeFunction()
        rate_ltf.add(self._t_start, self.get_rate(self._t_start))
        self.initialize_asi(t_stop)
        i = 0
        next_instant = self.get_next_instant(t_stop, ts.t, i)

        while next_instant <= t_stop:
            if i < len(ts.t) and ts.t[i] == next_instant:
                self.new_sample(ts.t[i], 0)
                rate_ltf.add(next_instant, self.get_rate(ts.t[i]))
                self.new_sample(ts.t[i], ts.v[i])
                val = self.get_rate(ts.t[i])
                self.update_asi_sample_instant(ts.t[i])
                i += 1
            elif self._additionalSamplingInstants:
                self._additionalSamplingInstants.pop(0)
                val = self.get_rate(next_instant)
                self.update_asi_asi(next_instant)
            else:
                print("This should not happen.")
            rate_ltf.add(next_instant, val)
            next_instant = self.get_next_instant(t_stop, ts.t, i)
        return rate_ltf


class TDRM_UTEMA_CPA(TimeDependentRateMeasurement):
    # only for rate measurement, not for moving average

    def __init__(self, memory, t_start):
        super(TDRM_UTEMA_CPA, self).__init__(memory, t_start)
        self.reset(memory, t_start)

    def reset(self, memory, t_start):
        super(TDRM_UTEMA_CPA, self).reset(memory, t_start)
        self._beta = 1 / memory
        self._t_last = t_start

    def new_sample(self, t, X):
        if self._n == 0:
            self._s = X / (t - self._t_start)
            self._s += 1
        else:
            tmp = math.exp(-self._beta * (t - self._t_last))
            self._s *= tmp
            if (t - self._t_last) < 2 ** -149:
                print(t, self._t_last, t - self._t_last)
            self._s += (1 - tmp) * X / (t - self._t_last)
        self._t_last = t

    def get_rate(self, t):
        return self._s

    def get_average(self, t):
        print(type(self).__name__ + ".get_average(t) not available")
        return 0


class TDRM_DTWMA_UEMA(TDRM_DTWMA):
    # only for rate measurement, not for moving average

    def __init__(self, memory, t_start, w):
        self._w = w
        super(TDRM_DTWMA_UEMA, self).__init__(w, t_start)
        self.reset_w(memory, t_start, w)

    def reset_w(self, memory, t_start, w):

        super(TDRM_DTWMA_UEMA, self).reset(w, t_start)
        a = 1 - self._w / memory
        ma_memory = 1 / (1 - a)
        self._ma = UEMA(ma_memory)
        self._memory = memory #!!!!!!!!!!!!!!!!

    def reset(self, memory, t_start):
        self.reset_w(memory, t_start, self._w)

    def update(self, t):
        while t >= self._t_last + self._w:
            self._t_last += self._w
            self._s = 0
            while self._times and self._times[0] <= self._t_last + self._w:
                self._times.pop(0)
                self._s += self._values.pop(0)
            self._ma.new_sample(self._s / self._w)

    def new_sample(self, t, x):
        self._values.append(x)
        self._times.append(t)

    def get_rate(self, t):
        self.update(t)
        return self._ma.get_average()

    def get_average(self, t):
        print(type(self).__name__ + ".get_average(t) not available")
        return 0


class TDRM_DTWMA_EMA(TDRM_DTWMA_UEMA):
    # only for rate measurement, not for moving average

    def reset_w(self, memory, t_start, w):
        # super(TDRM_DTWMA_UEMA) used instead of super(TDRM_DTWMA_EMA) to avoid loops
        super(TDRM_DTWMA_UEMA, self).reset(w, t_start)
        a = 1 - self._w / memory
        ma_memory = 1 / (1 - a)
        self._ma = EMA(ma_memory)
        self._memory = memory #!!!!!!!!!!!

