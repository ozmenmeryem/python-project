# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(633, 393)
        font = QFont()
        font.setKerning(True)
        Widget.setFont(font)
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: #FFF8DC;  /* \u00c7ok a\u00e7\u0131k sar\u0131ms\u0131 krem */\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frameReminderOptions = QWidget(Widget)
        self.frameReminderOptions.setObjectName(u"frameReminderOptions")
        self.frameReminderOptions.setStyleSheet(u"QRadioButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bbb;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #444;\n"
"    min-width: 150px;\n"
"    text-align: center;\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;  /* klasik yuvarla\u011f\u0131 gizle */\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #f0f8ff;\n"
"    border: 2px solid #88c;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #d0f0c0;\n"
"    border: 2px solid #4CAF50;\n"
"    color: #2b4;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.frameReminderOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton3 = QRadioButton(self.frameReminderOptions)
        self.radioButton3.setObjectName(u"radioButton3")
        self.radioButton3.setStyleSheet(u"QRadioButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bbb;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #444;\n"
"    min-width: 150px;\n"
"    text-align: center;\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;  /* klasik yuvarla\u011f\u0131 gizle */\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #f0f8ff;\n"
"    border: 2px solid #88c;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #d0f0c0;\n"
"    border: 2px solid #4CAF50;\n"
"    color: #2b4;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.radioButton3, 3, 1, 1, 1)

        self.radioButton1 = QRadioButton(self.frameReminderOptions)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setAutoFillBackground(False)
        self.radioButton1.setStyleSheet(u"QRadioButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bbb;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #444;\n"
"    min-width: 150px;\n"
"    text-align: center;\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;  /* klasik yuvarla\u011f\u0131 gizle */\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #f0f8ff;\n"
"    border: 2px solid #88c;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #d0f0c0;\n"
"    border: 2px solid #4CAF50;\n"
"    color: #2b4;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.radioButton1, 1, 1, 1, 1)

        self.radioButton2 = QRadioButton(self.frameReminderOptions)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setStyleSheet(u"QRadioButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bbb;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #444;\n"
"    min-width: 150px;\n"
"    text-align: center;\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;  /* klasik yuvarla\u011f\u0131 gizle */\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #f0f8ff;\n"
"    border: 2px solid #88c;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #d0f0c0;\n"
"    border: 2px solid #4CAF50;\n"
"    color: #2b4;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.radioButton2, 2, 1, 1, 1)

        self.radioButton4 = QRadioButton(self.frameReminderOptions)
        self.radioButton4.setObjectName(u"radioButton4")
        self.radioButton4.setStyleSheet(u"QRadioButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #aaa;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0px;  /* yuvarlak noktas\u0131n\u0131 gizle */\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #d0eaff;\n"
"    border: 2px solid #3399ff;\n"
"    color: #000;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.radioButton4, 4, 1, 1, 1)

        self.buttonBack = QPushButton(self.frameReminderOptions)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.buttonBack, 5, 1, 1, 1)

        self.label_hatirlatmaOnayi = QLabel(self.frameReminderOptions)
        self.label_hatirlatmaOnayi.setObjectName(u"label_hatirlatmaOnayi")
        self.label_hatirlatmaOnayi.setStyleSheet(u" background-color: #e6ffe6;\n"
" color: #2d862d;\n"
" border: 2px solid #5cd65c;\n"
" border-radius: 10px;\n"
" padding: 8px;\n"
" font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.label_hatirlatmaOnayi, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frameReminderOptions, 0, 4, 1, 1)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_gorev = QLabel(self.frame)
        self.label_gorev.setObjectName(u"label_gorev")
        self.label_gorev.setStyleSheet(u"QLabel {\n"
"    background-color: #f5f5f5;\n"
"    border: 2px solid #aaa;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #333;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.label_gorev.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_gorev.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_gorev, 1, 0, 1, 2)

        self.startButton = QPushButton(self.frame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(False)
        self.startButton.setFont(font1)
        self.startButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.startButton, 2, 0, 1, 2)

        self.button3 = QPushButton(self.frame)
        self.button3.setObjectName(u"button3")
        self.button3.setEnabled(True)
        self.button3.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/breathing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button3.setIcon(icon)
        self.button3.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.button3, 5, 0, 1, 2)

        self.button4 = QPushButton(self.frame)
        self.button4.setObjectName(u"button4")
        self.button4.setEnabled(True)
        self.button4.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/eyes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button4.setIcon(icon1)
        self.button4.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.button4, 6, 0, 1, 2)

        self.button2 = QPushButton(self.frame)
        self.button2.setObjectName(u"button2")
        self.button2.setEnabled(True)
        self.button2.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads/mineral-water.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button2.setIcon(icon2)
        self.button2.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.button2, 4, 0, 1, 2)

        self.button1 = QPushButton(self.frame)
        self.button1.setObjectName(u"button1")
        self.button1.setEnabled(True)
        self.button1.setMinimumSize(QSize(299, 29))
        self.button1.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../Downloads/orthopedics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button1.setIcon(icon3)
        self.button1.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.button1, 3, 0, 1, 2)

        self.labelWelcome = QLabel(self.frame)
        self.labelWelcome.setObjectName(u"labelWelcome")
        self.labelWelcome.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(26)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(True)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.labelWelcome.setFont(font2)
        self.labelWelcome.setStyleSheet(u"font: 600 italic 26pt \"Segoe UI\";")
        self.labelWelcome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelWelcome, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.radioButton3.setText(QCoreApplication.translate("Widget", u"         45 dakika", None))
        self.radioButton1.setText(QCoreApplication.translate("Widget", u"         1 Dakika", None))
        self.radioButton2.setText(QCoreApplication.translate("Widget", u"         30 dakika", None))
        self.radioButton4.setText(QCoreApplication.translate("Widget", u"        60 dakika", None))
        self.buttonBack.setText("")
        self.label_hatirlatmaOnayi.setText("")
        self.label_gorev.setText("")
        self.startButton.setText(QCoreApplication.translate("Widget", u"BA\u015eLA", None))
        self.button3.setText(QCoreApplication.translate("Widget", u"NEFES EGZERS\u0130ZLER\u0130", None))
        self.button4.setText(QCoreApplication.translate("Widget", u"G\u00d6Z D\u0130NLEND\u0130RME", None))
        self.button2.setText(QCoreApplication.translate("Widget", u"SU \u0130\u00c7ME", None))
        self.button1.setText(QCoreApplication.translate("Widget", u"D\u0130K DURMA", None))
        self.labelWelcome.setText(QCoreApplication.translate("Widget", u"HO\u015eGELD\u0130N\u0130Z", None))
    # retranslateUi

