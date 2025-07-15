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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_widget_Gemini(object):
    def setupUi(self, widget_Gemini):
        if not widget_Gemini.objectName():
            widget_Gemini.setObjectName(u"widget_Gemini")
        widget_Gemini.resize(935, 847)
        font = QFont()
        font.setFamilies([u"Noto Naskh Arabic"])
        font.setPointSize(12)
        widget_Gemini.setFont(font)
        widget_Gemini.setStyleSheet(u"margin:20pt;")
        self.verticalLayout = QVBoxLayout(widget_Gemini)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(widget_Gemini)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.textEdit.setFont(font1)
        self.textEdit.setMouseTracking(True)
        self.textEdit.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"padding:8px;\n"
"margin: 8px;\n"
"border-radius: 12%;")
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.widget = QWidget(widget_Gemini)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 46))
        self.widget.setMaximumSize(QSize(16777215, 64))
        self.widget.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"margin: 8px;\n"
"border-radius: 12%;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.promt_textEdit = QTextEdit(self.widget)
        self.promt_textEdit.setObjectName(u"promt_textEdit")
        self.promt_textEdit.setMinimumSize(QSize(0, 44))
        self.promt_textEdit.setMaximumSize(QSize(16777215, 46))
        font2 = QFont()
        font2.setPointSize(12)
        self.promt_textEdit.setFont(font2)

        self.horizontalLayout.addWidget(self.promt_textEdit)

        self.run_ia_button = QPushButton(self.widget)
        self.run_ia_button.setObjectName(u"run_ia_button")
        self.run_ia_button.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.run_ia_button.setFont(font3)
        self.run_ia_button.setStyleSheet(u"padding: 8px;")
        icon = QIcon()
        icon.addFile(u"../icon/gemini_image.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run_ia_button.setIcon(icon)
        self.run_ia_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.run_ia_button)


        self.verticalLayout.addWidget(self.widget)


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
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:normal;\"><br /></p></body></html>", None))
        self.run_ia_button.setText("")
    # retranslateUi

