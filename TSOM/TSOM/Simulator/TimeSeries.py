from GUI.Error.DifferendFileLength import Ui_DifferendFileLengthError
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class TimeSeries:
    def __init__(self):
        self.t = []
        self.v = []

    def check(self):
        if len(self.t) != len(self.v):
            print("TimeSeries.check(): .t and .v have different number of entries")
        if len(self.t) > 0:
            last_t = self.t[0]
            for i in range(1, len(self.t)):
                if self.t[i] < last_t:
                    print("TimeSeries.check(): .t not in ascending order")
                last_t = self.t[i]

    @staticmethod
    def from_time_vector(t, constant_vector=1):
        ts = TimeSeries()
        ts.t = t
        ts.v = []
        for i in t:
            ts.v.append(constant_vector)
        ts.check()
        return ts

    @staticmethod
    def from_value_vector(v, start_time=0, spacing_interval=1):
        ts = TimeSeries()
        ts.v = v
        for i in range(len(v)):
            ts.t.append(float(start_time) + i * float(spacing_interval))
        return ts

    @staticmethod
    def from_vectors(t, v):
        ts = TimeSeries()
        ts.t = t
        ts.v = v
        ts.check()
        return ts

    @staticmethod
    def from_value_file(filename, start_time=0, spacing_interval=1):
        v = read_float_array_fom_file(filename)
        return TimeSeries.from_value_vector(v, start_time, spacing_interval)

    @staticmethod
    def from_time_file(filename, constant_value=1, time_shift=0):
        t = read_float_array_fom_file(filename, time_shift)
        return TimeSeries.from_time_vector(t, constant_value)

    @staticmethod
    def from_files(t_filename, v_filename, time_shift=0):
        t = read_float_array_fom_file(t_filename, time_shift)
        v = read_float_array_fom_file(v_filename)
        if len(t) != len(v):
            t = t[:min(len(t), len(v))]
            v = v[:min(len(t), len(v))]
            diff_file_length_error = QtWidgets.QDialog()
            ui = Ui_DifferendFileLengthError(diff_file_length_error)
            diff_file_length_error.exec()



        return TimeSeries.from_vectors(t, v)

    @staticmethod
    def from_value_file_and_time_distribution(v_filename, distribution, time_shift):
        v = read_float_array_fom_file(v_filename)
        t = distribution.get_time_vector_from_length(len(v), time_shift)
        return TimeSeries.from_vectors(t, v)

    @staticmethod
    def from_time_file_and_sample_size_distribution(t_filename, distribution, time_shift=0):
        t = read_float_array_fom_file(t_filename, time_shift)
        v = distribution.get_sample_vector_from_length(len(t))
        return TimeSeries.from_vectors(t, v)

    @staticmethod
    def from_time_distribution(distribution, value, t_stop, time_shift=0):
        t = distribution.get_time_vector(t_stop, time_shift)
        return TimeSeries.from_time_vector(t, value)

    @staticmethod
    def from_distributions(t_distribution, v_distribution, t_stop, time_shift=0):
        t = t_distribution.get_time_vector(t_stop, time_shift)
        v = v_distribution.get_sample_vector_from_length(len(t))
        return TimeSeries.from_vectors(t, v)


    def add(self, time, value):
        self.t.append(time)
        self.v.append(value)

    def to_string(self):
        return ".t=" + str(self.t) + "\n.v=" + str(self.v)


def read_float_array_fom_file(filename, time_shift=0):
    arr = []
    inp = open(filename, "r")
    #  read line into array
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(time_shift + float(i))
    return arr
