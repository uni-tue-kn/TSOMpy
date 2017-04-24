# TSOMpy
Online measurement techniques, e.g., moving averages (MAs), calculate time-dependent statistics and are often used in adaptive systems. We proposed a framework to compare multiple MA methods, extended MAs to moving histograms (MHs) and time-dependent rate measurment (TDRM) methods in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf).

TSOMpy is a Python library for online measurement of time series implementing all moving averages (MAs), moving histograms (MHs), and time-dependent rate measurement (TDRM) concepts of [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf).

## Features
TSOMpy offers the following features:

### Qt5-based GUI

TSOMpy includes an intuitive GUI for simplified use. The GUI offers a project model for working on multiple analyses in parallel, a plot model for generating multiple plots for a specific time series and an analysis model to support various evaluation methods on a specific plot.

### Generation and import of time series

TSOMpy allows to import or generate time series using a GUI wizard. Online measurement concepts can be applied to two different types of time series:

- Equally-spaced time series
  + Vector of samples
    + Import a vector of samples (from a CSV file)
    + Generate a vector of samples according to a distribution
    + Set a fixed sample size
  + Vector of time instants
    + Samples are assigned with time indizes 0, 1, 2, ..., n per default
    + Optional: set the starting point and the spacing interval
- Unequally-spaced time series
  + Vector of samples (as above)
  + Vector of time instants
    + Import a vector of time instants (from a CSV file)
    + Generate a vector of time instants according to a distribution

### Application of Online Measurement Methods
All online measurement concepts are implemented in an object-oriented class hierarchy. MA and MH concepts inherit from their base class, TDRM interit from their base class and specific MA classes.

**MAs (for evenly-spaced time series)**

| Class name | Full method's name     |
|------------|------------------------|
| CumMean | Cumulative Mean (3.1.2) |
| WMA | Window MA (3.1.3) |
| DWMA | Disjoint Windows MA (3.1.4) |
| UEMA | Unbiased Exponential MA (3.1.5) |
| EMA | Exponential MA (3.1.6) |

**Time-dependent MAs (for unevenly-spaced time series)**

| Class name | Full method's name     |
|------------|------------------------|
| TWMA | Time Window MA (3.2.2) |
| DTWMA | Disjoint Time Windows MA (3.2.3) |
| UTEMA | Unbiased Time-Exponential MA (3.2.4) |
| TEMA | Time-Exponential MA (3.2.5) |

**MHs (for evenly-spaced time series)**

| Class name | Full method's name     |
|------------|------------------------|
| MH_CumMean | MH with CumMean (5.1) |
| MH_WMA |  MH with WMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |
| MH_DWMA | MH with DWMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |
| MH_UEMA | MH with UEMA (5.1) |
| MH_EMA | MH with EMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |

**Time-dependent MHs (for unevenly-spaced time series)**

| Class name | Full method's name     |
|------------|------------------------|
| TDMH_TWMA | TDMH with TWMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |
| TDMH_DTWMA | TDMH with DTWMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |
| TDMH_UTEMA | TDMH with UTEMA (5.2) |
| TDMH_TEMA | TDMH with TEMA (not considered in [the paper](https://atlas.informatik.uni-tuebingen.de/~menth/papers/Menth17c.pdf)) |

**Time-dependent RMs (for unevenly-spaced time series)**

| Class name | Full method's name     |
|------------|------------------------|
| TDRM_TWMA | TDRM with Time Window MA (6.1.2) |
| TDRM_DTWMA | TDRM with DTWMA (6.1.3) |
| TDRM_DTWMA_UEMA | TDRM with DTWMA and UEMA (6.1.4) |
| TDRM_UTEMA | TDRM with UTEMA (6.1.5) |
| TDRM_UTEMA_CPA | TDRM with UTEMA and Continuous Packet Arrivals (6.1.6) |
