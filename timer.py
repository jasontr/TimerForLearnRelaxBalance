from TimerUIElement import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys


class Timer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Timer, self).__init__()
        self.setupUi(self)
        self.additionalUISettings()

    def additionalUISettings(self):
        self.learnTime
        self.
        self.relaxPushButton.clicked.connect(self.relaxPushButtonClickedEvent)
        self.learnPushButton.clicked.connect(self.learnPushButtonClickedEvent)
        self.learnLcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.learnTimer = QtCore.QTimer(self.learnLcd)
        self.learnTimer.timeout.connect(self.learnTimerShowTime)
        self.learnTimer.started = False
        self.learnTimer.start(53)

        self.learnTimerShowTime()

        self.setWindowTitle("Digital Clock")

    def relaxPushButtonClickedEvent(self):
        print("greetings")

    def learnPushButtonClickedEvent(self):
        print("hello")
        if not self.learnTimer.started:
            self.learnTimer.start(500)

    def learnTimerShowTime(self):
        time = QtCore.QTime.currentTime()

        text = time.toString('hh:mm:ss:zzz')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:8] + ' ' + text[9:]

        self.learnLcd.display(text)


if __name__ == "__main__":
    # Create a QApplication
    app = QtWidgets.QApplication([])
    widget = Timer()
    widget.show()

    # Connect the button "clicked" signal to the exit() method
    # that finishes the QApplication

    sys.exit(app.exec_())
    pass
