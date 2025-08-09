# This Python file uses the following encoding: utf-8
import sys

from io import BytesIO
from PIL import ImageGrab
from numpy import array
import base64

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
    QPixmap,
    QImage
)
from torch import hann_window
#     pyside6-uic form.ui -o ui_form.py
from ui.ui_form import Ui_Widget
from ui.ui_set_buttons import Ui_widgetButtonTop
from ui.ui_gemini import Ui_widget_Gemini
from ui.ui_input_dialog import Ui_widget_input

from translate import g_translate
from gemini import Gemini

HOME_PATH = "/home/khamzat/py_project/screen_read"
USER_NAME = "Xamz_pok"
DEFOLT_MESSAG = "Сорянь но я там текста невижу"
DEFOLT_PROMPT = "Ответь только олддно сообшение что запрос не дошол"

GEMINI = Gemini()

res_ai_text = ""

WIDTH = 0
HEIGHT = 0


def screan(x, y, w, h):
    if w > 12 and h > 12:
        im = ImageGrab.grab(bbox=(x, y, x+w, y+h))
        
        bt = BytesIO()
        im.save(bt, format="PNG")
        b64 = base64.b64encode(bt.getvalue()).decode("utf-8")
        im_np = array(im)
        return im_np, b64
    else:
        return "Выди хот чтото", 0


def read_text(im_np):
    from easyocr import Reader
    reader = Reader(['en', 'ru'], detector="dbnet18")
    try:
        text = reader.readtext(im_np, batch_size=5)
    except SystemError:
        return DEFOLT_MESSAG
    res = [i[1] for i in text]
    return (res if res else DEFOLT_MESSAG)


class Ai_widget(QDialog, Ui_widget_Gemini):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.run_ia_button.setIcon(QIcon(f"{HOME_PATH}/icon/gemini_image.svg"))
        self.run_ia_button.clicked.connect(self.ai_run_button_press)

    def ai_run_button_press(self, event):
        prompt = self.promt_textEdit.toPlainText()

        global res_ai_text
        res_ai_text += f"""\
## {USER_NAME.rjust(40)}",
{prompt}
## GEMINI
{GEMINI.gemini(prompt)}"""
        self.textEdit.setMarkdown(res_ai_text)


