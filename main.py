import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QLabel, QLineEdit, QTextEdit, QGridLayout,
                             QApplication, QPushButton, QFileDialog,
                             QStyleFactory)

from PyQt5.QtGui import QIcon
from gui.main_widget import App, MainWindow


app = QApplication(sys.argv)
main_w = MainWindow()
main_w.show()
sys.exit(app.exec_())
