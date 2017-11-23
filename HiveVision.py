#!/usr/bin/pythn
# coding: utf-8


import sys
from PyQt4 import QtGui as qtg
from PyQt4 import QtCore as qtc


class foreWindow(qtg.QMainWindow):

    def __init__(self, parent=None):
        super(foreWindow,self).__init__(parent)

        #self.buttonBox = qtg.QDialogButtonBox(self)

        self.setGeometry(600,100,300,100)
        self.setWindowTitle("StreamUla")



class mainWindow(qtg.QMainWindow):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        #self.btn = qtg.QPushButton("Stream Link", self)
        #self.btn.move(20, 20)
        #self.btn.clicked.connect(self.on_pushButton)


        self.dialog=foreWindow(self)

        textEdit = qtg.QTextEdit()
        self.setCentralWidget(textEdit)

        stream = qtg.QAction(qtg.QIcon('icon.png'), 'Stream Link', self)
        stream.setStatusTip('Stream Link')
        stream.triggered.connect(self.on_pushButton)

        ex=qtg.QAction("Exit",self)
        ex.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(ex)


        toolbar = self.addToolBar('Stream Link')
        toolbar.addAction(stream)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowIcon(qtg.QIcon('icon.png'))
        self.setWindowTitle('HiveVision')
        self.show()

    @qtc.pyqtSlot()
    def on_pushButton(self):
        self.dialog.show()





def main():

    app=qtg.QApplication(sys.argv)
    ex=mainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()