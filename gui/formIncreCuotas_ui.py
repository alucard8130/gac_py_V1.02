# Form implementation generated from reading ui file 'c:\Users\smart\OneDrive\Escritorio\gac_py_V1.02\gui\formIncreCuotas.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_formClientes(object):
    def setupUi(self, formClientes):
        formClientes.setObjectName("formClientes")
        formClientes.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        formClientes.resize(379, 326)
        formClientes.setWindowTitle("")
        formClientes.setStyleSheet("background-color: rgb(245, 245, 252);")
        self.frame = QtWidgets.QFrame(parent=formClientes)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 71))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(8, 14, 91);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 40, 832, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(parent=formClientes)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 681, 211))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.cmb_tcuota = QtWidgets.QComboBox(parent=self.frame_2)
        self.cmb_tcuota.setGeometry(QtCore.QRect(90, 50, 200, 30))
        self.cmb_tcuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmb_tcuota.setObjectName("cmb_tcuota")
        self.cmb_tcuota.addItem("")
        self.cmb_tcuota.addItem("")
        self.cmb_tcuota.addItem("")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 30, 91, 16))
        self.label.setObjectName("label")
        self.txt_porcentaje = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txt_porcentaje.setGeometry(QtCore.QRect(90, 130, 200, 30))
        self.txt_porcentaje.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txt_porcentaje.setObjectName("txt_porcentaje")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 131, 16))
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(parent=formClientes)
        self.frame_3.setGeometry(QtCore.QRect(-10, 280, 681, 51))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnSalir = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnSalir.setGeometry(QtCore.QRect(230, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.btnSalir.setFont(font)
        self.btnSalir.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet("background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSalir.setIcon(icon)
        self.btnSalir.setIconSize(QtCore.QSize(20, 20))
        self.btnSalir.setFlat(True)
        self.btnSalir.setObjectName("btnSalir")
        self.btnEjecutar = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnEjecutar.setGeometry(QtCore.QRect(20, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.btnEjecutar.setFont(font)
        self.btnEjecutar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnEjecutar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnEjecutar.setStyleSheet("background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/entrar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnEjecutar.setIcon(icon1)
        self.btnEjecutar.setIconSize(QtCore.QSize(30, 30))
        self.btnEjecutar.setFlat(True)
        self.btnEjecutar.setObjectName("btnEjecutar")

        self.retranslateUi(formClientes)
        QtCore.QMetaObject.connectSlotsByName(formClientes)

    def retranslateUi(self, formClientes):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("formClientes", " INCREMENTAR CUOTAS "))
        self.cmb_tcuota.setItemText(0, _translate("formClientes", "---selecciona una opcion----"))
        self.cmb_tcuota.setItemText(1, _translate("formClientes", "locales comerciales"))
        self.cmb_tcuota.setItemText(2, _translate("formClientes", "areas comunes"))
        self.label.setText(_translate("formClientes", "Tipo de Cuota"))
        self.label_2.setText(_translate("formClientes", "Porcentaje Incremento"))
        self.btnSalir.setText(_translate("formClientes", "Salir"))
        self.btnEjecutar.setText(_translate("formClientes", "Ejecutar"))
