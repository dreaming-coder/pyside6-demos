from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QApplication


class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.button.clicked.connect(self.bell_alert)

    def setupUi(self):
        self.setWindowTitle("Hello")
        self.resize(300, 150)

        self.label = QLabel(self)
        self.label.setText("地球不爆炸，我们不放假")
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(self)
        self.button.setText("响铃与预警")
        self.button.setGeometry(90, 100, 100, 20)

    def bell_alert(self):
        QApplication.beep()
        QApplication.alert(win, duration=0)


if __name__ == '__main__':
    app = QApplication()
    app.setApplicationDisplayName("欢迎程序")
    app.setEffectEnabled(Qt.UIEffect.UI_AnimateCombo)
    app.setWindowIcon(QPixmap("milk.png"))

    win = QWidget()
    win.show()
    mywin = myWidget()
    mywin.show()

    app.exec()
