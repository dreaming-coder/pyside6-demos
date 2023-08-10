from PySide6.QtCore import QMimeData, QObject, QEvent
from PySide6.QtGui import QMouseEvent, Qt, QDrag, QDragEnterEvent, QDragMoveEvent
from PySide6.QtWidgets import QPushButton, QFrame, QWidget, QHBoxLayout, QApplication


class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("MyPushButton")

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.MouseButton.LeftButton:
            self.drag = QDrag(self)
            self.drag.setHotSpot(e.pos())
            mime = QMimeData()
            self.drag.setMimeData(mime)
            self.drag.exec()


class MyFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Shape.Box)
        self.btn = MyPushButton(self)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        self.child = self.childAt(event.pos())  # 获取指定位置的控件
        if self.child:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if self.child:
            self.child.move(event.pos() - self.child.drag.hotSpot())


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.resize(600, 400)
        self.setAcceptDrops(True)

    def setupUi(self):
        self.frame_1 = MyFrame(self)
        self.frame_2 = MyFrame(self)
        H = QHBoxLayout(self)
        H.addWidget(self.frame_1)
        H.addWidget(self.frame_2)

        self.frame_1.btn.installEventFilter(self)
        self.frame_2.btn.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if watched == self.frame_1.btn and event.type() == QEvent.Type.Move:
            self.frame_2.btn.move(event.pos())
            return True
        if watched == self.frame_2.btn and event.type() == QEvent.Type.Move:
            self.frame_1.btn.move(event.pos())
            return True
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication()
    win = MyWindow()
    win.show()
    app.exec()
