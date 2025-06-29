# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gemini.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTextEdit,
    QWidget)

class Ui_widget_Gemini(object):
    def setupUi(self, widget_Gemini):
        if not widget_Gemini.objectName():
            widget_Gemini.setObjectName(u"widget_Gemini")
        widget_Gemini.resize(935, 847)
        widget_Gemini.setStyleSheet(u"margin:20pt;")
        self.gridLayout = QGridLayout(widget_Gemini)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(widget_Gemini)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setMouseTracking(True)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)


        self.retranslateUi(widget_Gemini)

        QMetaObject.connectSlotsByName(widget_Gemini)
    # setupUi

    def retranslateUi(self, widget_Gemini):
        widget_Gemini.setWindowTitle(QCoreApplication.translate("widget_Gemini", u"Form", None))
    # retranslateUi

