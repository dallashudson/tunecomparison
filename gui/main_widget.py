import sys
import os
#import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMenu, QStyleFactory
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from mod.tune import TUNE
from mod.comparison import Comparison


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = App(self)
        # self.multi_widget = multiTUNE(self)
        self.setCentralWidget(self.form_widget)
        self.build()

        font = self.font()
        font.setBold(True)
        self.setFont(font)
        self.experiment = True
        # print(QStyleFactory.keys)

    def changeStyle(self, style):
        qApp.setStyleSheet(style)

    def changeExp(self):
        if self.experiment is True:
            self.experiment = False
        else:
            self.experiment = True

    def build(self):
        s = QStyleFactory.create('Fusion')

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        '''windows = QAction(QIcon('exit.png'), 'Windows', self)
        windows.setStatusTip('Change To Default Windows Theme')
        windows.triggered.connect(lambda: qApp.setStyleSheet(s))

        vista = QAction(QIcon('exit.png'), 'Vista', self)
        vista.setStatusTip('Change To Vista Theme')
        vista.triggered.connect(lambda: qApp.setStyleSheet(dark_stylesheet))'''

        fusion = QAction(QIcon('exit.png'), 'Light', self)
        fusion.setStatusTip('Change To Light Theme')
        fusion.setShortcut('Ctrl+L')
        fusion.triggered.connect(lambda: self.changeStyle('thisdoesntwork'))

        dark = QAction(QIcon('exit.png'), 'Dark', self)
        dark.setStatusTip('Change To Dark Theme')
        dark.setShortcut('Ctrl+D')
        dark.triggered.connect(lambda: qApp.setStyleSheet(dark_stylesheet))

        experimental = QAction(QIcon('exit.png'), 'Experimental', self)
        experimental.setStatusTip('Enable Experimental Functions')
        experimental.triggered.connect(lambda: self.changeExp())

        multiAction = QAction(QIcon('exit.png'), 'Multiple-TUNE Layout', self)
        multiAction.setStatusTip('Compare Multiple TUNES at Once')
        multiAction.triggered.connect(lambda: self.toMulti())
        singleAction = QAction(QIcon('exit.png'), 'Single-TUNE Layout', self)
        singleAction.setStatusTip('Compare Multiple TUNES at Once')
        singleAction.triggered.connect(lambda: self.toSingle())

        # fusion = QAction(QIcon('exit.png'), '&Exit', self)
        # fusion.setStatusTip('Change Theme to Fusion')
        # fusion.triggered.connect(qApp.fusion)

        self.setGeometry(30, 30, 640, 300)
        self.setStyleSheet("background-image: url(bruh.png)")
        self.setWindowIcon(QIcon('icons/bom.jpg'))
        self.setWindowTitle('Tune Differences Comparison Tool')
        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')

        #themeMenu = QMenu('Change Theme', self)

        #modeMenu = QMenu('Change Mode', self)

        '''fileMenu.addMenu(modeMenu)
        fileMenu.addMenu(themeMenu)
        themeMenu.addAction(fusion)
        themeMenu.addAction(dark)
        modeMenu.addAction(multiAction)
        modeMenu.addAction(singleAction)
        fileMenu.addAction(exitAct)'''

    def toSingle(self):
        self.form_widget = App(self)
        self.multi_widget = multiTUNE(self)
        self.setCentralWidget(self.form_widget)
        try:
            self.multi_widget.close()
        except RuntimeError or AttributeError:
            pass

    def toMulti(self):
        self.multi_widget = multiTUNE(self)
        self.setCentralWidget(self.multi_widget)
        try:
            self.form_widget.close()
        except RuntimeError or AttributeError:
            pass


