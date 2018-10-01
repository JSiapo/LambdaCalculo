# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(735, 553)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowOpacity(0.99)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_formula = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.txt_formula.setFont(font)
        self.txt_formula.setObjectName("txt_formula")
        self.gridLayout.addWidget(self.txt_formula, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txt_valores = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.txt_valores.setFont(font)
        self.txt_valores.setObjectName("txt_valores")
        self.gridLayout.addWidget(self.txt_valores, 1, 1, 1, 1)
        self.txt_resultado = QtWidgets.QTextEdit(Dialog)
        self.txt_resultado.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(60)
        self.txt_resultado.setFont(font)
        self.txt_resultado.setAcceptDrops(True)
        self.txt_resultado.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setObjectName("txt_resultado")
        self.gridLayout.addWidget(self.txt_resultado, 2, 0, 1, 2)
        self.btn_ejecutar = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.btn_ejecutar.setFont(font)
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        self.gridLayout.addWidget(self.btn_ejecutar, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lambda Calculo"))
        self.label.setText(_translate("Dialog", "Ingrese Función    "))
        self.txt_formula.setPlaceholderText(_translate("Dialog", "Ingrese fórmula"))
        self.label_2.setText(_translate("Dialog", "Ingrese Valores    "))
        self.txt_valores.setPlaceholderText(_translate("Dialog", "Ingrese valores separados por ,"))
        self.btn_ejecutar.setText(_translate("Dialog", "Ejecutar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
