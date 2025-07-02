# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_dialog.ui'
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
    QTextEdit, QWidget)

class Ui_widget_input(object):
    def setupUi(self, widget_input):
        if not widget_input.objectName():
            widget_input.setObjectName(u"widget_input")
        widget_input.resize(460, 68)
        widget_input.setStyleSheet(u"border-radius:14px;")
        self.horizontalLayout = QHBoxLayout(widget_input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(widget_input)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 42))
        font = QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"padding:4px;\n"
"")

        self.horizontalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(widget_input)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(42, 42))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(widget_input)

        QMetaObject.connectSlotsByName(widget_input)
    # setupUi

    def retranslateUi(self, widget_input):
        widget_input.setWindowTitle(QCoreApplication.translate("widget_input", u"Form", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("widget_input", u"<html><head/><body><p align=\"center\">Exir</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
    # retranslateUi

