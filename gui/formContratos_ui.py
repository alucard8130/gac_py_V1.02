# Form implementation generated from reading ui file 'c:\Users\smart\OneDrive\Escritorio\gac_py_V1.02\gui\formContratos.ui'
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
        formClientes.resize(572, 455)
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
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 681, 331))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txtNumContrato = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtNumContrato.setGeometry(QtCore.QRect(10, 40, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.txtNumContrato.setFont(font)
        self.txtNumContrato.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtNumContrato.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.txtNumContrato.setReadOnly(True)
        self.txtNumContrato.setObjectName("txtNumContrato")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_10.setObjectName("label_10")
        self.cmbCliente = QtWidgets.QComboBox(parent=self.frame_2)
        self.cmbCliente.setEnabled(True)
        self.cmbCliente.setGeometry(QtCore.QRect(10, 110, 261, 30))
        self.cmbCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbCliente.setObjectName("cmbCliente")
        self.cmbCliente.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 111, 21))
        self.label_5.setObjectName("label_5")
        self.cmbTipoContrato = QtWidgets.QComboBox(parent=self.frame_2)
        self.cmbTipoContrato.setEnabled(True)
        self.cmbTipoContrato.setGeometry(QtCore.QRect(340, 40, 211, 30))
        self.cmbTipoContrato.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbTipoContrato.setObjectName("cmbTipoContrato")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.dateInicial = QtWidgets.QDateEdit(parent=self.frame_2)
        self.dateInicial.setGeometry(QtCore.QRect(340, 110, 211, 30))
        self.dateInicial.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dateInicial.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.dateInicial.setCalendarPopup(True)
        self.dateInicial.setObjectName("dateInicial")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(340, 90, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(340, 180, 71, 21))
        self.label_8.setObjectName("label_8")
        self.dateFinal = QtWidgets.QDateEdit(parent=self.frame_2)
        self.dateFinal.setGeometry(QtCore.QRect(340, 200, 211, 30))
        self.dateFinal.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dateFinal.setCalendarPopup(True)
        self.dateFinal.setObjectName("dateFinal")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 261, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmbAreaComun = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cmbAreaComun.setEnabled(True)
        self.cmbAreaComun.setGeometry(QtCore.QRect(10, 40, 241, 30))
        self.cmbAreaComun.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbAreaComun.setObjectName("cmbAreaComun")
        self.cmbAreaComun.addItem("")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label_12.setObjectName("label_12")
        self.txtDG = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtDG.setGeometry(QtCore.QRect(140, 110, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDG.setFont(font)
        self.txtDG.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtDG.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.txtDG.setReadOnly(True)
        self.txtDG.setObjectName("txtDG")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(140, 90, 61, 16))
        self.label_13.setObjectName("label_13")
        self.txtCuota = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtCuota.setGeometry(QtCore.QRect(10, 110, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCuota.setFont(font)
        self.txtCuota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCuota.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.txtCuota.setReadOnly(True)
        self.txtCuota.setObjectName("txtCuota")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 41, 16))
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(parent=formClientes)
        self.frame_3.setGeometry(QtCore.QRect(10, 400, 654, 51))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnGuardar = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnGuardar.setGeometry(QtCore.QRect(0, 12, 261, 30))
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
        self.btnSalir.setGeometry(QtCore.QRect(330, 10, 211, 30))
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
        self.label_6.setText(_translate("formClientes", " REGISTRO CONTRATOS"))
        self.label_10.setText(_translate("formClientes", "Num Contrato"))
        self.cmbCliente.setItemText(0, _translate("formClientes", "---seleccione una opcion..."))
        self.label_3.setText(_translate("formClientes", "Cliente"))
        self.label_5.setText(_translate("formClientes", "Tipo Contrato"))
        self.cmbTipoContrato.setItemText(0, _translate("formClientes", "---seleccione una opcion..."))
        self.cmbTipoContrato.setItemText(1, _translate("formClientes", "Arrendamiento"))
        self.cmbTipoContrato.setItemText(2, _translate("formClientes", "Comodato"))
        self.cmbTipoContrato.setItemText(3, _translate("formClientes", "Uso o Goce"))
        self.label_4.setText(_translate("formClientes", "Fecha Inicio"))
        self.label_8.setText(_translate("formClientes", "Fecha Fin"))
        self.groupBox_2.setTitle(_translate("formClientes", "Area"))
        self.cmbAreaComun.setItemText(0, _translate("formClientes", "---seleccione una opcion..."))
        self.label_12.setText(_translate("formClientes", "Numero"))
        self.label_13.setText(_translate("formClientes", "Deposito"))
        self.label_7.setText(_translate("formClientes", "Cuota"))
        self.btnGuardar.setText(_translate("formClientes", "Guardar"))
        self.btnSalir.setText(_translate("formClientes", "Salir"))
