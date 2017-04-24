import math


class TIC:
    # TimeIndependentCounter

    def __init__(self):
        self.reset()

    def reset(self):
        self._n = 0
        self._e1 = 0
        self._e2 = 0

    def new_sample(self, x):
        self._n += 1
        self._e1 += x
        self._e2 += x * x

    def mean(self):
        return self._e1 / self._n

    def s2(self):
        return self._n / (self._n - 1) * (self._e2 / self._n - self.mean() ** 2)

    def stdev(self):
        return math.sqrt(self.s2())

    def cvar(self):
        if self.mean() > 0:
            return self.stdev() / self.mean()
        else:
            return 0

    @staticmethod
    def from_vector(v):
        tic = TIC()
        for i in v:
            tic.new_sample(i)
        return tic


class TDC:
    # TimeDependentCounter

    def __init__(self):
        self.reset(0, 0)

    def reset(self, t, X):
        self._t_last = t
        self._x_last = X
        self._e1 = 0
        self._e2 = 0
        self._duration = 0

    def new_sample(self, t, x):
        self._e1 += self._x_last * (t - self._t_last)
        self._e2 += self._x_last * self._x_last * (t - self._t_last)
        self._duration += (t - self._t_last)
        self._t_last = t
        self._x_last = x

    def mean(self):
        return self._e1 / self._duration

    def s2(self):
        return (self._e2 / self._duration) - self.mean() * self.mean()

    def stdev(self):
        if self.s2() >= 0:
            return math.sqrt(self.s2())
        else:
            return 0

    def cvar(self):
        if self.mean() > 0:
            return self.stdev() / self.mean()
        else:
            return 0

    def read_time_series(self, ts):
        if len(ts.t) > 1:
            self.reset(ts.t[0], ts.v[0])
            for i in range(1, len(ts.t)):
                self.new_sample(ts.t[i], ts.v[i])
        else:
            self.reset(0, 0)

    def read_linear_time_function(self, ltf):
        self.reset(0, 0)
        for i in range(1, len(ltf.t)):
            d = ltf.t[i] - ltf.t[i - 1]
            self._duration += d
            if d > 0:
                a = ltf.v[i - 1]
                b = (ltf.v[i] - ltf.v[i - 1]) / d
                self._e1 += d * (a + d * b / 2)
                self._e2 += d * (a * a + d * (a * b + d * b * b / 3))