import matplotlib.pyplot as plt
from Simulator.RandomProcess import GammaArrivalProcess, PoissonArrivalProcess
from Simulator.TimeSeries import TimeSeries

from Simulator.Concepts.MAs import CumMean, WMA, DWMA
from Simulator.Concepts.TimeDependentMAs import *
from Simulator.Concepts.TimeDependentRMs import *
from Simulator.Counter.Counter import TDC


# ---------------------------------------------------------------------------------------------------------------------------------------------
# Functions to generate data and figures for the ICPE paper
# ---------------------------------------------------------------------------------------------------------------------------------------------



def conference_paper_figures(file_path):
    import matplotlib
    import numpy as np

    # use type 42 fonts (request from ACM submission service)
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42

    # Set ggplot style
    plt.style.use('ggplot')
    matplotlib.rcParams.update({'font.size': 18})

    colors = ["r-", "g-", "b-", "k-"]
    markers = ["o", "^", "s", "p"]

    #
    # graph settings
    #

    graphs_l_width = 2

    # color_brewer Set1_4 as RGB values
    graph_colors = [((228 / 255), (26 / 255), (28 / 255)), ((55 / 255), (126 / 255), (184 / 255)), ((77 / 255), \
                                                                                                    (175 / 255),
                                                                                                    (74 / 255)),
                    ((152 / 255), (78 / 255), (163 / 255))]

    #
    # Figure 1 (a)
    #

    ax = plt.gca()
    ax.patch.set_facecolor('None')  # disable plot background

    # R look
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')

    ax.xaxis.grid(False)
    ax.yaxis.grid(False)

    sample_instants = [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]

    ts = TimeSeries.from_value_vector(sample_instants)

    memory = 4
    moving_averages = [CumMean(memory), WMA(memory), UEMA(memory), DWMA(memory)]
    moving_averages_names = ["CumMean", "WMA", "UEMA", "DWMA"]

    for i in range(0, len(moving_averages)):
        tmp = moving_averages[i].get_avg_ltf(ts)
        plt.plot(tmp.t, tmp.v, color=graph_colors[i], linewidth=graphs_l_width)

        # plot points
        points = tmp.get_points()
        points.t.pop(-1)
        points.v.pop(-1)
        plt.plot(points.t, points.v, color=graph_colors[i], marker=markers[i], markersize=7, ls="")

        # not-plotted plot() for generating labels with markers
        plt.plot(-10, -10, color=graph_colors[i], linewidth=graphs_l_width, label=moving_averages_names[i], \
                 marker=markers[i], markersize=7)

    plt.axis([-.1, 12.5, -.1, 1.1])  # set plot axis ranges

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.xlabel(r'Time index_of_concept $j$')  # set x-axis label
    plt.ylabel(r'Time-dependent average $A_j$')  # set y-axis label
    plt.tight_layout()  # set tight layout

    plt.legend(loc='lower center', frameon=0, numpoints=1)

    plt.savefig(str(file_path) + "ESTS-MA-Overview.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 1 (b)
    #

    ax = plt.gca()
    ax.patch.set_facecolor('None')

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    memories = [2, 4, 10]
    labels = ["a = 0.5", "a = 0.75", "a = 0.9"]

    for i in range(0, len(memories)):
        tmp = UEMA(memories[i]).get_avg_ltf(ts)
        plt.plot(tmp.t, tmp.v, color=graph_colors[i], linewidth=graphs_l_width)

        # plot points
        points = tmp.get_points()
        points.t.pop(-1)
        points.v.pop(-1)
        plt.plot(points.t, points.v, color=graph_colors[i], marker=markers[i], markersize=7, ls="")

        # not-plotted plot() for generating labels with markers
        plt.plot(-10, -10, color=graph_colors[i], linewidth=graphs_l_width, label=labels[i], marker=markers[i],
                 markersize=7)

    plt.xlabel(r'Time index_of_concept $j$')  # set x-axis label
    plt.ylabel(r'Time-dependent average $A_j$')  # set y-axis label
    plt.tight_layout()  # set tight layout

    plt.axis([-.1, 12.5, -.1, 1.1])  # set plot axis ranges
    plt.legend(loc='lower left', frameon=0, numpoints=1)

    plt.savefig(str(file_path) + "UEMA-Impact-SmoothingFactor.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 1 (c)
    #

    ax = plt.gca()
    ax.patch.set_facecolor('None')

    v = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ts = TimeSeries.from_value_vector(v)

    tmp = UEMA(4).get_avg_ltf(ts)
    plt.plot(tmp.t, tmp.v, color=graph_colors[0], linewidth=graphs_l_width)

    # plot points
    points = tmp.get_points()
    points.t.pop(-1)
    points.v.pop(-1)
    plt.plot(points.t, points.v, color=graph_colors[0], marker=markers[0], markersize=7, ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[0], linewidth=graphs_l_width, label="UEMA", marker=markers[0], markersize=7)

    tmp = EMA(4).get_avg_ltf(ts)
    plt.plot(tmp.t, tmp.v, color=graph_colors[1], linewidth=graphs_l_width)

    # plot points
    points = tmp.get_points()
    points.t.pop(-1)
    points.v.pop(-1)
    plt.plot(points.t, points.v, color=graph_colors[1], marker=markers[1], markersize=7, ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[1], linewidth=graphs_l_width, label="EMA", marker=markers[1], markersize=7)

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.xlabel(r'Time index_of_concept $j$')
    plt.ylabel(r'Time-dependent average $A_j$')
    plt.tight_layout()

    plt.axis([-.1, 12.5, -.1, 1.1])  # set plot axis ranges
    plt.legend(frameon=0, numpoints=1)

    plt.savefig(str(file_path) + "UEMA-EMA-Bias.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 2 (a)
    #

    ax = plt.gca()
    ax.patch.set_facecolor('None')

    # plot fast-slow time series
    fast_slow = [.5, 1, 1.5, 2, 2.5, 3, 4.5, 6, 7.5, 9, 10.5, 12]
    plt.axhline(1.2, linewidth=graphs_l_width, color=graph_colors[0])
    plt.plot(fast_slow, np.repeat(1.2, len(fast_slow)), 'v', color=graph_colors[0], markersize=7)
    plt.text(0, 1.25, 'fast - slow', fontsize=18)

    # plot evenly spaced time series
    evenly_spaced = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.axhline(y=1.1, linewidth=2, color=graph_colors[1])
    plt.plot(evenly_spaced, np.repeat(1.1, len(evenly_spaced)), 'ro', color=graph_colors[1], markersize=7)
    plt.text(0, 1.15, 'evenly spaced', fontsize=18)

    # plot slow-fast time series
    slow_fast = [1.5, 3, 4.5, 6, 7.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
    plt.axhline(1, linewidth=2, color=graph_colors[2])
    plt.plot(slow_fast, np.repeat(1, len(fast_slow)), '^', color=graph_colors[2], markersize=7)
    plt.text(0, 1.05, 'slow - fast', fontsize=18)

    plt.axis([-.5, 12.5, .9, 1.3])  # set plot axis ranges
    plt.yticks([])  # disable y-labels
    plt.xlabel(r'Time ($\Delta t$)')  # set x-axis label
    plt.tight_layout()  # set tight layout

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.savefig(str(file_path) + "TimeStructure.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 2 (b)
    #

    ax = plt.gca()
    ax.patch.set_facecolor('None')

    fast_slow = [.5, 1, 1.5, 2, 2.5, 3, 4.5, 6, 7.5, 9, 10.5, 12]
    evenly_spaced = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    slow_fast = [1.5, 3, 4.5, 6, 7.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
    samples = [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]

    tdma = UTEMA(4, 0)
    tdma._granularity = 20

    ts_fast_slow = TimeSeries.from_vectors(fast_slow, samples)
    tmp = tdma.get_avg_ltf(max(ts_fast_slow.t) + 1, ts_fast_slow)
    plt.plot(tmp.t, tmp.v, color=graph_colors[0], linewidth=2)

    # plot points
    ts = tmp.get_points()
    ts.t.pop(0)
    ts.v.pop(0)
    ts.t.pop(-1)
    ts.v.pop(-1)
    plt.plot(ts.t, ts.v, color=graph_colors[0], marker=markers[0], ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[0], linewidth=graphs_l_width, label="fast-slow", marker=markers[0],
             markersize=7)

    tdma = UTEMA(4, 0)
    tdma._granularity = 20

    ts_evenly_spaced = TimeSeries.from_vectors(evenly_spaced, samples)
    tmp = tdma.get_avg_ltf(max(ts_evenly_spaced.t) + 1, ts_evenly_spaced)
    plt.plot(tmp.t, tmp.v, color=graph_colors[1], linewidth=2)

    # plot points
    ts = tmp.get_points()
    ts.t.pop(0)
    ts.v.pop(0)
    ts.t.pop(-1)
    ts.v.pop(-1)
    plt.plot(ts.t, ts.v, color=graph_colors[1], marker=markers[1], markersize=7, ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[1], linewidth=graphs_l_width, label="evenly spaced", marker=markers[1],
             markersize=7)

    tdma = UTEMA(4, 0)
    tdma._granularity = 20

    ts_slow_fast = TimeSeries.from_vectors(slow_fast, samples)
    tmp = tdma.get_avg_ltf(max(ts_slow_fast.t) + 1, ts_slow_fast)
    plt.plot(tmp.t, tmp.v, color=graph_colors[2], linewidth=2)

    # plot points
    ts = tmp.get_points()
    ts.t.pop(0)
    ts.v.pop(0)
    ts.t.pop(-1)
    ts.v.pop(-1)
    plt.plot(ts.t, ts.v, color=graph_colors[2], marker=markers[2], markersize=7, ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[2], linewidth=graphs_l_width, label="slow-fast", marker=markers[2],
             markersize=7)

    plt.axis([-.1, 12.5, -.1, 1.1])
    plt.xlabel(r'Time $\Delta t$')  # set x-axis label
    plt.ylabel(r'Time-dependent average $A_j$')
    plt.tight_layout()  # set tight layout

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.legend(frameon=0, loc="lower right", bbox_to_anchor=[.7, .1], numpoints=1)

    plt.savefig(str(file_path) + "UTEMA-Impact-TimeStructure.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 2 (c)
    #

    sample_instants = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    time_instants = [0, 1.9, 2, 3.9, 4, 5.9, 6, 7.9, 8, 9.9, 10, 11.9, 12]

    # Plot arrival instants
    ts = TimeSeries.from_vectors(time_instants, sample_instants)
    plt.plot(ts.t, ts.v, color=graph_colors[0], marker=markers[0], ls='', label="Sample")

    ma = UTEMA(4, 0)
    ma._granularity = 20
    tmp = ma.get_avg_ltf(max(ts.t) + 1, ts)
    plt.plot(tmp.t, tmp.v, color=graph_colors[1], linewidth=2)

    ts_points = tmp.get_points()
    ts_points.t.pop(0)
    ts_points.v.pop(0)
    ts_points.t.pop(-1)
    ts_points.v.pop(-1)
    plt.plot(ts_points.t, ts_points.v, marker=markers[1], color=graph_colors[1], ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[1], linewidth=graphs_l_width, label="UTEMA", marker=markers[1], markersize=7)

    ma = TEMA(4, 0)
    ma._granularity = 20
    tmp = ma.get_avg_ltf(max(ts.t) + 1, ts)
    plt.plot(tmp.t, tmp.v, color=graph_colors[2], linewidth=2)

    ts_points = tmp.get_points()
    ts_points.t.pop(0)
    ts_points.v.pop(0)
    ts_points.t.pop(-1)
    ts_points.v.pop(-1)
    plt.plot(ts_points.t, ts_points.v, marker=markers[2], color=graph_colors[2], ls="")

    # not-plotted plot() for generating labels with markers
    plt.plot(-10, -10, color=graph_colors[2], linewidth=graphs_l_width, label="TEMA", marker=markers[2], markersize=7)

    plt.xlabel(r'Time $t$')  # set x-axis label
    plt.ylabel(r'Time-dependent average $A_t$')
    plt.tight_layout()  # set tight layout

    ax = plt.gca()  # get the axes
    ax.patch.set_facecolor('None')  # disable plot background

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.axis([-.1, 12.5, -.1, 1.1])
    plt.legend(frameon=0, loc="lower right", bbox_to_anchor=[1, .1], numpoints=1)

    plt.savefig(str(file_path) + "UTEMA-TEMA-Bias.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 3
    #

    fig, ax1 = plt.subplots()

    # disable background color
    for item in [fig, ax1]:
        item.patch.set_visible(False)

    n = 100
    memory = 4
    uema = UEMA(memory)
    beta = 1 / uema.adapted_memory()
    print(beta)
    print(uema._a)
    x = []
    y = []
    z = []
    for i in range(-8 * n, 1):
        x.append(i / n)
        y.append(math.exp(beta * x[-1]))
        z.append(pow(uema._a, -math.ceil(x[-1])))

    x_points = []
    z_points = []
    for i in range(-8, 1):
        x_points.append(i)
        z_points.append(pow(uema._a, -i))

    # plot UEMA
    ax1.plot(0, 0, color=graph_colors[0], label=r'$g_{UEMA}(k)$', linewidth=2, marker="o")  # empty plot for label
    ax1.plot(x, y, color=graph_colors[1], label=r'$g_{UTEMA}(t)$', linewidth=2)
    ax1.set_ylabel('Weights')
    ax1.set_xlabel(r'Time $\Delta t$')
    ax1.legend(loc=0, frameon=0, numpoints=1)

    ax2 = ax1.twiny()
    ax2.plot(x, z, color=graph_colors[0], label=r'$g_{UTEMA}(t)$', linewidth=2)
    print(z)
    ax2.plot(x_points, z_points, color=graph_colors[0], marker="o", ls="")
    ax2.set_xlabel('Time index_of_concept k')
    ax2.get_yaxis().set_visible(False)

    # plot frame_sv border colors
    ax1 = plt.gca()  # get the axes
    ax1.grid(b=False)
    ax1.patch.set_facecolor('None')  # disable plot background
    ax1.spines['bottom'].set_color('black')
    ax1.spines['top'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    ax2 = plt.gca()  # get the axes
    ax2.grid(b=False)
    ax2.patch.set_facecolor('None')  # disable plot background
    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    fig.tight_layout()
    plt.axis([-8.1, 0.1, 0, 1.1])

    plt.savefig(str(file_path) + "UEMA-UTEMA-Comparison-WeightFunction.pdf")
    plt.close()

    #
    # Figure 4
    #

    plt.figure(figsize=(11, 4))

    ax = plt.gca()
    ax1.grid(b=False)
    ax.patch.set_facecolor('None')

    memory = 1
    t_start = -16
    t_stop = 2
    t = [0]

    ts = TimeSeries.from_time_vector(t)

    tdrms = [TDRM_TWMA(memory, t_start), TDRM_DTWMA_UEMA(memory, t_start, memory * 0.25), \
             TDRM_UTEMA(memory, t_start)]
    tdrm_labels = ["TDRM-TWMA", "TDRM-DTWMA-UEMA", "TDRM-UTEMA"]

    t = [0, 2]
    v = [0, 0]
    ltf_plot = LinearTimeFunction.interpolate_from_time_series(TimeSeries.from_vectors(t, v))

    for i in range(0, len(tdrms)):
        ltf = tdrms[i].get_rate_ltf(t_stop, ts)
        ltf = LinearTimeFunction.difference(ltf, ltf_plot)
        plt.plot(ltf.t, ltf.v, color=graph_colors[i], label=tdrm_labels[i], linewidth=2)

    plt.xlabel(r'Time ($\Delta t$)')
    plt.ylabel(r'Rate ($1/\Delta t$)')
    plt.tight_layout()  # set tight layout

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.legend(frameon=0, loc="upper right")
    plt.savefig(str(file_path) + "Impulses.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 5
    #

    plt.figure(figsize=(22, 5))

    ax = plt.gca()
    ax.grid(b=False)
    ax.patch.set_facecolor('None')

    memory = 10
    t_start = 0
    t_stop = 70
    t = []

    for i in range(15, 45):
        t.append(i)

    sample_value = []
    for t_item in t:
        sample_value.append(-.2)

    # Plot arrival instants
    plt.axhline(y=-.1, linewidth=2, color="black")
    ts = TimeSeries.from_vectors(time_instants, sample_instants)
    plt.plot(t, sample_value, color="black", marker="o", ls='')

    ts = TimeSeries.from_time_vector(t)
    tdrms = [TDRM_TWMA(memory, t_start), TDRM_DTWMA(memory, t_start), TDRM_DTWMA_UEMA(memory, t_start, memory * 0.2),
             TDRM_UTEMA(memory, t_start)]
    labels = ["TDRM-TWMA", "TDRM-DTWMA", "TDRM-DTWMA-UEMA", "TDRM-UTEMA"]

    t = [10, 70]
    v = [0, 0]

    ltf_plot = LinearTimeFunction.interpolate_from_time_series(TimeSeries.from_vectors(t, v))

    for i in range(0, len(tdrms)):
        ltf = tdrms[i].get_rate_ltf(t_stop, ts)
        ltf = LinearTimeFunction.difference(ltf, ltf_plot)
        plt.plot(ltf.t, ltf.v, color=graph_colors[i], label=labels[i], linewidth=2)

    plt.xlabel(r'Time ($\Delta t$)')
    plt.ylabel(r'TDRM ($1/\Delta t}$)')
    plt.tight_layout()  # set tight layout

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.axis([10, 65, -.3, 1.1])
    plt.legend(frameon=0, loc="lower center", bbox_to_anchor=[.5, .15])

    plt.savefig(str(file_path) + "Burst.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 6
    #

    # experiment setup
    t_start4plot = 40
    t_stop4plot = 240
    mean_iat = 1
    memory = 20
    t_start = 0
    seed = 9
    lineStyle = ["r-", "g-", "b-", "k-"]

    # define TDRM methods to be used
    mrs = [TDRM_TWMA(memory, t_start), TDRM_DTWMA(memory, t_start), TDRM_DTWMA_UEMA(memory, t_start, 0.25 * memory),
           TDRM_UTEMA(memory, t_start)]

    # generate sample data following a Poisson process
    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop4plot)
    ts = TimeSeries.from_time_vector(t)

    #
    # Figure 6 (a)
    #

    t_new = []
    v_new = []

    for i in range(0, len(t)):
        t_new.append(t[i])
        t_new.append(t[i])
        t_new.append(t[i])
        v_new.append(0)
        v_new.append(1)
        v_new.append(0)

    plt.figure(figsize=(14, 1.3))
    plt.ylim(ymax=1.0, ymin=0)
    plt.xlim(xmax=t_stop4plot, xmin=t_start4plot)
    plt.plot(t_new, v_new, "k-")

    ax = plt.gca()
    ax.grid(b=False)
    ax.patch.set_facecolor('None')

    plt.yticks([])  # disable y-labels
    plt.tight_layout()  # set tight layout

    # plot frame_sv border colors
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')

    plt.savefig(str(file_path) + "PoissonProcess.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 6 (b) - TDRM-TWMA
    #

    m = [memory, 2 * memory]

    fig, ax1 = plt.subplots(figsize=(22, 4))
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(r'Measured rates ($1/\Delta t$)')
    ax1.set_ylim(0.5, 1.65)

    ax2 = ax1.twinx()
    ax2.grid(b=False)
    ax2.axhline(y=0, color="black", linestyle='-')

    rate_ltf = []

    # memory = memory
    mrs[0].reset(m[0], t_start)
    rate_ltf.append(mrs[0].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[0].t, rate_ltf[0].v, color=graph_colors[0], linewidth=2,
             label=r'TDRM-TWMA ($M = 20 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[1], linewidth=2, label=r'TDRM-TWMA ($M = 40 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[2], linewidth=2, label="Rate difference")
    ax1.legend(loc="upper right", frameon=0, ncol=3, bbox_to_anchor=(0.98, 1))

    # memory = 2 * memory
    mrs[0].reset(m[1], t_start)
    rate_ltf.append(mrs[0].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[1].t, rate_ltf[1].v, color=graph_colors[1], linewidth=2,
             label=r'TDRM-TWMA ($M = 40 \cdot \Delta t)')

    # plot rate difference
    diff = LinearTimeFunction.difference(rate_ltf[0], rate_ltf[1])
    diff = diff.normalize()

    ax2.plot(diff.t, diff.v, color=graph_colors[2], linewidth=2)
    ax2.set_ylabel(r'Rate difference ($1/\Delta t$)', rotation=270, labelpad=30)
    ax2.set_ylim(-0.6, 0.6)

    ax1.set_xlim(40, 240)

    ax1.patch.set_facecolor('None')  # disable plot background
    ax1.grid(b=False)
    ax2.patch.set_facecolor('None')  # disable plot background
    ax2.grid(b=False)

    # plot frame_sv border colors
    ax1.spines['bottom'].set_color('black')
    ax1.spines['top'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    fig.tight_layout()
    plt.savefig(str(file_path) + "TDRM_TWMA.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 6 (c)
    #

    m = [memory, 2 * memory]

    fig, ax1 = plt.subplots(figsize=(22, 4))
    ax1.grid(b=False)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(r'Measured rates ($1/\Delta t$)')
    ax1.set_ylim(0.5, 1.65)

    rate_ltf = []

    # memory = memory
    mrs[1].reset(m[0], t_start)
    rate_ltf.append(mrs[1].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[0].t, rate_ltf[0].v, color=graph_colors[0], linewidth=2,
             label=r'TDRM-DTWMA ($M = 20 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[1], linewidth=2, label=r'TDRM-DTWMA ($M = 40 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[2], linewidth=2, label="Rate difference")
    ax1.legend(loc="upper right", frameon=0, ncol=3)

    # memory = 2 * memory
    mrs[1].reset(m[1], t_start)
    rate_ltf.append(mrs[1].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[1].t, rate_ltf[1].v, color=graph_colors[1], linewidth=2)

    # plot rate difference
    diff = LinearTimeFunction.difference(rate_ltf[0], rate_ltf[1])
    diff = diff.normalize()

    ax2 = ax1.twinx()
    ax2.axhline(y=0, color="black", linestyle='-')
    ax2.grid(b=False)
    ax2.plot(diff.t, diff.v, color=graph_colors[2], linewidth=2)
    ax2.set_ylabel(r'Rate difference ($1/\Delta t$)', rotation=270, labelpad=30)
    ax2.set_ylim(-0.6, 0.6)

    ax1.set_xlim(40, 240)

    ax1.patch.set_facecolor('None')  # disable plot background
    ax1.grid(b=False)
    ax2.patch.set_facecolor('None')  # disable plot background
    ax2.grid(b=False)

    # plot frame_sv border colors
    ax1.spines['bottom'].set_color('black')
    ax1.spines['top'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    fig.tight_layout()
    plt.savefig(str(file_path) + "TDRM_DTWMA.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 6 (d)
    #

    m = [memory, 2 * memory]

    fig, ax1 = plt.subplots(figsize=(22, 4))
    ax1.grid(b=False)

    rate_ltf = []

    # memory = memory
    mrs[2].reset(m[0], t_start)
    rate_ltf.append(mrs[2].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[0].t, rate_ltf[0].v, color=graph_colors[0], linewidth=2,
             label=r'TDRM-DTWMA-UEMA ($M = 20 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[1], linewidth=2, label=r'TDRM-DTWMA-UEMA ($M = 40 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[2], linewidth=2, label="Rate difference")
    ax1.legend(loc="upper right", frameon=0, ncol=3)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(r'Measured rates ($1/\Delta t$)')
    ax1.set_ylim(0.5, 1.65)

    # memory = 2 * memory

    mrs[2].reset(m[1], t_start)
    rate_ltf.append(mrs[2].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[1].t, rate_ltf[1].v, color=graph_colors[1], linewidth=2)

    # plot rate difference
    diff = LinearTimeFunction.difference(rate_ltf[0], rate_ltf[1])
    diff = diff.normalize()

    ax2 = ax1.twinx()
    ax2.axhline(y=0, color="black", linestyle='-')
    ax2.grid(b=False)
    ax2.plot(diff.t, diff.v, color=graph_colors[2], linewidth=2)
    ax2.set_ylabel(r'Rate difference ($1/\Delta t$)', rotation=270, labelpad=30)
    ax2.set_ylim(-0.6, 0.6)

    ax1.set_xlim(40, 240)

    ax1.patch.set_facecolor('None')  # disable plot background
    ax1.grid(b=False)
    ax2.patch.set_facecolor('None')  # disable plot background
    ax2.grid(b=False)

    # plot frame_sv border colors
    ax1.spines['bottom'].set_color('black')
    ax1.spines['top'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    fig.tight_layout()
    plt.savefig(str(file_path) + "TDRM_DTWMA_UEMA.pdf", bbox_inches="tight")
    plt.close()

    #
    # Figure 6 (e)
    #

    m = [memory, 2 * memory]

    fig, ax1 = plt.subplots(figsize=(22, 4))
    ax1.grid(b=False)

    rate_ltf = []

    # memory = memory
    mrs[3].reset(m[0], t_start)
    rate_ltf.append(mrs[3].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[0].t, rate_ltf[0].v, color=graph_colors[0], linewidth=2,
             label=r'TDRM-UTEMA ($M = 20 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[1], linewidth=2, label=r'TDRM-UTEMA ($M = 40 \cdot \Delta t$)')
    ax1.plot(0, 0, color=graph_colors[2], linewidth=2, label="Rate difference")
    ax1.legend(loc="upper right", frameon=0, ncol=3)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(r'Measured rates ($1/\Delta t$)')
    ax1.set_ylim(0.5, 1.65)

    # memory = 2 * memory
    mrs[3].reset(m[1], t_start)
    rate_ltf.append(mrs[3].get_rate_ltf(t_stop4plot, ts))
    ax1.plot(rate_ltf[1].t, rate_ltf[1].v, color=graph_colors[1], linewidth=2)

    # plot rate difference
    diff = LinearTimeFunction.difference(rate_ltf[0], rate_ltf[1])
    diff = diff.normalize()

    ax2 = ax1.twinx()
    ax2.axhline(y=0, color="black", linestyle='-')
    ax2.grid(b=False)
    ax2.plot(diff.t, diff.v, color=graph_colors[2], linewidth=2)
    ax2.set_ylabel(r'Rate difference ($1/\Delta t$)', rotation=270, labelpad=30)
    ax2.set_ylim(-0.6, 0.6)

    ax1.set_xlim(40, 240)

    ax1.patch.set_facecolor('None')  # disable plot background
    ax1.grid(b=False)
    ax2.patch.set_facecolor('None')  # disable plot background
    ax2.grid(b=False)

    # plot frame_sv border colors
    ax1.spines['bottom'].set_color('black')
    ax1.spines['top'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    fig.tight_layout()
    plt.savefig(str(file_path) + "TDRM_UTEMA.pdf", bbox_inches="tight")
    plt.close()



def figure6_subfigures():
    # plots the subfigures in Fig. 6
    t_start4plot = 40
    t_stop4plot = 240
    mean_iat = 1
    memory = 20
    t_start = 0
    seed = 9
    line_style = ["r-", "g-", "b-", "k-"]

    mrs = [TDRM_TWMA(memory, t_start), TDRM_DTWMA(memory, t_start),
           TDRM_DTWMA_UEMA(memory, t_start, 0.25 * memory), TDRM_UTEMA(memory, t_start)]

    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop4plot)
    ts = TimeSeries.from_time_vector(t)

    for mr in mrs:
        m = [memory, 2 * memory]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Measured rates (1/s)')

        rate_ltf = []

        for i in range(0, 2):
            mr.reset(m[i], t_start)
            rate_ltf.append(mr.get_rate_ltf(t_stop4plot, ts))

            # plot rates for different memories
            ax1.plot(rate_ltf[i].t, rate_ltf[i].v, line_style[i])

        # plot rate difference
        diff = LinearTimeFunction.difference(rate_ltf[0], rate_ltf[1])
        diff = diff.normalize()

        ax2 = ax1.twinx()
        ax2.plot(diff.t, diff.v, line_style[2])
        ax2.set_ylabel('Rate difference (1/s)')

        fig.tight_layout()
        plt.show()


# figure6_subfigures()

def figure6_data():
    # computes the data for Fig. 6
    mean_iat = 1
    memory = 20
    m = [memory, 2 * memory]
    print("investigated memories=", m)
    t_start = 0
    t_stop = 1000000
    seed = 9
    mrs =[TDRM_UTEMA(memory, t_start)]
    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop)
    ts = TimeSeries.from_time_vector(t)
    t_stop = t[len(t) - 1]
    for mr in mrs:
        ltfs = []
        print(type(mr).__name__)
        for i in range(0, 2):
            mr.reset(m[i], t_start)
            ltf = mr.get_rate_ltf(t_stop, ts)
            tdc = TDC()
            tdc.read_linear_time_function(ltf)
            ltfs.append(ltf)
            print("E=", tdc.mean(), " cvar=", tdc.cvar())
        diff = LinearTimeFunction.difference(ltfs[0], ltfs[1])
        diff = LinearTimeFunction.absolute(diff)
        tdc = TDC()
        tdc.read_linear_time_function(diff)
        print("avg. deviation=", tdc.mean())



#figure6_data()

def tema_exponential():
    mean_iat = 1
    memory = [4, 10, 25]
    t_start = 0
    t_stop = 1000000
    seed = 9
    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop)
    v = []
    t_last = 0
    for x in t:
        v.append(x - t_last)
        t_last = x
    ts = TimeSeries.from_vectors(t, v)
    t_stop = t[len(t) - 1]
    mas = [TEMA(memory[0], t_start), UTEMA(memory[0], t_start)]
    for m in memory:
        for ma in mas:
            ma.reset(m, t_start)
            ltf = ma.get_avg_ltf(t_stop, ts)
            tdc = TDC()
            tdc.read_linear_time_function(ltf)
            print(type(ma).__name__, " M=", m, " E=", tdc.mean(), " cvar=", tdc.cvar())


# tema_exponential()


# Figure5()


def illustrations(memory):
    # Uses TDRMsList
    # prints rates computed by different TDRMs in one figure
    # two figures for two different memories are generated
    # was Figure 6 in the original submission
    mean_iat = 1
    t_start = 0
    t_start4plot = 40
    t_stop4plot = 200
    seed = 9

    mrs=[TDRM_UTEMA(20, 0)]            #mrs = TDRMsList(memory, t_start)
    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop4plot)
    ts = TimeSeries.from_time_vector(t)
    line_style = ["r-", "g-", "b-", "k-"]
    memories = [memory, 2 * memory]

    for m in memories:
        print("memory: ", m)
        plt.figure(figsize=(12, 2))
        plt.subplots_adjust(left=0.05, right=0.975, top=0.95, bottom=0.1)
        plt.ylim(ymax=1.6, ymin=0.5)
        plt.xlim(xmax=t_stop4plot, xmin=t_start4plot)
        for i in range(0, len(mrs)):
            print(type(mrs[i]).__name__)
            mrs[i].reset(m, t_start)
            ltf = mrs[i].get_rate_ltf(max(ts.t), ts)
            plt.plot(ltf.t, ltf.v, line_style[i])
        plt.show()

#illustrations(20)

def analysis(memory, t, t_start):
    # computes E and cvar of measured rates
    # computed avg. deviation of rates measured with memory and 2*memory
    v = []
    for i in t:
        v.append(1)
    t_start = 0
    mrs = [TDRM_UTEMA(memory, t_start), TDRM_UTEMA_CPA(memory, t_start)]
    for mr in mrs:
        print(type(mr).__name__)
        print("memory: ", memory)
        mr.reset(memory, t_start)
        ts = TimeSeries.from_vectors(t, v)
        ltf = mr.get_rate_ltf(max(t), ts)
        tdc = TDC()
        tdc.read_linear_time_function(ltf)
        print("mean=", tdc.mean(), "cvar=", tdc.cvar())



def test_analysis():
    seed = 1
    mean_iat = 1
    t_start = 0
    t_stop = 10000

    t=PoissonArrivalProcess(seed,mean_iat,t_start).get_time_vector(t_stop)
    t = GammaArrivalProcess(seed, mean_iat, t_start, 2).get_time_vector(t_stop)
    analysis(10, t, t_start)


def table6():
    t_start = 0
    t_stop = 1000000
    seed = 9
    mean_iat = 1

    t = PoissonArrivalProcess(seed, mean_iat, t_start).get_time_vector(t_stop)
    analysis(10, t, t_start)
    analysis(100, t, t_start)

    t = GammaArrivalProcess(seed, mean_iat, t_start, 2).get_time_vector(t_stop)
    analysis(10, t, t_start)
    analysis(100, t, t_start)

    # table6()


    # seems ok
    # test_processes()

    # seems ok
    # test_tdhs()

    # seems ok
    # test_mas()

    # seems ok
    # test_tdmas()

    # seems ok
    # test_tdrms()

    # seems ok
    # table2()

    # seems ok
    # table3()

    # seems ok
    # amin_for_probs()

    # seems ok
    # table4()

    # seems ok
    # table5()

    # seems ok
    # table6()

    # seems ok
    # figure6_subfigures()
    # figure6_data()

    # seems ok
    # illustrations(20)

    # seems ok
    # test_memory_adaptation()
