#!/usr/bin/python
#coding: cp1250

import os
import sys
from os import system
from PyQt4 import QtGui as qtg
from PyQt4 import QtCore as qtc



class label_datetime(qtg.QLabel):
    def __init__(self, parent=None):
        super(label_datetime,self).__init__(parent)
        qf = qtg.QFont("Arial", 20)
        self.setFont(qf)
        self.setAlignment(qtc.Qt.AlignCenter)
        self.adjustSize()
        self.setStyleSheet('color: black;')
        timer = qtc.QTimer(self)
        timer.timeout.connect(self.displaytime)
        timer.start(1000)
        self.show()

    def displaytime(self):
        tijd = qtc.QDateTime.currentDateTime().toString()
        self.setText(qtc.QDateTime.currentDateTime().toString())
        self.setAlignment(qtc.Qt.AlignCenter)
        self.adjustSize()

class Login(qtg.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.textName = qtg.QLineEdit(self)
        self.textPass = qtg.QLineEdit(self)
        self.buttonLogin = qtg.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = qtg.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):

        conf = open("content/.config", "rw")
        text = conf.readlines()
        conf.close()

        config = []
        for data in text:
            config.append(data.splitlines())
        ID = config[0][0]
        PASS = config[1][0]

        if (self.textName.text() == ID and
            self.textPass.text() == PASS):
            self.accept()
        else:
            qtg.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

class settingWindow(qtg.QDialog):

    def __init__(self, parent=None):
        super(settingWindow,self).__init__(parent)

        self.buttonBox = qtg.QDialogButtonBox(self)

        self.setGeometry(600,100,300,100)
        self.setWindowTitle("Settings Panel")




class mainWindow(qtg.QMainWindow):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__()

        self.initUI()

    def initUI(self):


        # Creating menuebar
        menubar = self.menuBar()


        #### Setting toolbar menu

        stream_toolbar = self.addToolBar('Stream Link')
        stream = qtg.QAction(qtg.QIcon('content/icon.png'), 'Stream Link', self)
        stream.setStatusTip('Stream Link')
        stream.triggered.connect(self.on_pushStream)

        save_toolbar = self.addToolBar('Save')
        save = qtg.QAction(qtg.QIcon('content/save.png'), 'Save', self)
        save.setStatusTip('Save')
        save.triggered.connect(self.on_pushSave)

        settings_toolbar=self.addToolBar('Settings')
        settings=qtg.QAction('Settings',self)
        settings.triggered.connect(self.on_pushSettings)


        #### Adding actions to toolbar
        stream_toolbar.addAction(stream)
        save_toolbar.addAction(save)
        settings_toolbar.addAction(settings)


        #$$$$ Setting notepad menu

        newAction = qtg.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create new file')
        newAction.triggered.connect(self.newFile)

        saveAction = qtg.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)

        openAction = qtg.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)

        closeAction = qtg.QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Notepad')
        closeAction.triggered.connect(self.on_closeButton)

        clearAction = qtg.QAction('Clear', self)
        clearAction.setShortcut('Ctrl+P')
        clearAction.setStatusTip('Clear Notepad')
        clearAction.triggered.connect(self.on_clearButton)


        #Adding menues
        fileMenu = menubar.addMenu('&App')
        fileMenu.addAction("License")

        noteMenu = menubar.addMenu('&Notepad')
        noteMenu.addAction(newAction)
        noteMenu.addAction(saveAction)
        noteMenu.addAction(openAction)
        noteMenu.addAction(closeAction)
        noteMenu.addAction(clearAction)


        #Add time clock
        self.time=label_datetime(self)

        #Set statusbar with clock
        self.statusBar().addWidget(self.time)


        #Set text editor in mainWindow
        self.text = qtg.QTextEdit()

        hbox = qtg.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.text)

        vbox = qtg.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setCentralWidget(self.text)
        self.text.show()


        self.setGeometry(300, 200, 600, 200)
        self.setWindowIcon(qtg.QIcon('content/icon.png'))
        self.setWindowTitle('HiveVision')
        self.show()


    def on_closeButton(self):
        close=qtg.QWidget(self)
        self.setCentralWidget(close)
        close.show()

    def on_clearButton(self):
        self.text.clear()

    def on_pushSettings(self):
        login=Login(self)
        if login.exec_() == qtg.QDialog.Accepted:
            dialog = settingWindow(self)
            dialog.show()

    def on_pushSave(self):
        filename = qtg.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def on_pushStream(self):
        stream = system('nohup vlc rtsp://192.168.43.96:8554/ &')
        #Sprawdzić status wykonania#
        #Statusbarem

    def timer(self):
        self.time.show()

    def newFile(self):
        self.text=qtg.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.text.show()

    def saveFile(self):
        filename = qtg.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def openFile(self):
        filename = qtg.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()



def main():
    app=qtg.QApplication(sys.argv)
    ex=mainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
