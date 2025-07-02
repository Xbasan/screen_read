# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        Widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.start_labal = QLabel(Widget)
        self.start_labal.setObjectName(u"start_labal")
        self.start_labal.setGeometry(QRect(755, 505, 410, 70))
        self.start_labal.setMinimumSize(QSize(410, 70))
        self.start_labal.setMaximumSize(QSize(410, 70))
        font = QFont()
        font.setFamilies([u"URW Gothic [urw]"])
        font.setPointSize(14)
        font.setBold(True)
        self.start_labal.setFont(font)
        self.start_labal.setStyleSheet(u"background-color: rgb(30, 33, 36);\n"
"border-radius:12%;")
        self.start_labal.setTextFormat(Qt.TextFormat.MarkdownText)
        self.start_labal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trase_widget = QWidget(Widget)
        self.trase_widget.setObjectName(u"trase_widget")
        self.trase_widget.setGeometry(QRect(0, 0, 0, 0))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.start_labal.setText(QCoreApplication.translate("Widget", u"Click and drag to make a selection", None))
    # retranslateUi

