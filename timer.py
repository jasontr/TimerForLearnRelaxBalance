from TimerUIElement import Ui_MainWindow
from PyQt5.QtCore import QTime, QTimer, QDateTime
from PyQt5.QtWidgets import QLCDNumber, QMainWindow, QApplication
import sys


class Timer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Timer, self).__init__()
        self.setupUi(self)
        self.additionalUISettings()

    def additionalUISettings(self):
        self.relaxPushButton.clicked.connect(self.relaxPushButtonClickedEvent)
        self.learnPushButton.clicked.connect(self.learnPushButtonClickedEvent)
        self.learnTimer = QTimer(self.learnLcd)
        self.relaxTimer = QTimer(self.relaxLcd)
        self.learnTimeComponent = Time(self.learnTimer, self.learnLcd)
        self.relaxTimeComponent = Time(self.relaxTimer, self.relaxLcd)

    def relaxPushButtonClickedEvent(self):
        print("greetings")
        self.relaxTimeComponent.push()

    def learnPushButtonClickedEvent(self):
        print("hello")
        self.learnTimeComponent.push()

    def learnTimerShowTime(self):
        pass

    def start(self):
        pass


class Time:
    def __init__(self, timer: QTimer, lcd: QLCDNumber):
        self.timer = timer
        self.lcd = lcd
        self.lcd.setSegmentStyle(QLCDNumber.Filled)
        # time variable
        self.start_time = QDateTime.currentDateTime()
        self.stop_time = QDateTime.currentDateTime()
        self.curr_time = QDateTime(1, 1, 1, 0, 0)
        self.timer.timeout.connect(self.currTime)
        self.started = False

    def currTime(self):

        durationQDatetime, duration = self.calcDuration()
        if not self.started:
            durationQDatetime = self.curr_time
        text = durationQDatetime.toString('hh:mm:ss.zzz')
        # text = self.curr_time.toString('hh:mm:ss.zzz')
        if (duration % 500) == 0:
            text = text[:8] + ' ' + text[9:]
        self.lcd.display(text)

    def startTimer(self):
        self.start_time = QDateTime.currentDateTime()
        self.started = True
        self.timer.start(53)

    def stopTimer(self):
        self.started = False
        self.curr_time = self.calcDuration()[0]

    def calcDuration(self) -> (QDateTime, int):
        self.stop_time = QDateTime.currentDateTime()
        duration = self.start_time.msecsTo(self.stop_time)
        return self.curr_time.addMSecs(duration), duration


    def push(self):
        if self.started:
            self.stopTimer()
        else:
            self.startTimer()


if __name__ == "__main__":
    # Create a QApplication
    app = QApplication([])
    widget = Timer()
    widget.show()

    # Connect the button "clicked" signal to the exit() method
    # that finishes the QApplication

    sys.exit(app.exec_())
    pass
