
from PyQt5 import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from Simulator.TSOM import TSOM

from matplotlib.figure import Figure

from GUI.AddConcepts import Ui_add_concept


class Ui_ConceptFrame(object):

    def __init__(self, ConceptFrame, tsom_project):
        self.tsom = tsom_project

        self.concept_list = []
        self.concept_names = []
        self.t_stop = -1
        self.colors = [QtGui.QColor('#dd0000'),
                       QtGui.QColor('#2804dd'),
                       QtGui.QColor('#dd6400'),
                       QtGui.QColor('#3a78dd'),
                       QtGui.QColor('#a138dd'),
                       QtGui.QColor('#41dd2f'),
                       QtGui.QColor('#3ab7dd'),
                       QtGui.QColor('#d4dd19'),
                       QtGui.QColor('#8add7d'),
                       QtGui.QColor('#02dd1c'),
                       QtGui.QColor('#7883dd'),
                       QtGui.QColor('#dddddd'),
                       QtGui.QColor('#0a8f03'),
                       QtGui.QColor('#3d6e8f'),
                       QtGui.QColor('#8f5b5c'),
                       QtGui.QColor('#2b8f76'),
                       QtGui.QColor('#054c8f'),
                       QtGui.QColor('#b7cddd'),
                       QtGui.QColor('#8f3c81'),
                       QtGui.QColor('#55ffff'),
                       ]

        self.setupUi(ConceptFrame)

    def setupUi(self, ConceptFrame):
        ConceptFrame.setObjectName("ConceptFrame")
        ConceptFrame.resize(1084, 424)
        ConceptFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        ConceptFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        ConceptFrame.setLineWidth(0)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ConceptFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FrameConcepts = QtWidgets.QFrame(ConceptFrame)
        self.FrameConcepts.setMaximumSize(QtCore.QSize(323, 16777215))
        self.FrameConcepts.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FrameConcepts.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FrameConcepts.setLineWidth(0)
        self.FrameConcepts.setObjectName("FrameConcepts")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.FrameConcepts)
        self.verticalLayout_6.setContentsMargins(0, -1, 11, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ConceptLable = QtWidgets.QLabel(self.FrameConcepts)
        self.ConceptLable.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ConceptLable.setFont(font)
        self.ConceptLable.setLineWidth(0)
        self.ConceptLable.setObjectName("ConceptLable")
        self.verticalLayout_6.addWidget(self.ConceptLable)
        self.ListOfConcepts = QtWidgets.QListWidget(self.FrameConcepts)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ListOfConcepts.setFont(font)
        self.ListOfConcepts.setFrameShape(QtWidgets.QFrame.Box)
        self.ListOfConcepts.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ListOfConcepts.setLineWidth(1)
        self.ListOfConcepts.setObjectName("ListOfConcepts")
        self.verticalLayout_6.addWidget(self.ListOfConcepts)
        self.frame_add_concept = QtWidgets.QFrame(self.FrameConcepts)
        self.frame_add_concept.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_add_concept.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_concept.setLineWidth(0)
        self.frame_add_concept.setObjectName("frame_add_concept")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_add_concept)
        self.horizontalLayout_2.setContentsMargins(0, 11, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AddConcepts = QtWidgets.QPushButton(self.frame_add_concept)
        self.AddConcepts.setMaximumSize(QtCore.QSize(143, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddConcepts.setFont(font)
        self.AddConcepts.setObjectName("AddConcepts")
        self.horizontalLayout_2.addWidget(self.AddConcepts)
        self.frame_2 = QtWidgets.QFrame(self.frame_add_concept)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_6.addWidget(self.frame_add_concept)
        self.frame = QtWidgets.QFrame(self.FrameConcepts)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_eval_concepts = QtWidgets.QLabel(self.frame)
        self.label_eval_concepts.setGeometry(QtCore.QRect(0, 0, 231, 45))
        self.label_eval_concepts.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_eval_concepts.setFont(font)
        self.label_eval_concepts.setLineWidth(0)
        self.label_eval_concepts.setObjectName("label_eval_concepts")
        self.verticalLayout_6.addWidget(self.frame)
        self.textBrowser_eval_concepts = QtWidgets.QTextBrowser(self.FrameConcepts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_eval_concepts.setFont(font)
        self.textBrowser_eval_concepts.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_eval_concepts.setLineWidth(1)
        self.textBrowser_eval_concepts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_eval_concepts.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_eval_concepts.setObjectName("textBrowser_eval_concepts")
        self.verticalLayout_6.addWidget(self.textBrowser_eval_concepts)
        self.horizontalLayout.addWidget(self.FrameConcepts)
        self.FrameDisplayConcepts = QtWidgets.QFrame(ConceptFrame)
        self.FrameDisplayConcepts.setFrameShape(QtWidgets.QFrame.Box)
        self.FrameDisplayConcepts.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FrameDisplayConcepts.setObjectName("FrameDisplayConcepts")
        self.concept_plot_layout = QtWidgets.QVBoxLayout(self.FrameDisplayConcepts)
        self.concept_plot_layout.setContentsMargins(0, 0, 0, 0)
        self.concept_plot_layout.setSpacing(0)
        self.concept_plot_layout.setObjectName("concept_plot_layout")
        self.horizontalLayout.addWidget(self.FrameDisplayConcepts)

        self.retranslateUi(ConceptFrame)
        QtCore.QMetaObject.connectSlotsByName(ConceptFrame)

        self.initialize()

    def initialize(self):
        self.figure = Figure()
        self.evalualtion = ""
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = None
        self.concept_dialogs = []
        self.ui_concept_list = []
        self.progressBar.setVisible(False)
        self.logic()


    def logic(self):
        self.AddConcepts.clicked.connect(self.on_add_concept_button_clicked)
        self.ListOfConcepts.itemClicked.connect(self.on_concept_clicked)

    def on_concept_clicked(self, item):

        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)
        index = self.ListOfConcepts.row(item)
        if item.text() == "Rate difference":
            color = QtWidgets.QColorDialog.getColor()
            self.colors[index] = color
            item.setForeground(color)
        else:
            self.add_concept = self.concept_dialogs[index]
            self.ui_concept = self.ui_concept_list[index]
            self.add_concept.exec()

            if not self.ui_concept.is_active():
                self.concept_dialogs.pop(index)
                self.ui_concept_list.pop(index)
                for ui in range(index, len(self.ui_concept_list)):
                    self.ui_concept_list[ui].index_of_concept -= 1

            self.update_concept_list()
        self.draw_concepts()
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)

    def update_concept_list(self):
        self.ListOfConcepts.clear()
        self.ListOfConcepts.addItems(self.concept_names)
        for item_index in range(len(self.concept_names)):
            curr_item = self.ListOfConcepts.item(item_index)
            curr_item.setForeground(self.colors[item_index])
        if "Rate difference" in self.concept_names:
            self.concept_names.remove("Rate difference")


    def on_add_concept_button_clicked(self):
        try:
            self.progressBar.setVisible(True)
            self.add_concept = QtWidgets.QDialog()
            self.ui_concept = Ui_add_concept(self.add_concept, self.concept_list, self.concept_names,
                                             self.colors, self.tsom)
            self.add_concept.exec()
            self.update_concept_list()
            self.concept_dialogs.append(self.add_concept)
            self.ui_concept_list.append(self.ui_concept)
            if self.tsom.ts.t:
                self.t_stop = self.tsom.ts.t[-1]

            self.draw_concepts()
            self.progressBar.setVisible(False)
            self.progressBar.setValue(0)
            self.colors.append(QtGui.QColor('#000000'))
        except:
            self.progressBar.setValue(0)
            self.progressBar.setVisible(False)
            if self.canvas:
                self.concept_plot_layout.removeWidget(self.canvas)
            if self.toolbar:
                self.concept_plot_layout.removeWidget(self.toolbar)
            print("No Concept")

    def draw_concepts(self):
        if self.canvas:
            self.concept_plot_layout.removeWidget(self.canvas)
        if self.toolbar:
            self.concept_plot_layout.removeWidget(self.toolbar)

        if self.concept_list:

            if type(self.concept_list[-1]) in TSOM.TimeDependentMHs:

                self.figure = self.tsom.get_calculated_histograms(self.concept_list,
                                                                  self.t_stop, self.colors)

            else:
                self.figure, self.evalualtion = self.tsom.get_calculated_plot(self.concept_list,
                                                                              self.concept_names,
                                                                              self.colors,
                                                                              self.progressBar)

        self.canvas = FigureCanvas(self.figure)
        self.concept_plot_layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.FrameDisplayConcepts, coordinates=True)
        self.concept_plot_layout.addWidget(self.toolbar)

        self.textBrowser_eval_concepts.setText(self.evalualtion)
        self.update_concept_list()

    def set_t_stop(self, t_stop):
        if t_stop != -1:
            self.t_stop = t_stop
            self.draw_concepts()

    def initialize_t_stop(self, t_stop):
        self.t_stop = t_stop



    def retranslateUi(self, ConceptFrame):
        _translate = QtCore.QCoreApplication.translate
        ConceptFrame.setWindowTitle(_translate("ConceptFrame", "Frame"))
        self.ConceptLable.setText(_translate("ConceptFrame", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Apply Concepts:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.AddConcepts.setText(_translate("ConceptFrame", "Add Concepts"))
        self.label_eval_concepts.setText(_translate("ConceptFrame", "<html><head/><body><p><span style=\" font-weight:600;\">Evaluation of Concepts:</span></p></body></html>"))
        self.textBrowser_eval_concepts.setHtml(_translate("ConceptFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.FrameDisplayConcepts.setProperty("class", _translate("ConceptFrame", "plot_concepts"))
