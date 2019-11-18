# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alterar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 353)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 310, 331, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 341, 281))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 321, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.y3_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y3_edit.setObjectName("y3_edit")
        self.gridLayout.addWidget(self.y3_edit, 2, 3, 1, 1)
        self.y2_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y2_edit.setObjectName("y2_edit")
        self.gridLayout.addWidget(self.y2_edit, 1, 3, 1, 1)
        self.y1_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y1_edit.setObjectName("y1_edit")
        self.gridLayout.addWidget(self.y1_edit, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.x3_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x3_edit.setObjectName("x3_edit")
        self.gridLayout.addWidget(self.x3_edit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.x2_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x2_edit.setObjectName("x2_edit")
        self.gridLayout.addWidget(self.x2_edit, 1, 1, 1, 1)
        self.x1_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x1_edit.setObjectName("x1_edit")
        self.gridLayout.addWidget(self.x1_edit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.x4_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x4_edit.setObjectName("x4_edit")
        self.gridLayout.addWidget(self.x4_edit, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.y4_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y4_edit.setObjectName("y4_edit")
        self.gridLayout.addWidget(self.y4_edit, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Alterar Coordenadas:"))
        self.label_4.setText(_translate("Dialog", "y2"))
        self.label_6.setText(_translate("Dialog", "y3"))
        self.label.setText(_translate("Dialog", "x1"))
        self.label_2.setText(_translate("Dialog", "y1"))
        self.label_5.setText(_translate("Dialog", "x3"))
        self.label_3.setText(_translate("Dialog", "x2"))
        self.label_7.setText(_translate("Dialog", "x4"))
        self.label_8.setText(_translate("Dialog", "y4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
