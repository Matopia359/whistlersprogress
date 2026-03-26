# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(187, 427)
        self.todoframe = QFrame(Widget)
        self.todoframe.setObjectName(u"todoframe")
        self.todoframe.setGeometry(QRect(10, 120, 171, 291))
        self.todoframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.todoframe.setFrameShadow(QFrame.Shadow.Raised)
        self.newvalue = QPlainTextEdit(Widget)
        self.newvalue.setObjectName(u"newvalue")
        self.newvalue.setGeometry(QRect(10, 90, 171, 21))
        self.criar = QPushButton(Widget)
        self.criar.setObjectName(u"criar")
        self.criar.setGeometry(QRect(30, 60, 121, 23))
        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 191, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 80, 191, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, -10, 20, 451))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(Widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(159, 0, 41, 431))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 16))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 30, 91, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
#if QT_CONFIG(statustip)
        self.newvalue.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.newvalue.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.criar.setText(QCoreApplication.translate("Widget", u"put new stuff", None))
        self.label.setText(QCoreApplication.translate("Widget", u"put what do u want todo in the", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"placeholder", None))
    # retranslateUi

