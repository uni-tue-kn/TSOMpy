
from PyQt5 import QtCore, QtGui, QtWidgets
from Simulator import GeneratePaperFigures
from shutil import copyfile
import os


class Ui_GeneratePaperFigures(object):

    def __init__(self, GeneratePaperFigures):
        self.setupUi(GeneratePaperFigures)

    def setupUi(self, GeneratePaperFigures):
        GeneratePaperFigures.setObjectName("GeneratePaperFigures")
        GeneratePaperFigures.resize(467, 305)
        self.action = QtWidgets.QDialogButtonBox(GeneratePaperFigures)
        self.action.setGeometry(QtCore.QRect(110, 250, 341, 32))
        self.action.setOrientation(QtCore.Qt.Horizontal)
        self.action.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.action.setObjectName("action")
        self.label_info = QtWidgets.QLabel(GeneratePaperFigures)
        self.label_info.setGeometry(QtCore.QRect(20, 61, 471, 61))
        self.label_info.setObjectName("label_info")
        self.path = QtWidgets.QTextEdit(GeneratePaperFigures)
        self.path.setGeometry(QtCore.QRect(20, 161, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.path.setFont(font)
        self.path.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.path.setObjectName("path")
        self.url_button = QtWidgets.QPushButton(GeneratePaperFigures)
        self.url_button.setGeometry(QtCore.QRect(350, 160, 101, 33))
        self.url_button.setObjectName("url_button")

        self.retranslateUi(GeneratePaperFigures)
        self.action.accepted.connect(GeneratePaperFigures.accept)
        self.action.rejected.connect(GeneratePaperFigures.reject)
        QtCore.QMetaObject.connectSlotsByName(GeneratePaperFigures)
        self.file_path = ""
        self.url_button.clicked.connect(self.get_url)
        self.action.accepted.connect(self.generate_figures)

    def get_url(self):
        self.file_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.path.setText(self.file_path)

    def generate_figures(self):
        if self.file_path != "":
            self.file_path = self.file_path + "/"
            GeneratePaperFigures.conference_paper_figures(self.file_path)

            copyfile(str(os.path.dirname(__file__)) + "/../Simulator/Papers/Demo_Online_Measurement_of_Time_Series.pdf",
                     str(self.file_path) + "Demo_Online_Measurement_of_Time_Series.pdf")

            copyfile(str(os.path.dirname(__file__)) + "/../Simulator/Papers/On_Moving_Averages,Histograms_and_Time-Dependent_Rates_for_Online_Measurement.pdf",
                     str(self.file_path) + "On_Moving_Averages,Histograms_and_Time-Dependent_Rates_for_Online_Measurement.pdf")

    def retranslateUi(self, GeneratePaperFigures):
        _translate = QtCore.QCoreApplication.translate
        GeneratePaperFigures.setWindowTitle(_translate("GeneratePaperFigures", "Generate Paper Figures"))
        self.label_info.setText(_translate("GeneratePaperFigures", "<html><head/><body><p><span style=\" font-size:12pt;\">Use the following directory to save</span></p><p><span style=\" font-size:12pt;\"> the figures  from the paper:<br/></span></p></body></html>"))
        self.path.setHtml(_translate("GeneratePaperFigures", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C:/</p></body></html>"))
        self.url_button.setText(_translate("GeneratePaperFigures", "URL"))

