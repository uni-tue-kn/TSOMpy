from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DifferendFileLengthError(object):

    def __init__(self, DifferendFileLengthError):
        self.setupUi(DifferendFileLengthError)

    def setupUi(self, DifferendFileLengthError):
        DifferendFileLengthError.setObjectName("DifferendFileLengthError")
        DifferendFileLengthError.resize(427, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(DifferendFileLengthError)
        self.buttonBox.setGeometry(QtCore.QRect(50, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DifferendFileLengthError)
        self.label.setGeometry(QtCore.QRect(10, 30, 411, 191))
        self.label.setObjectName("label")

        self.retranslateUi(DifferendFileLengthError)
        self.buttonBox.accepted.connect(DifferendFileLengthError.accept)
        self.buttonBox.rejected.connect(DifferendFileLengthError.reject)
        QtCore.QMetaObject.connectSlotsByName(DifferendFileLengthError)

    def retranslateUi(self, DifferendFileLengthError):
        _translate = QtCore.QCoreApplication.translate
        DifferendFileLengthError.setWindowTitle(_translate("DifferendFileLengthError", "Differend File Length Warning"))
        self.label.setText(_translate("DifferendFileLengthError", "<html><head/><body><p align=\"center\"><a name=\"result_box\"/><span style=\" font-size:16pt; font-weight:600; color:#c10003;\">D</span><span style=\" font-size:16pt; font-weight:600; color:#c10003;\">ifferent number of values </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#c10003;\">in files were detected:</span></p><p align=\"center\"><a name=\"result_box\"/><span style=\" font-size:14pt;\">A</span><span style=\" font-size:14pt;\">n automatic adjustment to the </span></p><p align=\"center\"><span style=\" font-size:14pt;\">minimum length has been made.</span></p></body></html>"))

