from Simulator.Concepts.MAs import *
from Simulator.Concepts.TimeDependentMAs import *
from Simulator.Concepts.TimeDependentRMs import *
from Simulator.Concepts.TimeDependentMHs import *
from matplotlib.figure import Figure
import numpy as np
from Simulator.Counter import Counter

class TSOM:
    MA_labels = ["CumMean", "WMA", "DWMA", "UEMA", "EMA"]
    MAs = [CumMean, WMA, DWMA, UEMA, EMA]
    TimeDependentMA_labels = ["TWMA", "DTWMA", "TEMA", "UTEMA"]
    TimeDependentMAs = [TWMA, DTWMA, TEMA, UTEMA]
    TimeDependentMHs_labels = ["TDH_UTEMA"]
    TimeDependentMHs = [TDH_UTEMA]
    TimeDependentRMs_labels = ["TDRMCumMean", "TDRM_TWMA", "TDRM_DTWMA", "TDRM_UTEMA", "TDRM_UTEMA_CPA",
                        "TDRM_DTWMA_EMA", "TDRM_DTWMA_UEMA"]
    TimeDependentRMs = [TDRMCumMean, TDRM_TWMA, TDRM_DTWMA, TDRM_UTEMA, TDRM_UTEMA_CPA,
                               TDRM_DTWMA_EMA, TDRM_DTWMA_UEMA]
    markers = ["o", "^", "s", "p"]

    def __init__(self):
        self.ts = TimeSeries()
        self.ts = TimeSeries.from_value_vector([])




    def get_calculated_histograms(self, concepts, t_stop, colors):
        index = 0
        figure = Figure()

        if not self.ts.t:
            return figure

        while (index < (len(self.ts.t))) and (self.ts.t[index] < t_stop):
            index += 1
        self.t_stop = index


        for i in range(0, len(concepts)):

            if type(concepts[i]) in self.TimeDependentMHs:
                ax = figure.add_subplot(111)

                values = self.ts.v[:self.t_stop]

                labels, y_values = concepts[i].calculate_histogram(values)

                (labels[0])[0] = (labels[0])[1]
                (labels[-1])[1] = (labels[-1])[0]

                x_values = [np.mean(label) for label in labels]
                width = (x_values[-1] - x_values[0]) / len(x_values)
                x_values[0] -= width / 2
                x_values[-1] += width / 2
                ax.set_title("Observed moment t = " + str(self.t_stop))
                ax.set_xlabel('Bins')
                ax.set_ylabel('Relative frequency')
                ax.bar(x_values, y_values, color=colors[i].name(), width=width, edgecolor='black')
            figure.set_tight_layout(1)

            return figure

        return figure

    def get_calculated_plot(self, concepts, concept_names, colors, progress_bar=None):

        graphs_l_width = 1
        self.markers.append('o')
        markers = self.markers

        rdiff = []
        figure = Figure()

        if not self.ts.t:
            return figure, ""

        ax1 = figure.add_subplot(111)
        ax2 = ax1.twinx()
        evaluation = ""
        if progress_bar:
            progress_bar.setValue(0)
            for i in range(31):
                progress_bar.setValue(i)
        for i in range(0, len(concepts)):
            concepts[i].reset_average()
            if type(concepts[i]) in self.MAs:
                tmp = concepts[i].get_avg_ltf(self.ts)

                ax = ax1
                if progress_bar:
                    progress_bar.setValue(30 + (70 * (i+1)) / len(concepts))

            elif type(concepts[i]) in self.TimeDependentMAs:
                ma = concepts[i]
                ma._granularity = 20
                tmp = ma.get_avg_ltf(max(self.ts.t) + 1, self.ts)
                ax = ax1
                if progress_bar:
                    progress_bar.setValue(30 + (70*(i+1)) / len(concepts))

            elif type(concepts[i]) in self.TimeDependentRMs:
                ax = ax2
                tmp = concepts[i].get_rate_ltf(self.ts.t[-1], self.ts)
                tdc = Counter.TDC()
                tdc.read_linear_time_function(tmp)

                evaluation += concept_names[i]
                evaluation += ",\n         E    = "
                evaluation += str(round(tdc.mean(), 4))
                evaluation += ",\n        cvar = "
                evaluation += str(round(tdc.cvar(), 4))
                evaluation += ",\n         I    = "
                evaluation += str(round(tmp.integral()/(self.ts.t[-1] - self.ts.t[0]), 4))
                evaluation += "\n\n"
                rdiff.append(tmp)
                if progress_bar:
                    if len(concepts) == 2:
                        progress_bar.setValue(30 + (20*(i+1) / len(concepts)))
                    else:
                        progress_bar.setValue(30 + (70*(i+1) / len(concepts)))

            else:
                raise NotImplementedError

            ax.plot(tmp.t, tmp.v, color=colors[i].name(), linewidth=graphs_l_width)
            ax1.set_xlabel('Time')
            ax1.set_ylabel('Values')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Rates', rotation=270, labelpad=15)

            if len(tmp.t) < 100:
                points = tmp.get_points()
                points.t.pop(-1)
                points.v.pop(-1)
                ax.plot(points.t, points.v, color=colors[i].name(), MarkerSize=3, marker=markers[i], ls="")

        if len(rdiff) == 2:
            diff = LinearTimeFunction.difference(rdiff[0], rdiff[1])
            if progress_bar:
                progress_bar.setValue(75)
            diff = LinearTimeFunction.absolute(diff)
            if progress_bar:
                progress_bar.setValue(90)
            tdc = Counter.TDC()
            tdc.read_linear_time_function(diff)
            evaluation += "Rate difference:\n"
            evaluation += "   R = "
            evaluation += str(round(tdc.mean(), 4))
            if progress_bar:
                progress_bar.setValue(100)
            diff = diff.normalize()
            ax.plot(diff.t, diff.v, color=colors[i+1].name())

            if "Rate difference" not in concept_names:
                concept_names.append("Rate difference")
            rdiff.append(diff)
        figure.set_tight_layout(1)

        return figure, evaluation


    def get_ltf(self, concept):
        if type(concept) in self.MAs:
            tmp = concept.get_avg_ltf(self.ts)

        elif type(concept) in self.TimeDependentMAs:
            ma = concept
            ma._granularity = 20
            tmp = ma.get_avg_ltf(max(self.ts.t) + 1, self.ts)

        elif type(concept) in self.TimeDependentRMs:
            tmp = concept.get_rate_ltf(self.ts.t[-1], self.ts)
        elif type(concept) in self.TimeDependentMHs:
            labels, y_values = concept.calculate_histogram(self.ts.v)
            return labels, y_values
        return tmp.t, tmp.v
