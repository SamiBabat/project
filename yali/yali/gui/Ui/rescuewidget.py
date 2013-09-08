# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yali/gui/Ui/rescuewidget.ui'
#
# Created: Fri Apr  5 17:37:32 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import gettext
__trans = gettext.translation('yali', fallback=True)
i18n = __trans.ugettext
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RescueWidget(object):
    def setupUi(self, RescueWidget):
        RescueWidget.setObjectName(_fromUtf8("RescueWidget"))
        RescueWidget.resize(785, 524)
        self.gridLayout = QtGui.QGridLayout(RescueWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(RescueWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(600, 250))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame.setStyleSheet(_fromUtf8("#frame{\n"
"background-color: rgba(0, 0, 0, 20);\n"
"border-top: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"border-bottom: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"QListView {\n"
"show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
" }\n"
"\n"
"QListView{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius:2px;\n"
"color:white;\n"
"}\n"
"\n"
"QListView::item {\n"
"border-radius:2;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0));\n"
"color: rgb(220, 220, 220);\n"
"padding:5\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"border-radius:2;\n"
"color:white;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"border-radius:2;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"color:white;\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(203, 239, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rescueGrub = QtGui.QRadioButton(self.groupBox)
        self.rescueGrub.setIconSize(QtCore.QSize(48, 48))
        self.rescueGrub.setChecked(True)
        self.rescueGrub.setObjectName(_fromUtf8("rescueGrub"))
        self.gridLayout_2.addWidget(self.rescueGrub, 0, 0, 1, 1)
        self.rescuePassword = QtGui.QRadioButton(self.groupBox)
        self.rescuePassword.setEnabled(True)
        self.rescuePassword.setStyleSheet(_fromUtf8(""))
        self.rescuePassword.setIconSize(QtCore.QSize(48, 48))
        self.rescuePassword.setObjectName(_fromUtf8("rescuePassword"))
        self.gridLayout_2.addWidget(self.rescuePassword, 2, 0, 1, 1)
        self.rescuePisi = QtGui.QRadioButton(self.groupBox)
        self.rescuePisi.setStyleSheet(_fromUtf8(""))
        self.rescuePisi.setIconSize(QtCore.QSize(48, 48))
        self.rescuePisi.setObjectName(_fromUtf8("rescuePisi"))
        self.gridLayout_2.addWidget(self.rescuePisi, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.rescueSystems = QtGui.QListWidget(self.frame)
        self.rescueSystems.setMaximumSize(QtCore.QSize(16777215, 100))
        self.rescueSystems.setObjectName(_fromUtf8("rescueSystems"))
        self.verticalLayout.addWidget(self.rescueSystems)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(RescueWidget)
        QtCore.QMetaObject.connectSlotsByName(RescueWidget)

    def retranslateUi(self, RescueWidget):
        self.groupBox.setTitle(i18n("Choose what do you want to do to repair your system"))
        self.rescueGrub.setText(i18n("Reinstall bootloader"))
        self.rescuePassword.setText(i18n("Reset forgotten password"))
        self.rescuePisi.setText(i18n("Return back to a previous system state"))

