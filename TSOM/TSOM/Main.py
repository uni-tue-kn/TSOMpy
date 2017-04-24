

try:
    from PyQt5 import QtWidgets
except ModuleNotFoundError as err:
    print("Module PyQT5 not found! Please install to proceed!")

try:
    import numpy
except ModuleNotFoundError as err:
    print("Module numpy not found! Please install to proceed!")

try:
    import matplotlib
except ModuleNotFoundError as err:
    print("Module matplotlib not found! Please install to proceed!")


try:
    from GUI.MainWindow import Ui_MainWindow
    import sys


    def main():
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(main_window)
        main_window.show()

        sys.exit(app.exec_())


    if __name__ == "__main__":
        main()

except ModuleNotFoundError as err:
    print("Module not found. Please check TSOMpy requirements!")


