from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSplitter, QWidget, QLabel, QApplication, QHBoxLayout


class W(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel("测试1")
        label1.setStyleSheet(".QLabel{background-color: pink}")
        label2 = QLabel("测试2")
        label2.setStyleSheet(".QLabel{background-color: yellow}")
        label3 = QLabel("测试3")
        label3.setStyleSheet(".QLabel{background-color: grey}")

        self.splitter_h = QSplitter(Qt.Orientation.Horizontal)
        self.splitter_h.setStyleSheet(".QSplitter{border: 1px solid red}")
        self.splitter_v = QSplitter(Qt.Orientation.Vertical)
        self.splitter_v.setStyleSheet(".QSplitter{border: 1px solid green}")

        h = QHBoxLayout(self)
        h.addWidget(self.splitter_h)
        self.splitter_h.addWidget(label1)
        self.splitter_h.addWidget(self.splitter_v)
        self.splitter_v.addWidget(label2)
        self.splitter_v.addWidget(label3)


if __name__ == '__main__':
    app = QApplication()
    win = W()
    win.show()
    app.exec()
