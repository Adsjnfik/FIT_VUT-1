# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_help_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_windowHelp(object):
    def setupUi(self, windowHelp):
        windowHelp.setObjectName("windowHelp")
        windowHelp.resize(574, 279)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(windowHelp.sizePolicy().hasHeightForWidth())
        windowHelp.setSizePolicy(sizePolicy)
        windowHelp.setMinimumSize(QtCore.QSize(574, 279))
        windowHelp.setMaximumSize(QtCore.QSize(574, 279))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.xpm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowHelp.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(windowHelp)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(windowHelp)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(windowHelp)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 301, 21))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(windowHelp)
        self.label_4.setGeometry(QtCore.QRect(70, 80, 261, 21))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(windowHelp)
        self.label_5.setGeometry(QtCore.QRect(70, 100, 261, 21))
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(windowHelp)
        self.label_6.setGeometry(QtCore.QRect(70, 120, 261, 21))
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(windowHelp)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 361, 21))
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(windowHelp)
        self.label_8.setGeometry(QtCore.QRect(10, 200, 371, 21))
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(windowHelp)
        self.label_9.setGeometry(QtCore.QRect(330, 200, 141, 21))
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(windowHelp)
        self.label_10.setGeometry(QtCore.QRect(10, 220, 471, 21))
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(windowHelp)
        self.label_11.setGeometry(QtCore.QRect(480, 220, 81, 21))
        self.label_11.setStyleSheet("color:white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(windowHelp)
        self.label_12.setGeometry(QtCore.QRect(10, 250, 361, 21))
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(windowHelp)
        self.label_13.setGeometry(QtCore.QRect(-10, -10, 604, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(604, 331))
        self.label_13.setMaximumSize(QtCore.QSize(604, 331))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(54, 22, 113, 255), stop:1 rgba(167, 134, 255, 255));\n"
"color: rgb(243, 243, 243);\n"
"border:none;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()

        self.retranslateUi(windowHelp)
        QtCore.QMetaObject.connectSlotsByName(windowHelp)

    def retranslateUi(self, windowHelp):
        _translate = QtCore.QCoreApplication.translate
        windowHelp.setWindowTitle(_translate("windowHelp", "Help"))
        self.label.setText(_translate("windowHelp", "Help"))
        self.label_2.setText(_translate("windowHelp", "To use this calculator simply:"))
        self.label_3.setText(_translate("windowHelp", "1) Enter first operand via mouse click"))
        self.label_4.setText(_translate("windowHelp", "2) Select operator you wish to use"))
        self.label_5.setText(_translate("windowHelp", "3) Enter second operand if needed"))
        self.label_6.setText(_translate("windowHelp", "4) Click equal to evaluate the result"))
        self.label_7.setText(_translate("windowHelp", "Unary operators don\'t require user to select equal."))
        self.label_8.setText(_translate("windowHelp", "When calculator notifies user with a message:"))
        self.label_9.setText(_translate("windowHelp", "\"Invalid expression\"."))
        self.label_10.setText(_translate("windowHelp", "It\'s only needed to start entering numbers or select the clear button"))
        self.label_11.setText(_translate("windowHelp", "to continue."))
        self.label_12.setText(_translate("windowHelp", "To exit application, click the X button top right."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowHelp = QtWidgets.QWidget()
    ui = Ui_windowHelp()
    ui.setupUi(windowHelp)
    windowHelp.show()
    sys.exit(app.exec_())
