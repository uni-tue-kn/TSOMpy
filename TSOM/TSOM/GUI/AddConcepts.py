
from PyQt5 import QtCore, QtGui, QtWidgets
from Simulator.Concepts.MAs import *
from Simulator.Concepts.TimeDependentMAs import *
from Simulator.Concepts.TimeDependentRMs import *
from Simulator.Concepts.TimeDependentMHs import *
from Simulator.TSOM import TSOM

class Ui_add_concept(object):
    def __init__(self, add_concept, concept_list, concept_names, colors, tsom):
        self.concept_list = concept_list
        self.concept_names = concept_names
        self.colors = colors
        self.index_of_concept = len(self.concept_list)
        self.setupUi(add_concept)
        self.tsom = tsom
        self.active = True

    def setupUi(self, add_concept):
        add_concept.setObjectName("add_concept")
        add_concept.resize(613, 487)
        self.action_button = QtWidgets.QDialogButtonBox(add_concept)
        self.action_button.setGeometry(QtCore.QRect(220, 420, 341, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.action_button.setFont(font)
        self.action_button.setOrientation(QtCore.Qt.Horizontal)
        self.action_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.action_button.setObjectName("action_button")
        self.label_concept = QtWidgets.QLabel(add_concept)
        self.label_concept.setGeometry(QtCore.QRect(50, 30, 101, 41))
        self.label_concept.setObjectName("label_concept")
        self.label_memory = QtWidgets.QLabel(add_concept)
        self.label_memory.setEnabled(True)
        self.label_memory.setGeometry(QtCore.QRect(270, 200, 71, 31))
        self.label_memory.setObjectName("label_memory")
        self.label_start_time = QtWidgets.QLabel(add_concept)
        self.label_start_time.setEnabled(True)
        self.label_start_time.setGeometry(QtCore.QRect(270, 250, 111, 31))
        self.label_start_time.setObjectName("label_start_time")
        self.input_n_bins = QtWidgets.QTextEdit(add_concept)
        self.input_n_bins.setEnabled(True)
        self.input_n_bins.setGeometry(QtCore.QRect(470, 245, 91, 31))
        self.input_n_bins.setObjectName("input_n_bins")
        self.concept_box = QtWidgets.QComboBox(add_concept)
        self.concept_box.setGeometry(QtCore.QRect(270, 31, 291, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.concept_box.setFont(font)
        self.concept_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.concept_box.setObjectName("concept_box")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.concept_box.addItem("")
        self.input_memory = QtWidgets.QTextEdit(add_concept)
        self.input_memory.setEnabled(True)
        self.input_memory.setGeometry(QtCore.QRect(470, 197, 91, 31))
        self.input_memory.setObjectName("input_memory")
        self.input_lable = QtWidgets.QTextEdit(add_concept)
        self.input_lable.setEnabled(True)
        self.input_lable.setGeometry(QtCore.QRect(470, 100, 91, 31))
        self.input_lable.setObjectName("input_lable")
        self.label_label = QtWidgets.QLabel(add_concept)
        self.label_label.setEnabled(True)
        self.label_label.setGeometry(QtCore.QRect(270, 100, 71, 31))
        self.label_label.setObjectName("label_label")
        self.label_line_color = QtWidgets.QLabel(add_concept)
        self.label_line_color.setEnabled(True)
        self.label_line_color.setGeometry(QtCore.QRect(270, 150, 111, 31))
        self.label_line_color.setObjectName("label_line_color")
        self.color = QtWidgets.QPushButton(add_concept)
        self.color.setGeometry(QtCore.QRect(540, 150, 21, 21))
        self.color.setText("")
        self.color.setObjectName("color")
        self.input_window_size = QtWidgets.QTextEdit(add_concept)
        self.input_window_size.setEnabled(True)
        self.input_window_size.setGeometry(QtCore.QRect(470, 295, 91, 31))
        self.input_window_size.setObjectName("input_window_size")
        self.label_window_size = QtWidgets.QLabel(add_concept)
        self.label_window_size.setEnabled(True)
        self.label_window_size.setGeometry(QtCore.QRect(270, 300, 111, 31))
        self.label_window_size.setObjectName("label_window_size")
        self.label_n_bins = QtWidgets.QLabel(add_concept)
        self.label_n_bins.setEnabled(True)
        self.label_n_bins.setGeometry(QtCore.QRect(270, 250, 181, 31))
        self.label_n_bins.setObjectName("label_n_bins")
        self.label_min = QtWidgets.QLabel(add_concept)
        self.label_min.setEnabled(True)
        self.label_min.setGeometry(QtCore.QRect(270, 300, 111, 31))
        self.label_min.setObjectName("label_min")
        self.input_max = QtWidgets.QTextEdit(add_concept)
        self.input_max.setEnabled(True)
        self.input_max.setGeometry(QtCore.QRect(470, 345, 91, 31))
        self.input_max.setObjectName("input_max")
        self.label_max = QtWidgets.QLabel(add_concept)
        self.label_max.setEnabled(True)
        self.label_max.setGeometry(QtCore.QRect(270, 350, 111, 31))
        self.label_max.setObjectName("label_max")
        self.input_start_time = QtWidgets.QTextEdit(add_concept)
        self.input_start_time.setEnabled(True)
        self.input_start_time.setGeometry(QtCore.QRect(470, 245, 91, 31))
        self.input_start_time.setObjectName("input_start_time")
        self.input_min = QtWidgets.QTextEdit(add_concept)
        self.input_min.setEnabled(True)
        self.input_min.setGeometry(QtCore.QRect(470, 295, 91, 31))
        self.input_min.setObjectName("input_min")
        self.Info_time_selection = QtWidgets.QLabel(add_concept)
        self.Info_time_selection.setGeometry(QtCore.QRect(-100, 150, 421, 191))
        self.Info_time_selection.setObjectName("Info_time_selection")

        self.retranslateUi(add_concept)
        self.action_button.accepted.connect(add_concept.accept)
        self.action_button.rejected.connect(add_concept.reject)
        QtCore.QMetaObject.connectSlotsByName(add_concept)
        self.initialize()

    def initialize(self):
        self.reset_window()
        self.action_button.button(self.action_button.Discard).setText("Delete")
        self.action_button.button(self.action_button.Ok).setText("Create")
        self.concept_box.currentIndexChanged.connect(self.show_input_boxes)
        self.action_button.accepted.connect(self.input_accepted)
        self.action_button.button(self.action_button.Save).clicked.connect(self.save_concept)
        self.action_button.button(self.action_button.Discard).clicked.connect(self.delete_concept)
        self.color.clicked.connect(self.get_color)
        self.color.setStyleSheet("background-color: " + self.colors[self.index_of_concept].name())
        self.input_memory.textChanged.connect(self.check_input)
        self.input_start_time.textChanged.connect(self.check_input)
        self.input_window_size.textChanged.connect(self.check_input)
        self.input_n_bins.textChanged.connect(self.check_input)
        self.input_max.textChanged.connect(self.check_input)
        self.input_min.textChanged.connect(self.check_input)
        self.concept_box.currentIndexChanged.connect(self.check_input)

    def get_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.color.setStyleSheet("background-color: " + color.name())
        self.colors[self.index_of_concept] = color

    def reset_window(self):
        self.action_button.setEnabled(True)
        if self.concept_list:
            if type(self.concept_list[0]) in TSOM.TimeDependentMHs:
                self.concept_box.model().item(2).setEnabled(False)
                self.concept_box.model().item(3).setEnabled(False)
                self.concept_box.model().item(4).setEnabled(False)
                self.concept_box.model().item(5).setEnabled(False)
                self.concept_box.model().item(6).setEnabled(False)
                self.concept_box.model().item(8).setEnabled(False)
                self.concept_box.model().item(9).setEnabled(False)
                self.concept_box.model().item(10).setEnabled(False)
                self.concept_box.model().item(11).setEnabled(False)
                self.concept_box.model().item(13).setEnabled(False)
                self.concept_box.model().item(14).setEnabled(False)
                self.concept_box.model().item(15).setEnabled(False)
                self.concept_box.model().item(16).setEnabled(False)
                self.concept_box.model().item(17).setEnabled(False)
                self.concept_box.model().item(18).setEnabled(False)
                self.concept_box.model().item(19).setEnabled(False)
                self.concept_box.model().item(20).setEnabled(False)
            else:
                self.concept_box.model().item(21).setEnabled(False)

        if self.concept_box.currentText() == "Choose Concept":
            self.action_button.setEnabled(False)

        self.input_lable.setVisible(False)
        self.input_memory.setVisible(False)
        self.input_start_time.setVisible(False)
        self.label_label.setVisible(False)
        self.label_memory.setVisible(False)
        self.label_start_time.setVisible(False)
        self.color.setVisible(False)
        self.label_line_color.setVisible(False)
        self.label_window_size.setVisible(False)
        self.input_window_size.setVisible(False)
        self.label_n_bins.setVisible(False)
        self.input_n_bins.setVisible(False)
        self.label_min.setVisible(False)
        self.input_min.setVisible(False)
        self.label_max.setVisible(False)
        self.input_max.setVisible(False)
        self.Info_time_selection.setVisible(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.concept_box.model().item(0).setEnabled(False)
        self.concept_box.model().item(0).setFont(font)
        self.concept_box.model().item(1).setEnabled(False)
        self.concept_box.model().item(1).setFont(font)
        self.concept_box.model().item(7).setEnabled(False)
        self.concept_box.model().item(7).setFont(font)
        self.concept_box.model().item(12).setEnabled(False)
        self.concept_box.model().item(12).setFont(font)
        self.concept_box.model().item(20).setEnabled(False)
        self.concept_box.model().item(20).setFont(font)

    def check_input(self):
        try:
            self.action_button.setEnabled(True)
            if int(self.input_memory.toPlainText()) <= 0:
                self.action_button.setEnabled(False)
            if self.concept_box.currentText() in [*TSOM.TimeDependentMA_labels, *TSOM.TimeDependentRMs_labels]:
                if float(self.input_start_time.toPlainText()) < 0:
                    self.action_button.setEnabled(False)
            if self.concept_box.currentText() in ["TDRM_DTWMA_UEMA", "TDRM_DTWMA_EMA"]:
                if int(self.input_window_size.toPlainText()) <= 0:
                    self.action_button.setEnabled(False)
            if self.concept_box.currentText() in TSOM.TimeDependentMHs_labels:
                if int(self.input_n_bins.toPlainText()) <= 0:
                    self.action_button.setEnabled(False)
                if (float(self.input_max.toPlainText()) <= float(self.input_min.toPlainText())):
                    self.action_button.setEnabled(False)
        except:
            self.action_button.setEnabled(False)

    def show_input_boxes(self):
        self.reset_window()
        self.input_lable.setVisible(True)
        self.input_memory.setVisible(True)
        self.label_label.setVisible(True)
        self.label_memory.setVisible(True)
        self.color.setVisible(True)
        self.label_line_color.setVisible(True)

        if self.concept_box.currentText() in [*TSOM.TimeDependentMA_labels, *TSOM.TimeDependentRMs_labels]:

            if self.concept_box.currentText() in ["TDRM_DTWMA_UEMA", "TDRM_DTWMA_EMA"]:
                self.label_window_size.setVisible(True)
                self.input_window_size.setVisible(True)

            self.label_start_time.setVisible(True)
            self.input_start_time.setVisible(True)

        if self.concept_box.currentText() in TSOM.TimeDependentMHs_labels:
            self.label_n_bins.setVisible(True)
            self.input_n_bins.setVisible(True)
            self.label_min.setVisible(True)
            self.input_min.setVisible(True)
            self.label_max.setVisible(True)
            self.input_max.setVisible(True)
            self.Info_time_selection.setVisible(True)

    def delete_concept(self):
        if self.concept_list:
            self.concept_list.pop(self.index_of_concept)
            self.concept_names.pop(self.index_of_concept)
            self.colors.pop(self.index_of_concept)
            self.active = False
        self.action_button.button(self.action_button.Cancel).click()

    def save_concept(self):
        self.input_accepted()
        self.save_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save Concept series',
                                                               'c:\\')[0]
        time_vector, value_vector = self.tsom.get_ltf(self.concept_list[self.index_of_concept])
        with open(str(self.save_path) + ".v", 'a+') as value_file:
            for element in value_vector:
                value_file.write(str(element) + " ")
            value_file.close()

        with open(str(self.save_path) + ".t", 'a+') as time_file:
            for element in time_vector:
                time_file.write(str(element) + " ")
            time_file.close()

    def is_active(self):
        return self.active

    def input_accepted(self):
        if self.concept_box.currentText() in TSOM.MA_labels:
            concept = self.concept_box.currentText() + "(" + self.input_memory.toPlainText() + ")"
            concept_label = self.concept_box.currentText() + "(mem: " + self.input_memory.toPlainText() + ")"
        elif self.concept_box.currentText() in ["TDRM_DTWMA_UEMA", "TDRM_DTWMA_EMA"]:
            concept = self.concept_box.currentText() + "(" + self.input_memory.toPlainText() + "," + \
                      self.input_start_time.toPlainText() + "," + self.input_window_size.toPlainText() + ")"
            concept_label = self.concept_box.currentText() + "(mem: " + self.input_memory.toPlainText() + \
                            ", t_start: " + \
                            self.input_start_time.toPlainText() + ", w_size: " + self.input_window_size.toPlainText() + ")"

        elif self.concept_box.currentText() in [*TSOM.TimeDependentMA_labels, *TSOM.TimeDependentRMs_labels]:

            concept = self.concept_box.currentText() + "(" + self.input_memory.toPlainText() + "," + \
                      self.input_start_time.toPlainText() + ")"
            concept_label = self.concept_box.currentText() + "(mem: " + self.input_memory.toPlainText() + ", t_start: " + \
                            self.input_start_time.toPlainText() + ")"
        elif self.concept_box.currentText() in TSOM.TimeDependentMHs_labels:
            concept = self.concept_box.currentText() + "(" + self.input_n_bins.toPlainText() + "," + \
                      self.input_min.toPlainText() + "," + self.input_max.toPlainText() + "," + \
                      self.input_memory.toPlainText() + ")"
            concept_label = self.concept_box.currentText() + "(n_bins: " + self.input_n_bins.toPlainText() + ", min: " + \
                      self.input_min.toPlainText() + ", max: " + self.input_max.toPlainText() + ", mem: " + \
                      self.input_memory.toPlainText() + ")"
        else:
            raise NotImplementedError

        label = self.input_lable.toPlainText()

        if label in ["", "Concept"]:
            self.add_concept_from_string(concept, concept_label)
        else:
            self.add_concept_from_string(concept, label)

    def add_concept_from_string(self, concept, label):

        if self.index_of_concept == len(self.concept_list):
            self.concept_list.append(eval(concept))
            self.concept_names.append(label)
        else:
            self.concept_list.pop(self.index_of_concept)
            self.concept_names.pop(self.index_of_concept)
            self.concept_list.insert(self.index_of_concept, eval(concept))
            self.concept_names.insert(self.index_of_concept, label)

    def retranslateUi(self, add_concept):
        _translate = QtCore.QCoreApplication.translate
        add_concept.setWindowTitle(_translate("add_concept", "Add Concept"))
        self.label_concept.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Concept:</span></p></body></html>"))
        self.label_memory.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Memory:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.label_start_time.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Start time:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.input_n_bins.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.concept_box.setItemText(0, _translate("add_concept", "Choose Concept"))
        self.concept_box.setItemText(1, _translate("add_concept", "MAs"))
        self.concept_box.setItemText(2, _translate("add_concept", "CumMean"))
        self.concept_box.setItemText(3, _translate("add_concept", "WMA"))
        self.concept_box.setItemText(4, _translate("add_concept", "DWMA"))
        self.concept_box.setItemText(5, _translate("add_concept", "UEMA"))
        self.concept_box.setItemText(6, _translate("add_concept", "EMA"))
        self.concept_box.setItemText(7, _translate("add_concept", "TimeDependentMAs"))
        self.concept_box.setItemText(8, _translate("add_concept", "TWMA"))
        self.concept_box.setItemText(9, _translate("add_concept", "DTWMA"))
        self.concept_box.setItemText(10, _translate("add_concept", "TEMA"))
        self.concept_box.setItemText(11, _translate("add_concept", "UTEMA"))
        self.concept_box.setItemText(12, _translate("add_concept", "TimeDependentRMs"))
        self.concept_box.setItemText(13, _translate("add_concept", "TDRMCumMean"))
        self.concept_box.setItemText(14, _translate("add_concept", "TDRM_TWMA"))
        self.concept_box.setItemText(15, _translate("add_concept", "TDRM_DTWMA"))
        self.concept_box.setItemText(16, _translate("add_concept", "TDRM_UTEMA"))
        self.concept_box.setItemText(17, _translate("add_concept", "TDRM_UTEMA_CPA"))
        self.concept_box.setItemText(18, _translate("add_concept", "TDRM_DTWMA_EMA"))
        self.concept_box.setItemText(19, _translate("add_concept", "TDRM_DTWMA_UEMA"))
        self.concept_box.setItemText(20, _translate("add_concept", "TimeDependentMHs"))
        self.concept_box.setItemText(21, _translate("add_concept", "TDH_UTEMA"))
        self.input_memory.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.input_lable.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Concept</p></body></html>"))
        self.label_label.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Label:</span></p></body></html>"))
        self.label_line_color.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Line color:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.input_window_size.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_window_size.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Window size:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.label_n_bins.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of bins:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.label_min.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Minimum:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.input_max.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_max.setText(_translate("add_concept", "<html><head/><body><p><span style=\" font-size:10pt;\">Maximum:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.input_start_time.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.input_min.setHtml(_translate("add_concept", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.Info_time_selection.setText(_translate("add_concept", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#981315;\">Select the time</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#981315;\">instant for calculating</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#981315;\">the moving histogram</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#981315;\">by clicking in the</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#981315;\">time series plot.</span></p></body></html>"))