class Ai_Image(QWidget, Ui_widget_input):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.b64 = ""
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.pushButton.setIcon(QIcon(f"{HOME_PATH}/icon/gemini_image.svg"))
        self.pushButton.clicked.connect(self.ai_run_button_press)

    def ai_run_button_press(self, event):
        promt = self.textEdit.toPlainText()

        global res_ai_text
        res_ai_text += f"""\
## {USER_NAME.rjust(40)}
{promt}
## GEMINI
{GEMINI.gemini_image(self.b64, promt)}
"""

        self.dialog_ai = Ai_widget()
        self.dialog_ai.textEdit.setMarkdown(res_ai_text)
        self.dialog_ai.setWindowTitle(f"Gemini : {promt:^20}")
        self.dialog_ai.exec()


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

        self.setupUi(self)
        self.showFullScreen()
        self.start_x = 0
        self.start_y = 0
        self.final_x = 0
        self.final_y = 0
        self.labal = QLabel(self)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            QApplication.quit()

    def translat_button_press(self, event):
        self.text = read_text(self.im_np)

        read_text(self.im_np)

        font = QFont("Noto Sans", 12)
        self.labal.setGeometry(self.start_x,
                               self.start_y,
                               self.w,
                               self.h)
        self.labal.setMinimumSize(self.w, self.h)
        self.labal.setStyleSheet("""
                                 color:#000000;
                                 background: rgb(255,255,255);
                                 border-radius: 6%;
                                 padding:1%;
                                 """)
        self.labal.setFont(font)
        self.labal.setWordWrap(True)
        self.labal.show()
        self.labal.raise_()
        self.labal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labal.adjustSize()
        if 1:
            self.labal.setText(str(g_translate(self.text)))
            self.labal.adjustSize()

    def copy_button_press(self, event):
        self.text = read_text(self.im_np)

        read_text(self.im_np)
        font = QFont("Noto Sans", 12)
        self.labal.setText(" ".join(self.text))
        self.labal.setGeometry(self.start_x,
                               self.start_y,
                               self.w,
                               self.h)
        self.labal.setMinimumSize(self.w, self.h)
        self.labal.setStyleSheet("""
                                 color:#000000;
                                 background: rgb(255,255,255);
                                 border-radius: 6%;
                                 padding:1%;
                                 """)
        self.labal.setFont(font)
        self.labal.setWordWrap(True)
        self.labal.show()
        self.labal.raise_()
        self.labal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.labal.adjustSize()

        clipboard = QApplication.clipboard()
        text = self.labal.text()
        clipboard.setText(text)

    def gemini_button_press(self, event):
        self.imd = Ai_Image(self)
        self.imd.b64 = str(self.b64)

        x = self.start_x+(self.w/2)-230
        if x < 0:
            x = 0

        y = (self.final_y
             if self.final_y > self.start_y
             else self.final_y + self.h)

        if y >= self.height() - 64:
            y = self.height() - 64

        self.imd.move(x, y)
        self.imd.show()
        self.imd.raise_()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            cur = event.position().toPoint()
            x = min(cur.x(), self.start_x)
            y = min(cur.y(), self.start_y)
            w = abs(cur.x() - self.start_x)
            h = abs(cur.y() - self.start_y)
            self.trase_widget.setGeometry(x, y, w, h)
            self.trase_widget.raise_()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            try:
                widgets_to_clean = [
                    ('bl',    True),
                    ('but',   True),
                    ('imd',   True),
                    ('label', False)
                ]

                for attr_name, should_delete in widgets_to_clean:
                    widget = getattr(self, attr_name, None)
                    if widget:
                        widget.setParent(None) 
                        if should_delete:
                            widget.deleteLater()
                self.bl = None
                self.but = None
                self.imd = None
                self.label = None
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
            self.w = abs(self.start_x - self.final_x)
            self.h = abs(self.start_y - self.final_y)
            self.start_x = min(self.final_x, self.start_x)
            self.start_y = min(self.final_y, self.start_y)

            self.im_np, self.b64 = screan(self.start_x,
                                          self.start_y,
                                          self.w,
                                          self.h)

            self.bl = ButtonTop(self)
            self.bl.translateButton.clicked.connect(self.translat_button_press)
            self.bl.copuButton.clicked.connect(self.copy_button_press)
            self.bl.gemini.clicked.connect(self.gemini_button_press)
            self.but = self.bl.widget
            self.but.setParent(self)
            self.but.setStyleSheet("""
                                   background-color: rgb(30, 33, 36);
                                   border-radius:15%;
                                   """)

            but_x = self.start_x+(self.w/2)-131
            but_x = 0 if but_x < 0 else but_x

            if self.start_y-62 > 0:
                but_y = self.start_y - 62
            else:
                but_y = self.start_y + self.h + 8

            if but_y > self.height():
                but_y = 8

            self.but.move(int(but_x), int(but_y))
            self.but.show()
            self.but.raise_()


if __name__ == "__main__":    
    im = ImageGrab.grab()

    im_bytes = im.tobytes("raw", "RGBA")
    WIDTH = im.width
    HEIGHT = im.height
    
    q_image = QImage(im_bytes, WIDTH, HEIGHT, QImage.Format_RGBA8888)
    
    app = QApplication(sys.argv)

    pixmap = QPixmap.fromImage(q_image) 
    window = Widget()
    window.setFixedSize(WIDTH, HEIGHT)

    background_label = QLabel(window)
    background_label.setPixmap(pixmap)
    background_label.setGeometry(0, 0, WIDTH, HEIGHT)
    background_label.show()
            
    window.show()
    sys.exit(app.exec())
