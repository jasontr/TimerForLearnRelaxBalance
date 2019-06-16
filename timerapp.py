from TimerUIElement import Ui_MainWindow
from PyQt5.QtCore import QTime, QTimer, QDateTime
from PyQt5.QtWidgets import QLCDNumber, QMainWindow, QApplication, QMessageBox
import sys
from enum import Enum
import pickle


class TimerType(Enum):
    RELAX = "R"
    LEARN = "L"


class ObjectData:
    def __init__(self, main_lcd_leading: TimerType, lcd_current_time: int):
        self.main_lcd_leading = main_lcd_leading
        self.main_lcd_current_time = lcd_current_time


class MainLcd:
    QDATETIME_FORMATTER = QDateTime(1, 1, 1, 0, 0)

    def __init__(self, main_qlcd: QLCDNumber, registry=None):
        self.qlcd = main_qlcd
        self.leading: TimerType = TimerType.LEARN if not registry else registry.main_lcd_leading
        self.current_time = 0 if not registry else registry.main_lcd_current_time

    def show(self, duration, from_timer: TimerType):
        self.current_time += duration if from_timer == self.leading else -duration
        if self.current_time < 0:
            self.leading = from_timer
            self.current_time = abs(self.current_time)
        current_qdatetime = self.QDATETIME_FORMATTER.addMSecs(self.current_time)
        text = current_qdatetime.toString('hh:mm:ss.zzz')
        if (duration % 500) == 0:
            text = text[:8] + ' ' + text[9:]
        text = self.leading.value + " " + text
        self.qlcd.display(text)


class Timer:
    TIME_RESET = QDateTime(1, 1, 1, 0, 0)
    TIME_FORMAT = 'hh:mm:ss.zzz'

    def __init__(self, timer: QTimer, lcd: QLCDNumber, main_lcd: MainLcd, timer_type: TimerType):
        self.timer = timer
        self.timer_type = timer_type
        self.lcd = lcd
        self.main_lcd = main_lcd
        self.lcd.setSegmentStyle(QLCDNumber.Filled)
        # time variable
        self.start_time = QDateTime.currentDateTime()
        self.stop_time = QDateTime.currentDateTime()
        self.curr_time = self.TIME_RESET
        self.timer.timeout.connect(self.currTime)
        self.running = False
        self.last_duration = 0

    def currTime(self):
        duration_q_datetime, duration = self.calcDuration()
        if not self.running:
            duration_q_datetime = self.curr_time
            duration = self.last_duration
        text = duration_q_datetime.toString(self.TIME_FORMAT)
        if (duration % 500) == 0:
            text = text[:8] + ' ' + text[9:]
        self.lcd.display(text)
        self.main_lcd.show(duration - self.last_duration, self.timer_type)
        self.last_duration = duration

    def startTimer(self):
        self.start_time = QDateTime.currentDateTime()
        self.running = True
        self.last_duration = 0
        self.timer.start(53)

    def pauseTimer(self):
        self.running = not self.running
        if self.isRunning():
            # when restarted from pause, set start_time to the time restarted
            self.start_time = QDateTime.currentDateTime()
            self.last_duration = 0
        else:
            # set curr_time to the time when timer is paused
            self.curr_time = self.calcDuration()[0]

    def calcDuration(self) -> (QDateTime, int):
        self.stop_time = QDateTime.currentDateTime()
        duration = self.start_time.msecsTo(self.stop_time)
        return self.curr_time.addMSecs(duration), duration

    def getTimerType(self) -> TimerType:
        return self.timer_type

    def isRunning(self) -> bool:
        return self.running

    def stopTimer(self):
        self.running = False
        # TODO jasontr write log
        self.curr_time = self.TIME_RESET
        self.lcd.display(self.TIME_RESET.toString(self.TIME_FORMAT))
        self.timer.stop()
        self.last_duration = 0

    def showZero(self):
        self.lcd.display(self.TIME_RESET.toString(self.TIME_FORMAT))


class TimerApp(QMainWindow, Ui_MainWindow):
    OBJECT_DATA_FILE = 'object_data'

    def __init__(self):
        super(TimerApp, self).__init__()
        self.object_data = self.loadObjectData()
        self.setupUi(self)
        self.additionalUISettings()
        self.componentInitialize()
        self.current_timer = TimerType.LEARN

    def additionalUISettings(self):
        self.relaxPushButton.clicked.connect(self.relaxPushButtonClickedEvent)
        self.learnPushButton.clicked.connect(self.learnPushButtonClickedEvent)
        self.learnTimer = QTimer(self.learnLcd)
        self.relaxTimer = QTimer(self.relaxLcd)

    def componentInitialize(self):
        self.mainLcd = MainLcd(self.timerLcd, self.object_data)
        self.mainLcd.show(0, TimerType.LEARN)
        self.learnTimeComponent = Timer(self.learnTimer, self.learnLcd, self.mainLcd, TimerType.LEARN)
        self.relaxTimeComponent = Timer(self.relaxTimer, self.relaxLcd, self.mainLcd, TimerType.RELAX)
        self.learnTimeComponent.showZero()
        self.relaxTimeComponent.showZero()

    def relaxPushButtonClickedEvent(self):
        self.push(self.relaxTimeComponent, self.learnTimeComponent)

    def learnPushButtonClickedEvent(self):
        self.push(self.learnTimeComponent, self.relaxTimeComponent)

    def push(self, self_component: Timer, another_component: Timer):
        if self_component.getTimerType() != self.current_timer:
            self.current_timer = self_component.getTimerType()
            self_component.startTimer()
            another_component.stopTimer()
        else:
            self_component.pauseTimer()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.dumpObjectData()
        else:
            event.ignore()

    def dumpObjectData(self):
        self.object_data = ObjectData(self.mainLcd.leading, self.mainLcd.current_time)
        with open(self.OBJECT_DATA_FILE, 'wb') as f:
            pickle.dump(self.object_data, f)

    def loadObjectData(self) -> ObjectData:
        try:
            with open(self.OBJECT_DATA_FILE, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None


if __name__ == "__main__":
    # Create a QApplication
    app = QApplication([])
    widget = TimerApp()
    widget.show()

    # Connect the button "clicked" signal to the exit() method
    # that finishes the QApplication

    sys.exit(app.exec_())
    pass
