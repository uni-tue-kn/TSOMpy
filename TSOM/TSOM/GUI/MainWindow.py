from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.ProjectTab import Ui_ProjectTab
from Simulator.TSOM import TSOM

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.tsom_projects = []
        self.tabs = []
        self.frames = []
        self.tab_layouts = []
        self.tab_ui = []
        self.maximum_project_index = 0
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1272, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setIconSize(QtCore.QSize(100, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.projects = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.projects.setFont(font)
        self.projects.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.projects.setObjectName("projects")
        self.project1 = QtWidgets.QWidget()
        self.project1.setObjectName("project1")
        self.projects.addTab(self.project1, "")
        self.new_tab = QtWidgets.QWidget()
        self.new_tab.setObjectName("new_tab")
        self.projects.addTab(self.new_tab, "")
        self.verticalLayout.addWidget(self.projects)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.projects.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.initialize()


    def initialize(self):
        self.tabs.append(self.project1)
        self.initialize_new_tab()
        self.projects.currentChanged.connect(self.change_project)
        self.projects.setCurrentIndex(0)
        self.projects.setTabIcon(self.maximum_project_index, QtGui.QIcon("Icons/new_project.png"))


    def change_project(self):
        if self.projects.currentIndex() == self.maximum_project_index:
            self.add_new_tab()


    def add_new_tab(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("Project " + str(self.maximum_project_index + 1))
        self.tabs.append(tab)
        self.projects.insertTab(self.maximum_project_index, tab, tab.objectName())
        self.initialize_new_tab()
        self.projects.setCurrentIndex(self.maximum_project_index-1)

    def initialize_new_tab(self):
        self.tsom_projects.append(TSOM())
        self.tab_layouts.append(QtWidgets.QVBoxLayout())
        self.frames.append(QtWidgets.QFrame())
        self.tab_ui.append(Ui_ProjectTab(self.frames[self.maximum_project_index],
                                         self.tsom_projects[self.maximum_project_index]))
        self.tab_layouts[self.maximum_project_index].addWidget(self.frames[self.maximum_project_index])
        self.tabs[self.maximum_project_index].setLayout(self.tab_layouts[self.maximum_project_index])
        self.maximum_project_index += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TSOM"))
        self.projects.setTabText(self.projects.indexOf(self.project1), _translate("MainWindow", "Project 1"))
        self.projects.setTabText(self.projects.indexOf(self.new_tab), _translate("MainWindow", "New Project"))

