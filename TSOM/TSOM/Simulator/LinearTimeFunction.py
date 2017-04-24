import math

from Simulator.TimeSeries import TimeSeries


class LinearTimeFunction(TimeSeries):

    @staticmethod
    def staircase_from_time_series(ts):
        ltf = LinearTimeFunction()
        ltf.t = []
        ltf.v = []
        for i in range(1, len(ts.t)):
            ltf.t.append(ts.t[i - 1])
            ltf.v.append(ts.v[i - 1])
            ltf.t.append(ts.t[i])
            ltf.v.append(ts.v[i - 1])
        ltf.t.append(ts.t[-1])
        ltf.v.append(ts.v[-1])
        return ltf

    @staticmethod
    def interpolate_from_time_series(ts):
        ltf = LinearTimeFunction()
        ltf.t = ts.t
        ltf.v = ts.v
        return ltf

    def get_value(self, time, i):
        # time: instant for which value is requested
        # self.t[i-1]<=time<=self.t[i]
        if len(self.t) > i:
            if i > 0:
                d = self.t[i] - self.t[i - 1]
            else:
                d = 0
            if d == 0:
                val = self.v[i]
            else:
                val = self.v[i - 1] + (self.v[i] - self.v[i - 1]) * (time - self.t[i - 1]) / d
        else:
            print("TimeFunction: index_of_concept out of bounds")
            val = 0
        return val

    @staticmethod
    def difference(ltf0, ltf1):
        diff = LinearTimeFunction()
        start = max(min(ltf0.t), min(ltf1.t))
        stop = min(max(ltf0.t), max(ltf1.t))
        if start <= stop:
            i0 = 0
            while i0 + 1 < len(ltf0.t) and ltf0.t[i0] < start:
                i0 += 1
            i1 = 0
            while i1 + 1 < len(ltf1.t) and ltf1.t[i1] < start:
                i1 += 1
            while i0 < len(ltf0.t) and i1 < len(ltf1.t):
                if ltf0.t[i0] <= ltf1.t[i1]:
                    diff.t.append(ltf0.t[i0])
                    val = ltf1.get_value(ltf0.t[i0], i1)
                    diff.v.append(ltf0.v[i0] - val)
                    i0 += 1
                else:
                    diff.t.append(ltf1.t[i1])
                    val = ltf0.get_value(ltf1.t[i1], i0)
                    diff.v.append(val - ltf1.v[i1])
                    i1 += 1
        return diff

    @staticmethod
    def absolute(ltf):
        absolute = LinearTimeFunction()
        i = 0
        if i < len(ltf.t):
            absolute.add(ltf.t[i], math.fabs(ltf.v[i]))
            i += 1
        while i < len(ltf.t):
            if ltf.v[i - 1] * ltf.v[i] < 0:
                t = absolute.t[-1] + (ltf.t[i] - absolute.t[-1]) * ltf.v[i - 1] / (ltf.v[i - 1] - ltf.v[i])
                absolute.add(t, 0)
            absolute.add(ltf.t[i], math.fabs(ltf.v[i]))
            i += 1
        return absolute

    def normalize(self):
        # only the first and last of equal consecutive values are needed
        # only the first and last of equal consecutive times are needed
        # only the first of two equal consecutive times and values are needed
        new = LinearTimeFunction()
        i = 0
        while i < len(self.t):
            while i + 1 < len(self.t) and self.t[i + 1] == self.t[i]:
                i += 1
            if new.t == [] or new.t[-1] != self.t[i] or new.v[-1] != self.v[i]:
                new.t.append(self.t[i])
                new.v.append(self.v[i])
            if i + 1 < len(self.t):
                i += 1
                new.t.append(self.t[i])
                new.v.append(self.v[i])
            i += 1
        return new

    def integral(self):
        summation = 0
        for i in range(1, len(self.t)):
            summation += (self.t[i] - self.t[i - 1]) * (self.v[i] + self.v[i - 1]) / 2
        return summation

    def get_points(self):
        ts = TimeSeries()
        i = 0
        while i < len(self.t):
            while i + 1 < len(self.t) and (self.t[i] == self.t[i + 1]):
                i += 1
            ts.add(self.t[i], self.v[i])
            i += 1
        return ts