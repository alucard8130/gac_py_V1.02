# Form implementation generated from reading ui file 'c:\Users\smart\OneDrive\Escritorio\gac_py_V1.02\gui\formClientes.ui'
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
        formClientes.resize(672, 487)
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
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 681, 351))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txtNombreCliente = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtNombreCliente.setGeometry(QtCore.QRect(20, 90, 280, 30))
        self.txtNombreCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtNombreCliente.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtNombreCliente.setObjectName("txtNombreCliente")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 49, 21))
        self.label_4.setObjectName("label_4")
        self.txtDireccion = QtWidgets.QTextEdit(parent=self.frame_2)
        self.txtDireccion.setGeometry(QtCore.QRect(370, 280, 281, 51))
        self.txtDireccion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtDireccion.setObjectName("txtDireccion")
        self.cmbTipoContribuyente = QtWidgets.QComboBox(parent=self.frame_2)
        self.cmbTipoContribuyente.setEnabled(True)
        self.cmbTipoContribuyente.setGeometry(QtCore.QRect(20, 220, 280, 30))
        self.cmbTipoContribuyente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbTipoContribuyente.setObjectName("cmbTipoContribuyente")
        self.cmbTipoContribuyente.addItem("")
        self.cmbTipoContribuyente.addItem("")
        self.cmbTipoContribuyente.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(370, 260, 49, 16))
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 280, 41))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.checkBoxStatus = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxStatus.setGeometry(QtCore.QRect(180, 10, 93, 16))
        self.checkBoxStatus.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.checkBoxStatus.setObjectName("checkBoxStatus")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(370, 10, 49, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(380, 140, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(370, 70, 111, 16))
        self.label_9.setObjectName("label_9")
        self.txtRFC = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtRFC.setGeometry(QtCore.QRect(20, 160, 280, 30))
        self.txtRFC.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtRFC.setMaxLength(13)
        self.txtRFC.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtRFC.setObjectName("txtRFC")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtEmail.setGeometry(QtCore.QRect(370, 30, 281, 30))
        self.txtEmail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtEmail.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtEmail.setObjectName("txtEmail")
        self.txtCel = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtCel.setGeometry(QtCore.QRect(370, 90, 281, 30))
        self.txtCel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtCel.setObjectName("txtCel")
        self.txtGiro = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtGiro.setGeometry(QtCore.QRect(370, 160, 281, 30))
        self.txtGiro.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtGiro.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtGiro.setObjectName("txtGiro")
        self.txtCURP = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtCURP.setGeometry(QtCore.QRect(20, 290, 280, 30))
        self.txtCURP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCURP.setText("")
        self.txtCURP.setMaxLength(18)
        self.txtCURP.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtCURP.setObjectName("txtCURP")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(370, 200, 111, 21))
        self.label_12.setObjectName("label_12")
        self.cmbTipoCliente = QtWidgets.QComboBox(parent=self.frame_2)
        self.cmbTipoCliente.setEnabled(True)
        self.cmbTipoCliente.setGeometry(QtCore.QRect(370, 220, 281, 30))
        self.cmbTipoCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbTipoCliente.setObjectName("cmbTipoCliente")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.frame_3 = QtWidgets.QFrame(parent=formClientes)
        self.frame_3.setGeometry(QtCore.QRect(0, 420, 701, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnGuardar = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnGuardar.setGeometry(QtCore.QRect(20, 20, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGuardar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnGuardar.setStyleSheet("background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/guardar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QtCore.QSize(30, 30))
        self.btnGuardar.setFlat(True)
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnSalir = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnSalir.setGeometry(QtCore.QRect(370, 20, 281, 30))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QtCore.QSize(20, 20))
        self.btnSalir.setFlat(True)
        self.btnSalir.setObjectName("btnSalir")

        self.retranslateUi(formClientes)
        QtCore.QMetaObject.connectSlotsByName(formClientes)

    def retranslateUi(self, formClientes):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("formClientes", " REGISTRO CLIENTES CUOTAS"))
        self.label_4.setText(_translate("formClientes", "CURP"))
        self.cmbTipoContribuyente.setItemText(0, _translate("formClientes", "---seleccione una opcion..."))
        self.cmbTipoContribuyente.setItemText(1, _translate("formClientes", "Persona Fisica"))
        self.cmbTipoContribuyente.setItemText(2, _translate("formClientes", "Persona Moral"))
        self.label_3.setText(_translate("formClientes", "Tipo Contribuyente"))
        self.label_8.setText(_translate("formClientes", "Direccion"))
        self.groupBox.setTitle(_translate("formClientes", "Status"))
        self.checkBoxStatus.setText(_translate("formClientes", "Cliente Activo"))
        self.label_5.setText(_translate("formClientes", "Email"))
        self.label_7.setText(_translate("formClientes", "Giro"))
        self.label_9.setText(_translate("formClientes", "Numero Telefonico"))
        self.label_10.setText(_translate("formClientes", "Razon Social"))
        self.label_11.setText(_translate("formClientes", "RFC"))
        self.label_12.setText(_translate("formClientes", "Tipo Cliente"))
        self.cmbTipoCliente.setItemText(0, _translate("formClientes", "---seleccione una opcion..."))
        self.cmbTipoCliente.setItemText(1, _translate("formClientes", "Areas Comunes"))
        self.cmbTipoCliente.setItemText(2, _translate("formClientes", "Locales Comerciales"))
        self.cmbTipoCliente.setItemText(3, _translate("formClientes", "Espacios Publicitarios"))
        self.cmbTipoCliente.setItemText(4, _translate("formClientes", "Estacionamiento"))
        self.cmbTipoCliente.setItemText(5, _translate("formClientes", "Recuperacion Servicios"))
        self.btnGuardar.setText(_translate("formClientes", "Guardar"))
        self.btnSalir.setText(_translate("formClientes", "Salir"))
