# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesDxALCs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(338, 349)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 120, 229, 161))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_layout = QVBoxLayout(self.frame_2)
        self.btn_layout.setSpacing(35)
        self.btn_layout.setObjectName(u"btn_layout")
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 50, 271, 31))
        self.edit_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.edit_layout.setObjectName(u"edit_layout")
        self.edit_layout.setContentsMargins(0, 0, 0, 0)

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 20, 316, 21))
        self.label.setTextFormat(Qt.AutoText)
        self.verticalLayoutWidget = QWidget(self.frame_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 291, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalLayoutWidget_2 = QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 200, 302, 91))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)


        self.page_2_layout.addWidget(self.frame_3)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"made by \u897f\u7c73\u5c4b\u82b1\u706b", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"how to use:", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"1.\u9009\u62e9\u8981\u6258\u7ba1\u7684\u6d4f\u89c8\u5668", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"2.\u542f\u52a8\u6258\u7ba1\u6d4f\u89c8\u5668", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"3.\u5728\u6258\u7ba1\u6d4f\u89c8\u5668\u4e2d\u6253\u5f00\u667a\u969c\u6811\u9700\u8981\u6258\u7ba1\u7684\u89c6\u9891\u9875\u9762", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"4.\u5f00\u59cb\u6258\u7ba1", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"declaration:", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"\u8fd9\u4e2a\u7a0b\u5e8f\u53ea\u662f\u6258\u7ba1\u6d4f\u89c8\u5668\uff0c\u4e0d\u4fee\u6539\u5185\u90e8\u6570\u636e", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"\u8bf7\u540c\u5b66\u8ba4\u771f\u542c\u8bfe\uff01", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"\u4e00\u5207\u540e\u679c\u81ea\u884c\u8d1f\u8d23", None))
    # retranslateUi

