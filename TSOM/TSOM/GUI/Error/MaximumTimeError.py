from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MaximumTimeError(object):

    def __init__(self, MaximumTimeError):
        self.setupUi(MaximumTimeError)

    def setupUi(self, MaximumTimeError):
        MaximumTimeError.setObjectName("MaximumTimeError")
        MaximumTimeError.resize(460, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(MaximumTimeError)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(MaximumTimeError)
        self.label.setGeometry(QtCore.QRect(10, 20, 441, 201))
        self.label.setObjectName("label")

        self.retranslateUi(MaximumTimeError)
        self.buttonBox.accepted.connect(MaximumTimeError.accept)
        self.buttonBox.rejected.connect(MaximumTimeError.reject)
        QtCore.QMetaObject.connectSlotsByName(MaximumTimeError)

    def retranslateUi(self, MaximumTimeError):
        _translate = QtCore.QCoreApplication.translate
        MaximumTimeError.setWindowTitle(_translate("MaximumTimeError", "Memory Error"))
        self.label.setText(_translate("MaximumTimeError", "<html><head/><body><p align=\"center\"><a name=\"result_box\"/><span style=\" font-size:16pt; font-weight:600; color:#c71518;\">E</span><span style=\" font-size:16pt; font-weight:600; color:#c71518;\">xcess of the maximum </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#c71518;\">time vector length.</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Automatic adaptation in 500.000</span></p><p align=\"center\"><span style=\" font-size:14pt;\">time units was carried out.</span></p></body></html>"))

