# This Python file uses the following encoding: utf-8
import sys

from easyocr import Reader
from PIL import ImageGrab
import numpy

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
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
from ui.ui_gemini import Ui_widget_Gemini

from translate import g_translate
from gemini import gemini

HOME_PATH = "/home/khamzat/py_project/screen_read"
DEFOLT_MESSAG = "Сорянь но я там текста невижу"
DEFOLT_PROMPT = "Ответь только олддно сообшение что запрос не дошол"


def screan(x, y, w, h) -> list:
    im = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    im_np = numpy.array(im)

    reader = Reader(['en', 'ru'])
    try:
        text = reader.readtext(im_np)
    except SystemError:
        return DEFOLT_MESSAG

    res = [i[1] for i in text]
    return res if res else DEFOLT_MESSAG


class Ai_widget(QDialog, Ui_widget_Gemini):
    def __init__(self, promt: str):
        super().__init__()
        self.setupUi(self)

        res_ai_text, res_id = gemini(text=promt)
        self.textEdit.setMarkdown(res_ai_text)


class ButtonTop(QWidget, Ui_widgetButtonTop):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.exitButton.setIcon(QIcon(f"{HOME_PATH}/icon/exit.svg"))
        self.translateButton.setIcon(QIcon(f"{HOME_PATH}/icon/translate.svg"))
        self.copuButton.setIcon(QIcon(f"{HOME_PATH}/icon/copi.svg"))
        self.gemini.setIcon(QIcon(f"{HOME_PATH}/icon/gemini-color.svg"))
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
        if 1:
            self.labal.setText(str(g_translate(self.text)))
            self.labal.adjustSize()
        elif 0:
            self.labal.setText(self.text)
            self.labal.adjustSize()

    def copy_button_press(self, event):
        clipboard = QApplication.clipboard()
        print(self.labal.selectedText())
        text = self.labal.text()
        clipboard.setText(text)

    def gemini_button_press(self, event):
        promt = self.labal.text()
        print(promt)
        self.dialog_ai = Ai_widget(promt)
        self.dialog_ai.setWindowTitle(f"Gemini : {promt}")
        self.dialog_ai.exec()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
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

            font = QFont("Noto Sans", 12)

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
            self.labal.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.labal.adjustSize()

            self.bl = ButtonTop(self)
            self.bl.translateButton.clicked.connect(self.translat_button_press)
            self.bl.copuButton.clicked.connect(self.copy_button_press)
            self.bl.gemini.clicked.connect(self.gemini_button_press)
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
