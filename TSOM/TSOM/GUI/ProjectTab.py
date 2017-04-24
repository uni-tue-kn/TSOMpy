import numpy as np
from GUI.InputFrame import Ui_InputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.VisualizeConcepts import Ui_ConceptFrame
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from Simulator import GeneratePaperFigures
from GUI.StorePaperFigures import Ui_GeneratePaperFigures



class Ui_ProjectTab(object):

    def __init__(self, ProjectTab, tsom_project):
        self.tsom = tsom_project

        self.tsom_project = tsom_project
        self.tabs = []
        self.frames = []
        self.tab_layouts = []
        self.tab_ui = []
        self.current_plot_number = 0
        self.setupUi(ProjectTab)

    def setupUi(self, ProjectTab):
        ProjectTab.setObjectName("ProjectTab")
        ProjectTab.resize(1319, 828)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        ProjectTab.setFont(font)
        ProjectTab.setFrameShape(QtWidgets.QFrame.NoFrame)
        ProjectTab.setFrameShadow(QtWidgets.QFrame.Plain)
        ProjectTab.setLineWidth(0)
        self.gridLayout = QtWidgets.QGridLayout(ProjectTab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Plots = QtWidgets.QTabWidget(ProjectTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plots.sizePolicy().hasHeightForWidth())
        self.Plots.setSizePolicy(sizePolicy)
        self.Plots.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Plots.setFont(font)
        self.Plots.setStyleSheet("borde-color: black")
        self.Plots.setTabsClosable(False)
        self.Plots.setMovable(False)
        self.Plots.setTabBarAutoHide(False)
        self.Plots.setObjectName("Plots")
        self.NewTab = QtWidgets.QWidget()
        self.NewTab.setObjectName("NewTab")
        self.Plots.addTab(self.NewTab, "")
        self.gridLayout.addWidget(self.Plots, 1, 0, 1, 1)
        self.frame_top = QtWidgets.QFrame(ProjectTab)
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setLineWidth(0)
        self.frame_top.setObjectName("frame_top")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top1 = QtWidgets.QFrame(self.frame_top)
        self.frame_top1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top1.setLineWidth(0)
        self.frame_top1.setObjectName("frame_top1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_top1)
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 23)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_top1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputData = QtWidgets.QFrame(self.frame_2)
        self.InputData.setMaximumSize(QtCore.QSize(324, 16777215))
        self.InputData.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.InputData.setFrameShadow(QtWidgets.QFrame.Plain)
        self.InputData.setLineWidth(0)
        self.InputData.setObjectName("InputData")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.InputData)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.InputLabel = QtWidgets.QLabel(self.InputData)
        self.InputLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.InputLabel.setFont(font)
        self.InputLabel.setLineWidth(0)
        self.InputLabel.setObjectName("InputLabel")
        self.verticalLayout_5.addWidget(self.InputLabel)
        self.InputTextBrowser = QtWidgets.QTextBrowser(self.InputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTextBrowser.sizePolicy().hasHeightForWidth())
        self.InputTextBrowser.setSizePolicy(sizePolicy)
        self.InputTextBrowser.setMaximumSize(QtCore.QSize(347, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(False)
        self.InputTextBrowser.setFont(font)
        self.InputTextBrowser.setObjectName("InputTextBrowser")
        self.verticalLayout_5.addWidget(self.InputTextBrowser)
        self.horizontalLayout.addWidget(self.InputData)
        self.FrameTimeSeries = QtWidgets.QFrame(self.frame_2)
        self.FrameTimeSeries.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FrameTimeSeries.setFrameShape(QtWidgets.QFrame.Box)
        self.FrameTimeSeries.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FrameTimeSeries.setObjectName("FrameTimeSeries")
        self.plot = QtWidgets.QVBoxLayout(self.FrameTimeSeries)
        self.plot.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.plot.setContentsMargins(0, 0, 0, 0)
        self.plot.setSpacing(0)
        self.plot.setObjectName("plot")
        self.horizontalLayout.addWidget(self.FrameTimeSeries)
        self.FrameTimeSeries.raise_()
        self.InputData.raise_()
        self.verticalLayout_3.addWidget(self.frame_2)
        self.FrameAddTimeSeries = QtWidgets.QFrame(self.frame_top1)
        self.FrameAddTimeSeries.setMaximumSize(QtCore.QSize(16777215, 53))
        self.FrameAddTimeSeries.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FrameAddTimeSeries.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAddTimeSeries.setObjectName("FrameAddTimeSeries")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.FrameAddTimeSeries)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 18)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.FrameSpaceHolder = QtWidgets.QFrame(self.FrameAddTimeSeries)
        self.FrameSpaceHolder.setMaximumSize(QtCore.QSize(16777215, 10))
        self.FrameSpaceHolder.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FrameSpaceHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameSpaceHolder.setObjectName("FrameSpaceHolder")
        self.toolbox = QtWidgets.QVBoxLayout(self.FrameSpaceHolder)
        self.toolbox.setContentsMargins(0, 0, -1, 0)
        self.toolbox.setObjectName("toolbox")
        self.horizontalLayout_4.addWidget(self.FrameSpaceHolder)
        self.button_generate_paper_figures = QtWidgets.QPushButton(self.FrameAddTimeSeries)
        self.button_generate_paper_figures.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_generate_paper_figures.setFont(font)
        self.button_generate_paper_figures.setObjectName("button_generate_paper_figures")
        self.horizontalLayout_4.addWidget(self.button_generate_paper_figures)
        self.scaling = QtWidgets.QComboBox(self.FrameAddTimeSeries)
        self.scaling.setMaximumSize(QtCore.QSize(231, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scaling.setFont(font)
        self.scaling.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.scaling.setObjectName("scaling")
        self.scaling.addItem("")
        self.scaling.addItem("")
        self.horizontalLayout_4.addWidget(self.scaling)
        self.save_button = QtWidgets.QPushButton(self.FrameAddTimeSeries)
        self.save_button.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_4.addWidget(self.save_button)
        self.newTimeSeries = QtWidgets.QPushButton(self.FrameAddTimeSeries)
        self.newTimeSeries.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newTimeSeries.setFont(font)
        self.newTimeSeries.setObjectName("newTimeSeries")
        self.horizontalLayout_4.addWidget(self.newTimeSeries)
        self.verticalLayout_3.addWidget(self.FrameAddTimeSeries)
        self.verticalLayout_2.addWidget(self.frame_top1)
        self.gridLayout.addWidget(self.frame_top, 0, 0, 1, 1)

        self.retranslateUi(ProjectTab)
        self.Plots.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectTab)
        self.initialize()

    def initialize(self):
        self.new_tab()
        self.Plots.setCurrentIndex(0)
        self.Plots.setTabIcon(self.current_plot_number, QtGui.QIcon("Icons/new_plot.ico"))
        self.Plots.currentChanged.connect(self.plot_changed)
        self.canvas = None
        self.InputDialog = None
        self.ui = None
        self.draw_time_series()
        self.logic()

    def plot_changed(self):
        if self.Plots.currentIndex() == self.current_plot_number:
            self.new_tab()
            self.Plots.setCurrentIndex(self.current_plot_number - 1)

    def logic(self):
        self.newTimeSeries.pressed.connect(self.on_pushButton_clicked)
        self.scaling.currentIndexChanged.connect(self.draw_time_series)
        self.save_button.clicked.connect(self.save_time_series)
        self.button_generate_paper_figures.clicked.connect(self.generate_paper_figures)

    def on_pushButton_clicked(self):
        if not self.InputDialog:
            self.InputDialog = QtWidgets.QDialog()
            self.ui = Ui_InputDialog(self.InputDialog, self.tsom)
        self.InputDialog.exec()
        self.tab_ui[self.Plots.currentIndex()].initialize_t_stop(len(self.tsom.ts.t))
        self.draw_time_series()

    def draw_time_series(self):
        if self.canvas:
            self.plot.removeWidget(self.canvas)
            self.plot.removeWidget(self.toolbar)
        self.figure = Figure()
        ax = self.figure.add_subplot(111)
        ax2 = ax.twinx()
        ax.plot(self.tsom.ts.t, self.tsom.ts.v, "r.",  MarkerSize=3)
        ax2.plot(self.tsom.ts.t, self.tsom.ts.v, "r.", MarkerSize=3)

        if self.scaling.currentIndex() == 1:
            ax.set_yscale('log')
            ax2.set_yscale('log')
        else:
            ax.set_yscale('linear')
            ax.set_yscale('linear')

        ax.set_ylabel('Values')
        ax2.set_ylabel('Values', rotation=-90, labelpad=15)
        ax.set_xlabel('Time')
        ax2.set_xlabel('Time')

        self.figure.set_tight_layout(10)
        self.canvas = FigureCanvas(self.figure)
        self.plot.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.FrameTimeSeries, coordinates=True)

        self.toolbar.setStyleSheet("background: transparent;")
        self.plot.addWidget(self.toolbar)


        if self.tsom.ts.v:
            font = QtGui.QFont()
            font.setPointSize(11)
            self.InputTextBrowser.setFont(font)
            self.InputTextBrowser.setText(self.ui.get_input_description())
        self.canvas.callbacks.connect('button_press_event', self.on_canvas_click)
        self.tab_ui[self.Plots.currentIndex()].draw_concepts()

    def on_canvas_click(self, event):
        self.tab_ui[self.Plots.currentIndex()].set_t_stop(event.xdata)

    def new_tab(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("Plot " + str(self.current_plot_number + 1))
        self.tabs.append(tab)
        self.Plots.insertTab(self.current_plot_number, tab, tab.objectName())
        self.initialize_new_tab()

    def initialize_new_tab(self):
        self.tab_layouts.append(QtWidgets.QVBoxLayout())
        self.frames.append(QtWidgets.QFrame())
        self.tab_ui.append(Ui_ConceptFrame(self.frames[self.current_plot_number],
                                           self.tsom_project))
        self.tab_layouts[self.current_plot_number].addWidget(self.frames[self.current_plot_number])
        self.tabs[self.current_plot_number].setLayout(self.tab_layouts[self.current_plot_number])
        self.current_plot_number += 1

    def save_time_series(self):
        self.save_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save time series',
                                                               'c:\\')[0]
        with open(str(self.save_path) + ".v", 'a+') as value_file:

            for element in self.tsom.ts.v:
                value_file.write(str(element) + " ")
            value_file.close()
        with open(str(self.save_path) + ".t", 'a+') as time_file:
            for element in self.tsom.ts.t:
                time_file.write(str(element) + " ")
            time_file.close()


    def generate_paper_figures(self):
        self.generate_paper_figures = QtWidgets.QDialog()
        self.ui = Ui_GeneratePaperFigures(self.generate_paper_figures)
        self.generate_paper_figures.exec()

    def retranslateUi(self, ProjectTab):
        _translate = QtCore.QCoreApplication.translate
        ProjectTab.setWindowTitle(_translate("ProjectTab", "ProjectTab"))
        self.Plots.setTabText(self.Plots.indexOf(self.NewTab), _translate("ProjectTab", "New Plot"))
        self.InputLabel.setText(_translate("ProjectTab", "<html><head/><body><p><span style=\" font-weight:600;\">Input data:</span></p></body></html>"))
        self.InputTextBrowser.setHtml(_translate("ProjectTab", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.FrameTimeSeries.setProperty("class", _translate("ProjectTab", "plot"))
        self.button_generate_paper_figures.setText(_translate("ProjectTab", "Generate Paper Figures"))
        self.scaling.setItemText(0, _translate("ProjectTab", "Linear Value Scale       "))
        self.scaling.setItemText(1, _translate("ProjectTab", "Logarithmic Value Scale   "))
        self.save_button.setText(_translate("ProjectTab", "Save Time Series"))
        self.newTimeSeries.setText(_translate("ProjectTab", "New Time Series"))

