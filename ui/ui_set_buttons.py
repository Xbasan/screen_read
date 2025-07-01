# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_buttons.ui'
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
    QWidget)

class Ui_widgetButtonTop(object):
    def setupUi(self, widgetButtonTop):
        if not widgetButtonTop.objectName():
            widgetButtonTop.setObjectName(u"widgetButtonTop")
        widgetButtonTop.resize(531, 284)
        widgetButtonTop.setStyleSheet(u"QPushButton::hover#start_stop_button\n"
"{\n"
"background-color: rgb(25, 25, 25);\n"
"}")
        self.widget = QWidget(widgetButtonTop)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 120, 260, 54))
        self.widget.setStyleSheet(u"background-color: rgb(30, 33, 36);                        \n"
"border-radius:12%;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copuButton = QPushButton(self.widget)
        self.copuButton.setObjectName(u"copuButton")
        self.copuButton.setMinimumSize(QSize(0, 36))
        self.copuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.copuButton.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/copi.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copuButton.setIcon(icon)
        self.copuButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.copuButton)

        self.translateButton = QPushButton(self.widget)
        self.translateButton.setObjectName(u"translateButton")
        self.translateButton.setMinimumSize(QSize(0, 36))
        self.translateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.translateButton.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/translate.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.translateButton.setIcon(icon1)
        self.translateButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.translateButton)

        self.gemini = QPushButton(self.widget)
        self.gemini.setObjectName(u"gemini")
        self.gemini.setMinimumSize(QSize(0, 36))
        self.gemini.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gemini.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"")
        self.gemini.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.gemini)

        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(0, 36))
        self.exitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exitButton.setStyleSheet(u"background-color:rgb(70, 77, 86);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icon/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exitButton.setIcon(icon2)
        self.exitButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.exitButton)


        self.retranslateUi(widgetButtonTop)

        QMetaObject.connectSlotsByName(widgetButtonTop)
    # setupUi

    def retranslateUi(self, widgetButtonTop):
        widgetButtonTop.setWindowTitle(QCoreApplication.translate("widgetButtonTop", u"Form", None))
#if QT_CONFIG(tooltip)
        self.copuButton.setToolTip(QCoreApplication.translate("widgetButtonTop", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.copuButton.setText("")
#if QT_CONFIG(tooltip)
        self.translateButton.setToolTip(QCoreApplication.translate("widgetButtonTop", u"<html><head/><body><p align=\"center\">Translate</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.translateButton.setText("")
        self.gemini.setText("")
#if QT_CONFIG(tooltip)
        self.exitButton.setToolTip(QCoreApplication.translate("widgetButtonTop", u"<html><head/><body><p align=\"center\">Exir</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exitButton.setText("")
    # retranslateUi

