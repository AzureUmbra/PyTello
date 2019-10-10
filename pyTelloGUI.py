from main import Ui_Form
from connect import Ui_Connect
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import sys
import re
from multiprocessing import Process, Event

from telloUDP import TelloUDP
from time import sleep


class test():

    def __init__(self):
        self.mainWindow = QtWidgets.QWidget()
        self.connectWindow = QtWidgets.QWidget()
        self.main = Ui_Form()
        self.connect = Ui_Connect()
        self.main.setupUi(self.mainWindow)
        self.connect.setupUi(self.connectWindow)
        self.connectWindow.show()

        self.connect.connect.clicked.connect(self.start)

        # self.main.commandMode.clicked.connect(self.commandMode)
        # self.main.takeoff.clicked.connect(self.takeoff)
        # self.main.land.clicked.connect(self.land)
        # self.main.emergency.clicked.connect(self.emergency)

        self.mainWindow.closeEvent = self.close

        self.ipRE = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        self.tello = TelloUDP()
        self.ip = "0.0.0.0"
        self.exitFlag = Event()
        self.commandProcess = Process(target=self.commandReader, args=(self.exitFlag, self.main.commandText,self.tello,))



    def start(self):
        if self.ipRE.match(self.connect.ip.text()):
            #self.tello.start()
            self.ip = self.connect.ip.text()
            self.connectWindow.close()
            self.mainWindow.show()
        else:
            msg = "That is not a valid IP address, please try again!"
            QtWidgets.QMessageBox.warning(self.connectWindow,'Bad IP',msg)

    def close(self, event):
        msg = "Are you sure you want to exit?"
        reply = QtWidgets.QMessageBox.question(self.mainWindow,"Exit?",msg)
        if reply == QtWidgets.QMessageBox.Yes:
            self.exitFlag.set()
            self.commandProcess.join()
            #self.tello.stop()
            del self.tello
            event.accept()
        else:
            event.ignore()

    def commandReader(self, exitFlag, textBox, tello):
        while not exitFlag.is_set():
            data = tello.getCommand()
            for i in data:
                string = '{}: {}-{}'.format(i[2],i[1],i[0])
                textBox.append(string)



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gui = test()
    sys.exit(app.exec_())
