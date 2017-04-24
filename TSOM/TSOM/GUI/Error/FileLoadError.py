from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadErrorDialog(object):

    def __init__(self, LoadErrorDialog):
        self.setupUi(LoadErrorDialog)

    def setupUi(self, LoadErrorDialog):
        LoadErrorDialog.setObjectName("LoadErrorDialog")
        LoadErrorDialog.resize(369, 254)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoadErrorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 200, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(LoadErrorDialog)
        self.label.setGeometry(QtCore.QRect(-20, 10, 411, 191))
        self.label.setObjectName("label")

        self.retranslateUi(LoadErrorDialog)
        self.buttonBox.accepted.connect(LoadErrorDialog.accept)
        self.buttonBox.rejected.connect(LoadErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadErrorDialog)

    def retranslateUi(self, LoadErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadErrorDialog.setWindowTitle(_translate("LoadErrorDialog", "Load Error"))
        self.label.setText(_translate("LoadErrorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#dd1010;\">An error occured while</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#dd1010;\">loading data file.</span></p><p align=\"center\"><a name=\"result_box\"/><span style=\" font-size:14pt;\">P</span><span style=\" font-size:14pt;\">lease check the input</span></p><p align=\"center\"><span style=\" font-size:14pt;\">file and reload it.</span></p></body></html>"))