class App(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.title = 'Tune Differences Comparison Tool'
        self.left = 30
        self.top = 30
        self.width = 640
        self.height = 300
        self.oText = 'Select First Tune Differences'
        self.nText = 'Select Second Tune Differences'
        self.build()

    def build(self):
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('File')
        title = QLabel('Select Tunes:')
        tune1 = QLabel('Tune 1')
        tune2 = QLabel('Tune 2')

        """options = QLabel('Options:')
        self.fai = QCheckBox("FAI Report?")
        self.revC = QCheckBox("Include Revision Changes?")
        newfont = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
        options.setFont(newfont)
        title.setFont(newfont)
        self.quanC = QCheckBox("Include Quantity Changes?")
        self.delC = QCheckBox("Include Deleted Items?")
        self.addC = QCheckBox("Include Added Items?")"""

        self.destination = QLabel('Destination')

        '''self.revC.setChecked(True)
        self.quanC.setChecked(True)
        self.delC.setChecked(True)
        self.addC.setChecked(True)'''

        tune1Lbl = QLabel('Comment')
        tune2Lbl = QLabel('Comment')
        tune1Lbl.setToolTip('Optional Comment about this TUNE')
        tune2Lbl.setToolTip('Optional Comment about this TUNE')
        compLbl = QLabel('File Name')

        self.destinationEdit = QLineEdit()

        self.tune1Edit = QLineEdit()
        self.tune2Edit = QLineEdit()
        self.tune1Name = QLineEdit()
        self.tune2Name = QLineEdit()
        self.tune2Name.setToolTip('Optional Comment about this TUNE')
        self.tune1Name.setToolTip('Optional Comment about this TUNE')
        self.compareName = QLineEdit()

        helpB = QPushButton('Help')
        helpB.setToolTip('Access Help Tutorial')

        openOld = QPushButton('Browse')
        openOld.setToolTip('.txt files only')
        openNew = QPushButton('Browse')
        openNew.setToolTip('.txt files only')
        setDes = QPushButton('Browse')
        btn_compare = QPushButton('Generate Report')
        self.tune1Edit.setText(str(self.oText))
        self.tune2Edit.setText(str(self.nText))
        self.destinationEdit.setText('Select Destination Folder')
        openOld.clicked.connect(lambda: self.tune1Edit.setText(str(
            self.old_click())))
        setDes.clicked.connect(lambda: self.destinationEdit.setText(str(
            self.des_click())))
        openNew.clicked.connect(lambda: self.tune2Edit.setText(str(
            self.new_click())))
        btn_compare.clicked.connect(lambda: self.compare())
        helpB.clicked.connect(lambda: self.help_window())

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(tune1, 2, 0)
        grid.addWidget(tune1Lbl, 3, 0)
        grid.addWidget(self.tune1Edit, 2, 1)
        grid.addWidget(self.tune1Name, 3, 1)

        grid.addWidget(tune2, 4, 0)
        grid.addWidget(tune2Lbl, 5, 0)
        grid.addWidget(self.tune2Edit, 4, 1)
        grid.addWidget(self.tune2Name, 5, 1)

        grid.addWidget(openOld, 2, 2)
        grid.addWidget(openNew, 4, 2)

        grid.addWidget(self.destination, 6, 0)
        grid.addWidget(self.destinationEdit, 6, 1)
        grid.addWidget(setDes, 6, 2)
        grid.addWidget(compLbl, 7, 0)
        grid.addWidget(self.compareName, 7, 1)

        grid.addWidget(btn_compare, 8, 1)

        '''grid.addWidget(options, 1, 3)
        grid.addWidget(self.fai, 2, 3)
        grid.addWidget(self.revC, 3, 3)
        grid.addWidget(self.quanC, 4, 3)
        grid.addWidget(self.addC, 5, 3)
        grid.addWidget(self.delC, 6, 3)'''
        grid.addWidget(helpB, 8, 2)

        title = QLabel('TUNE Compare', self)
        title.hide()
        # r = title.setPalette()
        # r.setColor(self.backgroundRole(), QColor(0, 0, 0))

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)
        self.setLayout(grid)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icons/bom.jpg'))
        self.show()

    def new_click(self):
        filt = "Text (*.txt)"
        n = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', filt)
        n = str(n)[2:]
        n = n[:-18]
        return n
        # tune2Edit.setText(str(fname))

    def old_click(self):
        filt = "Text (*.txt)"
        o = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', filt)
        o = str(o)[2:]
        o = o[:-18]
        return o
        # tune1Edit.setText(str(rname))

    def des_click(self):
        j = QFileDialog.getExistingDirectory(self, 'Open Folder', 'c:\\')
        # j = str(j)[2:]
        # j = j[:-19]
        return j

    def close_application(self, error):
        if(error == "Tune_1"):
            QMessageBox.about(self, "Error", "You did not choose a first tune")
        if(error == "Tune_2"):
            QMessageBox.about(
                self, "Error", "You did not choose a second tune")
        if(error == "name"):
            QMessageBox.about(self, "Error", "You did not choose a file name")
        if(error == "dest"):
            QMessageBox.about(self, "Error",
                              "You did not choose a destination folder")

    def help_window(self):
        self.form_widget = help_win(self)

    def compare(self):
        try:
            sheetName = self.compareName.text()
            present = True
            tune2file = self.tune2Edit.text()
            tune1file = self.tune1Edit.text()
            dest = self.destinationEdit.text()
            try:
                open(tune2file)
            except FileNotFoundError:
                self.close_application("Tune_2")
                present = False

            try:
                open(tune1file)
            except FileNotFoundError:
                self.close_application("Tune_1")
                present = False

            if(not os.path.exists(dest)):
                self.close_application("dest")
                present = False

            if(sheetName is ""):
                self.close_application("name")
                present = False

            if(present):
                oldName = self.tune1Name.text()
                f = os.path.basename(self.tune1Edit.text())
                f = f[:-4]  # Split by comma, this just deletes the file type
                if(str(oldName) != ""):
                    Tune_1 = TUNE(oldName)
                else:
                    Tune_1 = TUNE(str(f))

                tune1addresses = Tune_1.read_tune(str(self.tune1Edit.text()))

                r = os.path.basename(self.tune2Edit.text())
                r = r[:-4]  # Split by comma, this just deletes the file type
                newName = self.tune2Name.text()
                if(str(newName) != ""):
                    Tune_2 = TUNE(newName)
                else:
                    Tune_2 = TUNE(str(f))

                tune2addresses = Tune_2.read_tune(str(self.tune2Edit.text()))

                tuneCompare = Comparison()

                tuneCompare.compare_tunes(
                    tune1addresses, tune2addresses, dest, self.compareName.text(), self.tune1Name.text(), self.tune2Name.text())

                print(dest)
                # if self.experiment is False:
                QMessageBox.about(self, "Status", "Comparison Complete!")
                # else:
                #    buttonReply = QMessageBox.question(self, 'Status',
                #                                      "Comparison Complete!\n"
                #                                      "Would you like to\n"
                #                                      "open the report?",
                #                                      QMessageBox.Yes |
                #                                      QMessageBox.No)
                #    if buttonReply == QMessageBox.Yes:
                #        os.system("start " + (dest + "/" +
                #                  self.compareName.text() + ".xlsx"))
                #    else:
                #        print('No clicked.')
        except PermissionError:
            QMessageBox.about(self, "Error",
                              "Your file already exists and is currently open")
        # Tune_1.print_bom()
        # Tune_2.print_bom()


class help_win(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.title = 'TUNE Comparison Help Window'
        self.left = 30
        self.top = 30
        self.width = 250
        self.height = 250
        self.build()

    def build(self):
        heinfo = QLabel("The Tune Difference Comparison Tool is used to\n"
                        "compare the differences between stock tunes\n"
                        "and aftermarket/tuner tunes for a hex dump\n"
                        "of either an ECU, TCU, or CPC computer. Once\n"
                        "you have copied these differences in WinOLS,\n"
                        "paste them into a .txt file, make sure that you\n"
                        "press CTRL+A to select the entire window including\n"
                        "the title of the columns in the WinOLS Differences\n"
                        "window. From here, select the differences files that\n"
                        "you have just made, add a comment to put in the final\n"
                        "report if necessary, select a location, and generate!")
        grid = QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(heinfo, 1, 3)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)
        self.setLayout(grid)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
