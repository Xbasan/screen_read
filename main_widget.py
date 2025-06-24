# This Python file uses the following encoding: utf-8
from os import remove, path
import sys

from easyocr import Reader
from PIL import ImageGrab
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)
from PySide6.QtGui import (
    QKeyEvent,
    QFont,
    QMouseEvent,
    QIcon,
)
#     pyside6-uic form.ui -o ui_form.py
from ui.ui_form import Ui_Widget
from ui.ui_set_buttons import Ui_widgetButtonTop
from translate import translate

HOME_PATH = "/home/khamzat/py_project/screen_read"


def screan(x, y, w, h) -> str:
    image_path = path.join(HOME_PATH, "test.png")
    im = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    im.save(image_path)
    reader = Reader(['en', 'ru'])
    try:
        text = reader.readtext(image_path)
    except SystemError:
        pass
    res = list()
    for i in text:
        res.append(i[1])
    remove(image_path)
    return res


class ButtonTop(QWidget, Ui_widgetButtonTop):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.exitButton.setIcon(QIcon(f"{HOME_PATH}/icon/exit.svg"))
        self.translateButton.setIcon(QIcon(f"{HOME_PATH}/icon/translate.svg"))
        self.copuButton.setIcon(QIcon(f"{HOME_PATH}/icon/copi.svg"))
        self.exitButton.clicked.connect(self.exit_butto_press)

    def exit_butto_press(self, event):
        QApplication.quit()


class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setupUi(self)
        self.showFullScreen()
        self.start_x = 0
        self.start_y = 0
        self.final_x = 0
        self.fianl_y = 0

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            QApplication.quit()

    def translat_button_press(self, event):
        self.text = translate(self.text)
        self.labal.setText("".join(self.text))
        self.labal.adjustSize()

    def copy_button_press(self, event):
        clipboard = QApplication.clipboard()
        clipboard.setText(" ".join(self.text))

    def mouseMoveEvent(self, event):
        if self.dragging:
            cur = event.position().toPoint()
            x = min(cur.x(), self.start_x)
            y = min(cur.y(), self.start_y)
            w = abs(cur.x() - self.start_x)
            h = abs(cur.y() - self.start_y)
            self.trase_widget.setGeometry(x, y, w, h)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            try:
                self.bl.setParent(None)
                self.bl.deleteLater()
                self.but.setParent(None)
                self.but.deleteLater()
                self.labal.setParent(None)
            except AttributeError:
                pass
            finally:
                self.trase_widget.setGeometry(self.start_x, self.start_y, 0, 0)
                self.trase_widget.setStyleSheet("""
                                                border: 2px dashed #3daee9;
                                                border-radius: 6%;
                                                """)
                self.dragging = True
                self.start_labal.hide()
                pos = event.globalPosition().toPoint()
                self.start_x = pos.x()
                self.start_y = pos.y()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            pos = event.globalPosition().toPoint()
            self.final_x = pos.x()
            self.final_y = pos.y()
            width = abs(self.start_x - self.final_x)
            height = abs(self.start_y - self.final_y)
            self.start_x = min(self.final_x, self.start_x)
            self.start_y = min(self.final_y, self.start_y)

            self.text = screan(self.start_x, self.start_y, width, height)

            font = QFont("URW Gothic [UKWN]", 12)

            self.labal = QLabel(self)
            self.labal.setText(" ".join(self.text))
            self.labal.setGeometry(self.start_x, self.start_y, width, height)
            self.labal.setMinimumSize(width, height)
            self.labal.setStyleSheet("""
                                     color:#000000;
                                     background: rgba(255,255,255,80%);
                                     border-radius: 6%;
                                     padding:1%;
                                     """)
            self.labal.setFont(font)
            self.labal.setWordWrap(True)
            self.labal.show()
            self.labal.raise_()

            self.bl = ButtonTop(self)
            self.bl.translateButton.clicked.connect(self.translat_button_press)
            self.bl.copuButton.clicked.connect(self.copy_button_press)
            self.but = self.bl.widget
            self.but.setParent(self)
            self.but.setStyleSheet("""
                           background-color: rgb(30, 33, 36);
                           border-radius:5%;""")

            self.but.move(self.start_x+(width/2)-131, self.start_y-54)
            self.but.show()
            self.but.raise_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
