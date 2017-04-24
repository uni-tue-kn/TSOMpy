from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Simulator.RandomProcess import *
from GUI.Error.FileLoadError import Ui_LoadErrorDialog
from GUI.Error.MaximumTimeError import Ui_MaximumTimeError


class Ui_InputDialog(object):
    def __init__(self, InputDialog, tab_tsom):
        self.tsom = tab_tsom
        self._max_number_of_values = 500000
        self.setupUi(InputDialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1187, 932)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InputType = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.InputType.setFont(font)
        self.InputType.setStyleSheet("")
        self.InputType.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.InputType.setObjectName("InputType")
        self.equally = QtWidgets.QWidget()
        self.equally.setObjectName("equally")
        self.Lable_sv = QtWidgets.QLabel(self.equally)
        self.Lable_sv.setGeometry(QtCore.QRect(90, 110, 211, 41))
        self.Lable_sv.setObjectName("Lable_sv")
        self.path = QtWidgets.QTextEdit(self.equally)
        self.path.setGeometry(QtCore.QRect(410, 181, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.path.setFont(font)
        self.path.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.path.setObjectName("path")
        self.url_button = QtWidgets.QPushButton(self.equally)
        self.url_button.setGeometry(QtCore.QRect(910, 180, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.url_button.setFont(font)
        self.url_button.setObjectName("url_button")
        self.label_lff = QtWidgets.QLabel(self.equally)
        self.label_lff.setGeometry(QtCore.QRect(140, 190, 140, 24))
        self.label_lff.setObjectName("label_lff")
        self.label_tv = QtWidgets.QLabel(self.equally)
        self.label_tv.setGeometry(QtCore.QRect(90, 310, 201, 41))
        self.label_tv.setObjectName("label_tv")
        self.label_stv = QtWidgets.QLabel(self.equally)
        self.label_stv.setGeometry(QtCore.QRect(140, 390, 140, 24))
        self.label_stv.setObjectName("label_stv")
        self.label_si = QtWidgets.QLabel(self.equally)
        self.label_si.setGeometry(QtCore.QRect(140, 470, 181, 24))
        self.label_si.setObjectName("label_si")
        self.start_value = QtWidgets.QTextEdit(self.equally)
        self.start_value.setGeometry(QtCore.QRect(910, 387, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        self.start_value.setFont(font)
        self.start_value.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.start_value.setObjectName("start_value")
        self.spacing_interval = QtWidgets.QTextEdit(self.equally)
        self.spacing_interval.setGeometry(QtCore.QRect(910, 466, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.spacing_interval.setFont(font)
        self.spacing_interval.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spacing_interval.setObjectName("spacing_interval")
        self.InputType.addTab(self.equally, "")
        self.unequally = QtWidgets.QWidget()
        self.unequally.setObjectName("unequally")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.unequally)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_sv = QtWidgets.QFrame(self.unequally)
        self.frame_sv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_sv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_sv.setLineWidth(0)
        self.frame_sv.setObjectName("frame_sv")
        self.radioButton_constant_ss = QtWidgets.QRadioButton(self.frame_sv)
        self.radioButton_constant_ss.setGeometry(QtCore.QRect(140, 190, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_constant_ss.setFont(font)
        self.radioButton_constant_ss.setObjectName("radioButton_constant_ss")
        self.te_const_ss = QtWidgets.QTextEdit(self.frame_sv)
        self.te_const_ss.setEnabled(False)
        self.te_const_ss.setGeometry(QtCore.QRect(960, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        self.te_const_ss.setFont(font)
        self.te_const_ss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.te_const_ss.setObjectName("te_const_ss")
        self.label_sv_u = QtWidgets.QLabel(self.frame_sv)
        self.label_sv_u.setGeometry(QtCore.QRect(80, 40, 211, 41))
        self.label_sv_u.setObjectName("label_sv_u")
        self.radioButton_distr_ss = QtWidgets.QRadioButton(self.frame_sv)
        self.radioButton_distr_ss.setGeometry(QtCore.QRect(140, 270, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_distr_ss.setFont(font)
        self.radioButton_distr_ss.setObjectName("radioButton_distr_ss")
        self.url_button_sv = QtWidgets.QPushButton(self.frame_sv)
        self.url_button_sv.setEnabled(False)
        self.url_button_sv.setGeometry(QtCore.QRect(960, 105, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.url_button_sv.setFont(font)
        self.url_button_sv.setObjectName("url_button_sv")
        self.radioButton_lff = QtWidgets.QRadioButton(self.frame_sv)
        self.radioButton_lff.setGeometry(QtCore.QRect(140, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_lff.setFont(font)
        self.radioButton_lff.setObjectName("radioButton_lff")
        self.url_sv = QtWidgets.QTextEdit(self.frame_sv)
        self.url_sv.setEnabled(False)
        self.url_sv.setGeometry(QtCore.QRect(490, 106, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.url_sv.setFont(font)
        self.url_sv.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.url_sv.setObjectName("url_sv")
        self.comboBox_sv = QtWidgets.QComboBox(self.frame_sv)
        self.comboBox_sv.setEnabled(False)
        self.comboBox_sv.setGeometry(QtCore.QRect(860, 270, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_sv.setFont(font)
        self.comboBox_sv.setObjectName("comboBox_sv")
        self.comboBox_sv.addItem("")
        self.comboBox_sv.addItem("")
        self.comboBox_sv.addItem("")
        self.comboBox_sv.addItem("")
        self.label_seed_ss = QtWidgets.QLabel(self.frame_sv)
        self.label_seed_ss.setEnabled(True)
        self.label_seed_ss.setGeometry(QtCore.QRect(790, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_seed_ss.setFont(font)
        self.label_seed_ss.setObjectName("label_seed_ss")
        self.seed_input_ss = QtWidgets.QTextEdit(self.frame_sv)
        self.seed_input_ss.setEnabled(True)
        self.seed_input_ss.setGeometry(QtCore.QRect(960, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.seed_input_ss.setFont(font)
        self.seed_input_ss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.seed_input_ss.setObjectName("seed_input_ss")
        self.label_mean_ss = QtWidgets.QLabel(self.frame_sv)
        self.label_mean_ss.setEnabled(True)
        self.label_mean_ss.setGeometry(QtCore.QRect(370, 320, 181, 31))
        self.label_mean_ss.setObjectName("label_mean_ss")
        self.input_minimum_ss = QtWidgets.QTextEdit(self.frame_sv)
        self.input_minimum_ss.setEnabled(True)
        self.input_minimum_ss.setGeometry(QtCore.QRect(590, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.input_minimum_ss.setFont(font)
        self.input_minimum_ss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_minimum_ss.setObjectName("input_minimum_ss")
        self.label_maximum_ss = QtWidgets.QLabel(self.frame_sv)
        self.label_maximum_ss.setEnabled(True)
        self.label_maximum_ss.setGeometry(QtCore.QRect(370, 370, 151, 31))
        self.label_maximum_ss.setObjectName("label_maximum_ss")
        self.input_maximum_ss = QtWidgets.QTextEdit(self.frame_sv)
        self.input_maximum_ss.setEnabled(True)
        self.input_maximum_ss.setGeometry(QtCore.QRect(590, 370, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.input_maximum_ss.setFont(font)
        self.input_maximum_ss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_maximum_ss.setObjectName("input_maximum_ss")
        self.label_minimum_ss = QtWidgets.QLabel(self.frame_sv)
        self.label_minimum_ss.setEnabled(True)
        self.label_minimum_ss.setGeometry(QtCore.QRect(370, 320, 181, 31))
        self.label_minimum_ss.setObjectName("label_minimum_ss")
        self.input_mean_ss = QtWidgets.QTextEdit(self.frame_sv)
        self.input_mean_ss.setEnabled(True)
        self.input_mean_ss.setGeometry(QtCore.QRect(590, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.input_mean_ss.setFont(font)
        self.input_mean_ss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_mean_ss.setObjectName("input_mean_ss")
        self.label_number_trials = QtWidgets.QLabel(self.frame_sv)
        self.label_number_trials.setGeometry(QtCore.QRect(370, 325, 241, 18))
        self.label_number_trials.setObjectName("label_number_trials")
        self.label_probability = QtWidgets.QLabel(self.frame_sv)
        self.label_probability.setGeometry(QtCore.QRect(370, 374, 191, 21))
        self.label_probability.setObjectName("label_probability")
        self.input_trials = QtWidgets.QTextEdit(self.frame_sv)
        self.input_trials.setEnabled(True)
        self.input_trials.setGeometry(QtCore.QRect(590, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.input_trials.setFont(font)
        self.input_trials.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_trials.setObjectName("input_trials")
        self.input_probability = QtWidgets.QTextEdit(self.frame_sv)
        self.input_probability.setEnabled(True)
        self.input_probability.setGeometry(QtCore.QRect(590, 370, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.input_probability.setFont(font)
        self.input_probability.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_probability.setObjectName("input_probability")
        self.verticalLayout_2.addWidget(self.frame_sv)
        self.frame_tv = QtWidgets.QFrame(self.unequally)
        self.frame_tv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_tv.setLineWidth(0)
        self.frame_tv.setObjectName("frame_tv")
        self.radioButton_tv_lff = QtWidgets.QRadioButton(self.frame_tv)
        self.radioButton_tv_lff.setGeometry(QtCore.QRect(150, 90, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_tv_lff.setFont(font)
        self.radioButton_tv_lff.setObjectName("radioButton_tv_lff")
        self.radioButton_tv_distr = QtWidgets.QRadioButton(self.frame_tv)
        self.radioButton_tv_distr.setGeometry(QtCore.QRect(150, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_tv_distr.setFont(font)
        self.radioButton_tv_distr.setObjectName("radioButton_tv_distr")
        self.label_tv_ue = QtWidgets.QLabel(self.frame_tv)
        self.label_tv_ue.setGeometry(QtCore.QRect(90, 20, 201, 41))
        self.label_tv_ue.setObjectName("label_tv_ue")
        self.url_tv = QtWidgets.QTextEdit(self.frame_tv)
        self.url_tv.setEnabled(False)
        self.url_tv.setGeometry(QtCore.QRect(500, 91, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.url_tv.setFont(font)
        self.url_tv.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.url_tv.setObjectName("url_tv")
        self.pushButton_url_tv = QtWidgets.QPushButton(self.frame_tv)
        self.pushButton_url_tv.setEnabled(False)
        self.pushButton_url_tv.setGeometry(QtCore.QRect(970, 90, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_url_tv.setFont(font)
        self.pushButton_url_tv.setObjectName("pushButton_url_tv")
        self.comboBox_tv = QtWidgets.QComboBox(self.frame_tv)
        self.comboBox_tv.setEnabled(False)
        self.comboBox_tv.setGeometry(QtCore.QRect(870, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_tv.setFont(font)
        self.comboBox_tv.setObjectName("comboBox_tv")
        self.comboBox_tv.addItem("")
        self.comboBox_tv.addItem("")
        self.comboBox_tv.addItem("")
        self.seed = QtWidgets.QLabel(self.frame_tv)
        self.seed.setEnabled(True)
        self.seed.setGeometry(QtCore.QRect(800, 230, 61, 31))
        self.seed.setObjectName("seed")
        self.mean_iat = QtWidgets.QLabel(self.frame_tv)
        self.mean_iat.setEnabled(True)
        self.mean_iat.setGeometry(QtCore.QRect(370, 230, 221, 31))
        self.mean_iat.setObjectName("mean_iat")
        self.tstart = QtWidgets.QLabel(self.frame_tv)
        self.tstart.setEnabled(True)
        self.tstart.setGeometry(QtCore.QRect(800, 280, 121, 31))
        self.tstart.setObjectName("tstart")
        self.cvar = QtWidgets.QLabel(self.frame_tv)
        self.cvar.setEnabled(True)
        self.cvar.setGeometry(QtCore.QRect(370, 280, 61, 31))
        self.cvar.setObjectName("cvar")
        self.seedInput = QtWidgets.QTextEdit(self.frame_tv)
        self.seedInput.setEnabled(True)
        self.seedInput.setGeometry(QtCore.QRect(970, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.seedInput.setFont(font)
        self.seedInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.seedInput.setObjectName("seedInput")
        self.meanInput = QtWidgets.QTextEdit(self.frame_tv)
        self.meanInput.setEnabled(True)
        self.meanInput.setGeometry(QtCore.QRect(600, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.meanInput.setFont(font)
        self.meanInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.meanInput.setObjectName("meanInput")
        self.tstartInput = QtWidgets.QTextEdit(self.frame_tv)
        self.tstartInput.setEnabled(True)
        self.tstartInput.setGeometry(QtCore.QRect(970, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.tstartInput.setFont(font)
        self.tstartInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tstartInput.setObjectName("tstartInput")
        self.cvarInput = QtWidgets.QTextEdit(self.frame_tv)
        self.cvarInput.setEnabled(True)
        self.cvarInput.setGeometry(QtCore.QRect(600, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.cvarInput.setFont(font)
        self.cvarInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cvarInput.setObjectName("cvarInput")
        self.tstop = QtWidgets.QLabel(self.frame_tv)
        self.tstop.setEnabled(True)
        self.tstop.setGeometry(QtCore.QRect(800, 330, 121, 31))
        self.tstop.setObjectName("tstop")
        self.tstopInput = QtWidgets.QTextEdit(self.frame_tv)
        self.tstopInput.setEnabled(True)
        self.tstopInput.setGeometry(QtCore.QRect(970, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        self.tstopInput.setFont(font)
        self.tstopInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tstopInput.setObjectName("tstopInput")
        self.verticalLayout_2.addWidget(self.frame_tv)
        self.InputType.addTab(self.unequally, "")
        self.verticalLayout.addWidget(self.InputType)
        self.action = QtWidgets.QDialogButtonBox(Dialog)
        self.action.setOrientation(QtCore.Qt.Horizontal)
        self.action.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Retry)
        self.action.setObjectName("action")
        self.verticalLayout.addWidget(self.action)

        self.retranslateUi(Dialog)
        self.InputType.setCurrentIndex(0)
        self.action.accepted.connect(Dialog.accept)
        self.action.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.initialize()

    def initialize(self):
        self.input_logic()
        self.action.button(self.action.Retry).setText("Append")
        self.action.button(self.action.Ok).setText("Create")
        self.radioButton_lff.setChecked(True)
        self.radioButton_tv_lff.setChecked(True)
        self.seed.setVisible(False)
        self.seedInput.setVisible(False)
        self.mean_iat.setVisible(False)
        self.meanInput.setVisible(False)
        self.tstart.setVisible(False)
        self.tstartInput.setVisible(False)
        self.cvar.setVisible(False)
        self.cvarInput.setVisible(False)
        self.tstop.setVisible(False)
        self.tstopInput.setVisible(False)
        self.label_mean_ss.setVisible(False)
        self.input_mean_ss.setVisible(False)
        self.label_seed_ss.setVisible(False)
        self.seed_input_ss.setVisible(False)
        self.label_minimum_ss.setVisible(False)
        self.input_minimum_ss.setVisible(False)
        self.label_maximum_ss.setVisible(False)
        self.input_maximum_ss.setVisible(False)


    def input_logic(self):
        self.url_button.pressed.connect(self.load_equally_spaced_sample_vector)
        self.url_button_sv.pressed.connect(self.load_sample_vector)
        self.pushButton_url_tv.pressed.connect(self.load_time_vector)
        self.action.button(self.action.Ok).clicked.connect(self.accepted)
        self.action.button(self.action.Retry).clicked.connect(self.append_time_series)
        self.radioButton_lff.toggled.connect(self.activate_load_sample_size)
        self.radioButton_constant_ss.toggled.connect(self.activate_constant_sample_size)
        self.radioButton_distr_ss.toggled.connect(self.activate_distributed_sample_size)
        self.radioButton_tv_lff.toggled.connect(self.activate_load_time)
        self.radioButton_tv_distr.toggled.connect(self.activate_distributed_time)
        self.comboBox_tv.currentIndexChanged.connect(self.set_parameters_visible)
        self.comboBox_sv.currentIndexChanged.connect(self.set_parameters_visible)
        self.comboBox_sv.currentIndexChanged.connect(self.set_parameters_visible)
        self.start_value.textChanged.connect(self.proof_equally_spaced_input)
        self.spacing_interval.textChanged.connect(self.proof_equally_spaced_input)
        self.te_const_ss.textChanged.connect(self.proof_unequally_spaced_input)
        self.meanInput.textChanged.connect(self.proof_unequally_spaced_input)
        self.cvarInput.textChanged.connect(self.proof_unequally_spaced_input)
        self.seedInput.textChanged.connect(self.proof_unequally_spaced_input)
        self.tstartInput.textChanged.connect(self.proof_unequally_spaced_input)
        self.tstopInput.textChanged.connect(self.proof_unequally_spaced_input)
        self.comboBox_sv.currentTextChanged.connect(self.proof_unequally_spaced_input)
        self.comboBox_tv.currentIndexChanged.connect(self.proof_unequally_spaced_input)
        self.InputType.currentChanged.connect(self.tab_changed)
        self.radioButton_lff.toggled.connect(self.proof_unequally_spaced_input)
        self.radioButton_constant_ss.toggled.connect(self.proof_unequally_spaced_input)
        self.radioButton_distr_ss.toggled.connect(self.proof_unequally_spaced_input)
        self.radioButton_tv_lff.toggled.connect(self.proof_unequally_spaced_input)
        self.radioButton_tv_distr.toggled.connect(self.proof_unequally_spaced_input)
        self.radioButton_lff.toggled.connect(self.set_parameters_visible)
        self.radioButton_constant_ss.toggled.connect(self.set_parameters_visible)
        self.radioButton_distr_ss.toggled.connect(self.set_parameters_visible)
        self.radioButton_tv_lff.toggled.connect(self.set_parameters_visible)
        self.radioButton_tv_distr.toggled.connect(self.set_parameters_visible)
        self.input_mean_ss.textChanged.connect(self.proof_unequally_spaced_input)
        self.input_maximum_ss.textChanged.connect(self.proof_unequally_spaced_input)
        self.input_minimum_ss.textChanged.connect(self.proof_unequally_spaced_input)
        self.seed_input_ss.textChanged.connect(self.proof_unequally_spaced_input)
        self.input_trials.textChanged.connect(self.proof_unequally_spaced_input)
        self.input_probability.textChanged.connect(self.proof_unequally_spaced_input)

    def proof_equally_spaced_input(self):
        try:
            self.action.setEnabled(True)
            float(self.start_value.toPlainText())
            float(self.spacing_interval.toPlainText())
            self.action.setEnabled(True)
            if float(self.spacing_interval.toPlainText()) <= 0:
                self.action.setEnabled(False)
        except:
            self.action.setEnabled(False)

    def proof_unequally_spaced_input(self):
        try:
            self.action.setEnabled(True)

            if self.radioButton_constant_ss.isChecked():
                if float(self.te_const_ss.toPlainText()) < 0:
                    self.action.setEnabled(False)

            if self.radioButton_distr_ss.isChecked():
                if self.radioButton_distr_ss.isChecked():
                    if self.comboBox_sv.currentText() == "Choose distribution":
                        self.action.setEnabled(False)
                    int(self.seed_input_ss.toPlainText())
            if float(self.seed_input_ss.toPlainText()) < 0:
                self.action.setEnabled(False)
            if self.comboBox_sv.currentText() == "Exponential distribution":
                if float(self.input_mean_ss.toPlainText()) <= 0:
                    self.action.setEnabled(False)
            if self.comboBox_sv.currentText() == "Uniform distribution":
                if float(self.input_minimum_ss.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.input_maximum_ss.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.input_minimum_ss.toPlainText()) >= float(self.input_maximum_ss.toPlainText()):
                    self.action.setEnabled(False)
            if self.comboBox_sv.currentText() == "Binomial distribution":
                if float(self.input_probability.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.input_probability.toPlainText()) > 1:
                    self.action.setEnabled(False)
                int(self.input_trials.toPlainText())

            if self.radioButton_tv_distr.isChecked():
                if float(self.meanInput.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.cvarInput.toPlainText()) <= 0:
                    self.action.setEnabled(False)
                if float(self.seedInput.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.tstartInput.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if float(self.tstopInput.toPlainText()) < 0:
                    self.action.setEnabled(False)
                if self.comboBox_tv.currentText() == "Choose distribution":
                    self.action.setEnabled(False)

        except:
            self.action.setEnabled(False)

    def tab_changed(self):
        if self.InputType.currentIndex() == 0:
            self.proof_equally_spaced_input()
        else:
            self.proof_unequally_spaced_input()

    def load_equally_spaced_sample_vector(self):
        file_path = QFileDialog.getOpenFileName(None, 'Open file',
                                                'c:\\', "*.v")[0]
        self.path.setText(file_path)

    def load_sample_vector(self):
        file_path = QFileDialog.getOpenFileName(None, 'Open file',
                                                'c:\\', "*.v")[0]
        self.url_sv.setText(file_path)

    def load_time_vector(self):
        file_path = QFileDialog.getOpenFileName(None, 'Open file',
                                                'c:\\', "*.t")[0]
        self.url_tv.setText(file_path)

    def set_parameters_visible(self):
        self.seed.setVisible(False)
        self.seedInput.setVisible(False)
        self.mean_iat.setVisible(False)
        self.meanInput.setVisible(False)
        self.tstart.setVisible(False)
        self.tstartInput.setVisible(False)
        self.cvar.setVisible(False)
        self.cvarInput.setVisible(False)
        self.tstop.setVisible(False)
        self.tstopInput.setVisible(False)
        self.label_mean_ss.setVisible(False)
        self.input_mean_ss.setVisible(False)
        self.label_seed_ss.setVisible(False)
        self.seed_input_ss.setVisible(False)
        self.label_minimum_ss.setVisible(False)
        self.input_minimum_ss.setVisible(False)
        self.label_maximum_ss.setVisible(False)
        self.input_maximum_ss.setVisible(False)
        self.tstopInput.setVisible(False)
        self.input_trials.setVisible(False)
        self.input_probability.setVisible(False)
        self.label_number_trials.setVisible(False)
        self.label_probability.setVisible(False)


        if self.radioButton_distr_ss.isChecked():
            if self.comboBox_sv.currentText() == "Exponential distribution":
                self.label_mean_ss.setVisible(True)
                self.input_mean_ss.setVisible(True)
                self.label_seed_ss.setVisible(True)
                self.seed_input_ss.setVisible(True)


            if self.comboBox_sv.currentText() == "Uniform distribution":
                self.input_minimum_ss.setVisible(True)
                self.label_minimum_ss.setVisible(True)
                self.input_maximum_ss.setVisible(True)
                self.label_maximum_ss.setVisible(True)
                self.label_seed_ss.setVisible(True)
                self.seed_input_ss.setVisible(True)

            if self.comboBox_sv.currentText() == "Binomial distribution":
                self.input_trials.setVisible(True)
                self.input_probability.setVisible(True)
                self.label_number_trials.setVisible(True)
                self.label_probability.setVisible(True)
                self.label_seed_ss.setVisible(True)
                self.seed_input_ss.setVisible(True)

            if self.comboBox_tv.isEnabled():
                if not (self.comboBox_tv.currentText() == "Choose distribution"):
                    self.tstop.setVisible(True)
                    self.tstopInput.setVisible(True)



        if self.radioButton_tv_distr.isChecked():
            if self.comboBox_tv.currentText() == "Gamma arrival process":
                self.seed.setVisible(True)
                self.seedInput.setVisible(True)
                self.mean_iat.setVisible(True)
                self.meanInput.setVisible(True)
                self.tstart.setVisible(True)
                self.tstartInput.setVisible(True)
                self.cvar.setVisible(True)
                self.cvarInput.setVisible(True)

                if self.radioButton_constant_ss.isChecked():
                    self.tstop.setVisible(True)
                    self.tstopInput.setVisible(True)

            if self.comboBox_tv.currentText() == "Poisson arrival process":
                self.seed.setVisible(True)
                self.seedInput.setVisible(True)
                self.mean_iat.setVisible(True)
                self.meanInput.setVisible(True)
                self.tstart.setVisible(True)
                self.tstartInput.setVisible(True)

                if self.radioButton_constant_ss.isChecked():
                    self.tstop.setVisible(True)
                    self.tstopInput.setVisible(True)

    def accepted(self):
        self.input_accepted()

    def append_time_series(self):
        self.input_accepted(True)


    def input_accepted(self, append=False):

        if append:
            self.time_vector_last = self.tsom.ts.t[:]
            self.value_vector_last = self.tsom.ts.v[:]
            if self.tsom.ts.t:
                t_last = self.tsom.ts.t[-1]
            else:
                t_last = 0

        else:
            t_last = 0
            time_vector_last = []
            value_vector_last = []

        if self.InputType.currentWidget() is self.equally:
            try:

                self.tsom.ts = self.tsom.ts.from_value_file(self.path.toPlainText(),
                                                            t_last + float(self.start_value.toPlainText()),
                                                            self.spacing_interval.toPlainText()
                                                            )
            except:
                self.file_error = QtWidgets.QDialog()
                self.ui = Ui_LoadErrorDialog(self.file_error)
                self.file_error.exec()

        elif self.InputType.currentWidget() is self.unequally:
            if self.radioButton_lff.isChecked() and self.radioButton_tv_lff.isChecked():
                try:
                    self.tsom.ts = self.tsom.ts.from_files(self.url_tv.toPlainText(),
                                                           self.url_sv.toPlainText(),
                                                           t_last
                                                           )
                except:
                    self.file_error = QtWidgets.QDialog()
                    self.ui = Ui_LoadErrorDialog(self.file_error)
                    self.file_error.exec()

            elif self.radioButton_lff.isChecked() and self.radioButton_tv_distr.isChecked():
                if self.comboBox_tv.currentText() == "Gamma arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    c_var = float(self.cvarInput.toPlainText())
                    distribution = GammaArrivalProcess(seed, mean, t_start, c_var)

                elif self.comboBox_tv.currentText() == "Poisson arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    distribution = PoissonArrivalProcess(seed, mean, t_start)

                else:
                    raise NotImplementedError
                try:
                    self.tsom.ts = self.tsom.ts.from_value_file_and_time_distribution(self.url_sv.toPlainText(),
                                                                                      distribution,
                                                                                      t_last)
                except:
                    self.file_error = QtWidgets.QDialog()
                    self.ui = Ui_LoadErrorDialog(self.file_error)
                    self.file_error.exec()


            elif self.radioButton_constant_ss.isChecked() and self.radioButton_tv_lff.isChecked():
                try:
                    self.tsom.ts = self.tsom.ts.from_time_file(self.url_tv.toPlainText(),
                                                               float(self.te_const_ss.toPlainText()),
                                                               t_last)
                except:
                    self.file_error = QtWidgets.QDialog()
                    self.ui = Ui_LoadErrorDialog(self.file_error)
                    self.file_error.exec()

            elif self.radioButton_constant_ss.isChecked() and self.radioButton_tv_distr.isChecked():
                if self.comboBox_tv.currentText() == "Gamma arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    c_var = float(self.cvarInput.toPlainText())
                    distribution = GammaArrivalProcess(seed, mean, t_start, c_var)
                elif self.comboBox_tv.currentText() == "Poisson arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    distribution = PoissonArrivalProcess(seed, mean, t_start)
                else:
                    raise NotImplementedError
                self.tsom.ts = self.tsom.ts.from_time_distribution(distribution,
                                                                   float(self.te_const_ss.toPlainText()),
                                                                   float(self.tstopInput.toPlainText()),
                                                                   t_last)

                if len(self.tsom.ts.t) > self._max_number_of_values:
                    self.tsom.ts.t = self.tsom.ts.t[:self._max_number_of_values]
                    self.tsom.ts.v = self.tsom.ts.v[:self._max_number_of_values]
                    self.max_len_error = QtWidgets.QDialog()
                    self.ui = Ui_MaximumTimeError(self.max_len_error)
                    self.max_len_error.exec()



            elif self.radioButton_distr_ss.isChecked() and self.radioButton_tv_lff.isChecked():
                try:

                    if self.comboBox_sv.currentText() == "Exponential distribution":
                        seed = float(self.seed_input_ss.toPlainText())
                        mean = float(self.input_mean_ss.toPlainText())
                        distribution = ExponentialSampleSizeProcess(seed, mean)

                    elif self.comboBox_sv.currentText() == "Uniform distribution":
                        seed = float(self.seed_input_ss.toPlainText())
                        low = float(self.input_minimum_ss.toPlainText())
                        high = float(self.input_maximum_ss.toPlainText())
                        distribution = UniformSampleSizeProcess(seed, low, high)

                    elif self.comboBox_sv.currentText() == "Binomial distribution":
                        seed = float(self.seed_input_ss.toPlainText())
                        n = int(self.input_trials.toPlainText())
                        p = float(self.input_probability.toPlainText())
                        distribution = BinomialSampleSizeProcess(seed, n, p)

                    else:
                        raise NotImplementedError
                    self.tsom.ts = self.tsom.ts.from_time_file_and_sample_size_distribution(self.url_tv.toPlainText(),
                                                                                            distribution,
                                                                                            t_last)

                except:
                    self.file_error = QtWidgets.QDialog()
                    self.ui = Ui_LoadErrorDialog(self.file_error)
                    self.file_error.exec()


            elif self.radioButton_distr_ss.isChecked() and self.radioButton_tv_distr.isChecked():

                if self.comboBox_tv.currentText() == "Gamma arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    c_var = float(self.cvarInput.toPlainText())
                    t_distribution = GammaArrivalProcess(seed, mean, t_start, c_var)

                elif self.comboBox_tv.currentText() == "Poisson arrival process":
                    seed = float(self.seedInput.toPlainText())
                    mean = float(self.meanInput.toPlainText())
                    t_start = float(self.tstartInput.toPlainText())
                    t_distribution = PoissonArrivalProcess(seed, mean, t_start)
                else:
                    raise NotImplementedError

                if self.comboBox_sv.currentText() == "Exponential distribution":
                    seed = float(self.seed_input_ss.toPlainText())
                    mean = float(self.input_mean_ss.toPlainText())
                    s_distribution = ExponentialSampleSizeProcess(seed, mean)

                elif self.comboBox_sv.currentText() == "Uniform distribution":
                    seed = float(self.seed_input_ss.toPlainText())
                    low = float(self.input_minimum_ss.toPlainText())
                    high = float(self.input_maximum_ss.toPlainText())
                    s_distribution = UniformSampleSizeProcess(seed, low, high)

                elif self.comboBox_sv.currentText() == "Binomial distribution":
                    seed = float(self.seed_input_ss.toPlainText())
                    n = int(self.input_trials.toPlainText())
                    p = float(self.input_probability.toPlainText())
                    s_distribution = BinomialSampleSizeProcess(seed, n, p)

                else:
                    raise NotImplementedError
                self.tsom.ts = self.tsom.ts.from_distributions(t_distribution,
                                                               s_distribution,
                                                               float(self.tstopInput.toPlainText()),
                                                               t_last)
        else:
            raise NotImplementedError

        if append:
            self.tsom.ts = self.tsom.ts.from_vectors(self.time_vector_last + self.tsom.ts.t, self.value_vector_last + self.tsom.ts.v)



    def activate_load_sample_size(self):
        enabled = False
        if self.radioButton_lff.isChecked() == True:
            enabled = True
        self.url_button_sv.setEnabled(enabled)
        self.url_sv.setEnabled(enabled)

    def activate_constant_sample_size(self):
        enabled = False
        if self.radioButton_constant_ss.isChecked() == True:
            enabled = True
        self.te_const_ss.setEnabled(enabled)
        self.set_parameters_visible()

    def activate_distributed_sample_size(self):
        enabled = False
        if self.radioButton_distr_ss.isChecked() is True:
            enabled = True
        self.comboBox_sv.setEnabled(enabled)

    def activate_load_time(self):
        enabled = False
        if self.radioButton_tv_lff.isChecked() == True:
            enabled = True
        self.pushButton_url_tv.setEnabled(enabled)
        self.url_tv.setEnabled(enabled)

    def activate_distributed_time(self):
        enabled = False
        if self.radioButton_tv_distr.isChecked() == True:
            enabled = True
        self.comboBox_tv.setEnabled(enabled)

    def get_input_description(self):
        self.description = ""

        if self.InputType.currentIndex() is 0:
            self.description += "\nSample size distribution:"
            self.description += "\n                              Explicit"
            self.description += "\nTime distribution:"
            self.description += "\n                              Explicit"

        else:
            if self.radioButton_distr_ss.isChecked():
                self.description += "\nSample size distribution:"
                self.description += "\n               " + self.comboBox_sv.currentText() + "\n"
            elif self.radioButton_constant_ss.isChecked():
                self.description += "\nSample size distribution:"
                self.description += "\n                              Constant"
            else:
                self.description += "\nSample size distribution:"
                self.description += "\n                              Explicit"
            if self.radioButton_tv_distr.isChecked():
                self.description += "\nTime distribution:"
                self.description += "\n               " + self.comboBox_tv.currentText() + "\n"
            else:
                self.description += "\nTime distribution:"
                self.description += "\n                              Explicit"

        self.description += "\nNumber of values:"
        self.description += "\n                              " + str(len(self.tsom.ts.v))
        self.description += "\nMean:"
        self.description += "\n                              " + str(round(np.mean(self.tsom.ts.v), 4))
        self.description += "\nMinimum:"
        self.description += "\n                              " + str(round(min(self.tsom.ts.v), 4))
        self.description += "\nMaximum:"
        self.description += "\n                              " + str(round(max(self.tsom.ts.v), 4))
        return self.description


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.InputType.setProperty("class", _translate("Dialog", "InputType"))
        self.Lable_sv.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sample vector</span></p></body></html>"))
        self.path.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C:/</p></body></html>"))
        self.url_button.setText(_translate("Dialog", "URL"))
        self.label_lff.setText(_translate("Dialog", "<html><head/><body><p>Load from File:</p></body></html>"))
        self.label_tv.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Time vector</span></p></body></html>"))
        self.label_stv.setText(_translate("Dialog", "<html><head/><body><p>Start value:</p><p><br/></p></body></html>"))
        self.label_si.setText(_translate("Dialog", "<html><head/><body><p>Spacing interval:</p><p><br/></p><p><br/></p></body></html>"))
        self.start_value.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.spacing_interval.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.InputType.setTabText(self.InputType.indexOf(self.equally), _translate("Dialog", "    Equally-spaced Time Series            "))
        self.radioButton_constant_ss.setText(_translate("Dialog", " Constant sample sizes:"))
        self.te_const_ss.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_sv_u.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Sample vector</span></p></body></html>"))
        self.radioButton_distr_ss.setText(_translate("Dialog", " Distributed sample sizes:"))
        self.url_button_sv.setText(_translate("Dialog", "URL"))
        self.radioButton_lff.setText(_translate("Dialog", " Load sample sizes from file:"))
        self.url_sv.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C:/</p></body></html>"))
        self.comboBox_sv.setItemText(0, _translate("Dialog", "Choose distribution"))
        self.comboBox_sv.setItemText(1, _translate("Dialog", "Binomial distribution"))
        self.comboBox_sv.setItemText(2, _translate("Dialog", "Exponential distribution"))
        self.comboBox_sv.setItemText(3, _translate("Dialog", "Uniform distribution"))
        self.label_seed_ss.setText(_translate("Dialog", "<html><head/><body><p>Seed:</p></body></html>"))
        self.seed_input_ss.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.label_mean_ss.setText(_translate("Dialog", "<html><head/><body><p>Mean sample size:</p></body></html>"))
        self.input_minimum_ss.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>"))
        self.label_maximum_ss.setText(_translate("Dialog", "<html><head/><body><p>Maximum value:</p></body></html>"))
        self.input_maximum_ss.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.label_minimum_ss.setText(_translate("Dialog", "<html><head/><body><p>Minimum value:</p></body></html>"))
        self.input_mean_ss.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.label_number_trials.setText(_translate("Dialog", "Number of trials:"))
        self.label_probability.setText(_translate("Dialog", "Probability of success:"))
        self.input_trials.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.input_probability.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0.5</span></p></body></html>"))
        self.radioButton_tv_lff.setText(_translate("Dialog", " Load time units from file:"))
        self.radioButton_tv_distr.setText(_translate("Dialog", " Distributed time units:"))
        self.label_tv_ue.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Time vector</span></p></body></html>"))
        self.url_tv.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C:/</p></body></html>"))
        self.pushButton_url_tv.setText(_translate("Dialog", "URL"))
        self.comboBox_tv.setItemText(0, _translate("Dialog", "Choose distribution"))
        self.comboBox_tv.setItemText(1, _translate("Dialog", "Gamma arrival process"))
        self.comboBox_tv.setItemText(2, _translate("Dialog", "Poisson arrival process"))
        self.seed.setText(_translate("Dialog", "<html><head/><body><p>Seed:</p></body></html>"))
        self.mean_iat.setText(_translate("Dialog", "<html><head/><body><p><a name=\"result_box\"/>Mean inter arrival time:</p></body></html>"))
        self.tstart.setText(_translate("Dialog", "<html><head/><body><p>Start time:</p></body></html>"))
        self.cvar.setText(_translate("Dialog", "<html><head/><body><p>Cvar:</p></body></html>"))
        self.seedInput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.meanInput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.tstartInput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0</span></p></body></html>"))
        self.cvarInput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1</span></p></body></html>"))
        self.tstop.setText(_translate("Dialog", "<html><head/><body><p>Stop time:</p></body></html>"))
        self.tstopInput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1000</span></p></body></html>"))
        self.InputType.setTabText(self.InputType.indexOf(self.unequally), _translate("Dialog", "            Unequally-spaced Time Series            "))

