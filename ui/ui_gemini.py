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
        self.textEdit.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"padding:10px;\n"
"border-radius: 12%;")
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)


        self.retranslateUi(widget_Gemini)

        QMetaObject.connectSlotsByName(widget_Gemini)
    # setupUi

    def retranslateUi(self, widget_Gemini):
        widget_Gemini.setWindowTitle(QCoreApplication.translate("widget_Gemini", u"Form", None))
        self.textEdit.setHtml(QCoreApplication.translate("widget_Gemini", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

